from unittest import TestCase
from pathlib import Path
import docker
import os
import tarfile
import pytest


class BuildImageBase(TestCase):
    __test__ = False

    @classmethod
    def setUpClass(cls, runtime, dockerfile, dep_manager=None):
        """
        Test setup for each build image

        :param runtime: runtime of the build image
        :param dockerfile: dockerfile name of the build image
        :param dep_manager: dependency manager of the build image
        """
        cls.image = f"amazon/aws-sam-cli-build-image-{runtime}:latest"
        cls.app_location = f"tests/buildimages/apps/{runtime}"
        cls.runtime = runtime
        cls.dep_manager = dep_manager
        cls.client = docker.from_env()
        cls.sam_version = os.getenv("SAM_CLI_VERSION")
        TestCase().assertTrue(
            cls.sam_version
        )  # check if SAM_CLI_VERSION env variable is set

        cls.docker_image = None
        try:  # check if the image exists, else build one
            cls.client.images.get(cls.image)
        except docker.errors.ImageNotFound:
            cls.docker_image = cls.client.images.build(
                path="build-image-src/",
                dockerfile=dockerfile,
                tag=cls.image,
                buildargs={"SAM_CLI_VERSION": cls.sam_version},
            )

    @classmethod
    def tearDownClass(cls):
        """
        Cleanup after testing the build image.
        Removes all stopped containers and images built by the setUpClass.
        """
        cls.client.containers.prune()
        if cls.docker_image:
            cls.client.images.remove(image=cls.image, force=True)
            cls.client.images.remove(
                image=f"amazon/aws-sam-cli-emulation-image-{cls.runtime}", force=True
            )

        cls.client.images.prune()

    def test_common_packages(self):
        """
        Test common packages present in all build images
        """
        self.assertTrue(
            self.check_package_output(
                "sam --version", f"SAM CLI, version {self.sam_version}"
            )
        )
        self.assertTrue(self.is_package_present("aws"))
        self.assertTrue(self.is_package_present("jq"))

    def test_non_root_user(self):
        """
        Test using non-root `sam` user
        """
        output = (
            self.client.containers.run(image=self.image, user="sam", command="whoami")
            .decode()
            .strip()
        )
        self.assertEqual(output, "sam")

    def test_sam_init(self):
        """
        Test sam init hello world application for the given runtime and dependency manager
        """
        if self.runtime == "provided" or self.runtime == "provided.al2":
            pytest.skip("Skipping sam init test for self-provided images")

        op = self.client.containers.run(
            image=self.image,
            command=[
                "/bin/sh",
                "-c",
                f"sam init --name sam-app --runtime {self.runtime} --dependency-manager {self.dep_manager} --app-template hello-world && cd sam-app && sam build",
            ],
        ).decode()
        self.assertTrue(op.find("Build Succeeded"))

    def test_external_apps(self):
        """
        BYOApps for testing inside the build image. Place your apps in the tests/buildimages/apps/{runtime} folder
        """
        apps = []
        try:
            _, apps, _ = next(os.walk(self.app_location))  # Get all directories one level below the app location
        except StopIteration:  # When no apps are present in the app location
            pytest.skip("No external apps found for testing.")

        for app in apps:
            # For each app, check if app contains template.yaml file, make a tarball of the app directory,
            # start a container, extract the tarball in the container and build the app
            app_path = Path().resolve().joinpath(self.app_location, app)
            if app_path.joinpath("template.yaml").is_file():
                with tarfile.open(app + ".tar", "w") as tar:
                    tar.add(app_path, app)

                tar_data = open(app + ".tar", "rb").read()

                container = self.client.containers.run(
                    self.image, "/bin/bash", detach=True, tty=True
                )
                container.put_archive("/var/task", tar_data)
                ex_code, out = container.exec_run(
                    "sam build", workdir="/var/task/" + app
                )
                os.remove(app + ".tar")
                container.kill()

                self.assertTrue(out.decode().find("Build Succeeded"))

    def is_package_present(self, package):
        """
        Helper function to check if a package is present in the image
        """
        try:
            self.client.containers.run(
                self.image, command=["/bin/sh", "-c", f"command -v {package}"]
            )
            return True
        except docker.errors.ContainerError:
            return False

    def check_package_output(self, pkg_cmd, output, std_err=False):
        """
        Helper function to check a package's actual output contains the given expected substring
        """
        return (
            output
            in self.client.containers.run(self.image, pkg_cmd, stderr=std_err)
            .decode()
            .strip()
        )
