import pytest
from tests.build_image_base_test import BuildImageBase


@pytest.mark.java8
class TestBIJava8(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java8", "Dockerfile-java8", "maven")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "1.8', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("x86_64"))


class TestBIJava8AL2(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java8.al2", "Dockerfile-java8-al2", "gradle", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "1.8', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("x86_64"))


class TestBIJava8AL2ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java8.al2", "Dockerfile-java8-al2", "gradle", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "1.8', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("aarch64"))


class TestBIJava11(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java11", "Dockerfile-java11", "maven", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "11.0.', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("x86_64"))


class TestBIJava11ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java11", "Dockerfile-java11", "maven", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "11.0.', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("aarch64"))

@pytest.mark.nodejs10x
class TestBINode10(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("nodejs10.x", "Dockerfile-nodejs10x", "npm")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("node --version", "v10."))
        self.assertTrue(self.is_package_present("npm"))
        self.assertTrue(self.is_architecture("x86_64"))


class TestBINode12(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("nodejs12.x", "Dockerfile-nodejs12x", "npm", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("node --version", "v12."))
        self.assertTrue(self.is_package_present("npm"))
        self.assertTrue(self.is_architecture("x86_64"))


class TestBINode12ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("nodejs12.x", "Dockerfile-nodejs12x", "npm", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("node --version", "v12."))
        self.assertTrue(self.is_package_present("npm"))
        self.assertTrue(self.is_architecture("aarch64"))


class TestBINode14(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("nodejs14.x", "Dockerfile-nodejs14x", "npm", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("node --version", "v14."))
        self.assertTrue(self.is_package_present("npm"))
        self.assertTrue(self.is_architecture("x86_64"))


class TestBINode14ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("nodejs14.x", "Dockerfile-nodejs14x", "npm", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("node --version", "v14."))
        self.assertTrue(self.is_package_present("npm"))
        self.assertTrue(self.is_architecture("aarch64"))


@pytest.mark.python27
class TestBIPython27(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python2.7", "Dockerfile-python27", "pip")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("python --version", "Python 2.7.", True)
        )
        self.assertTrue(self.is_package_present("pip"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.python36
class TestBIPython36(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.6", "Dockerfile-python36", "pip")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.6."))
        self.assertTrue(self.is_package_present("pip"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.python37
class TestBIPython37(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.7", "Dockerfile-python37", "pip")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.7."))
        self.assertTrue(self.is_package_present("pip"))
        self.assertTrue(self.is_architecture("x86_64"))


class TestBIPython38(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.8", "Dockerfile-python38", "pip", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.8."))
        self.assertTrue(self.is_package_present("pip"))
        self.assertTrue(self.is_architecture("x86_64"))


class TestBIPython38ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.8", "Dockerfile-python38", "pip", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.8."))
        self.assertTrue(self.is_package_present("pip"))
        self.assertTrue(self.is_architecture("aarch64"))


class TestBIPython39(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.9", "Dockerfile-python39", "pip", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.9."))
        self.assertTrue(self.is_package_present("pip"))


class TestBIPython39ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.9", "Dockerfile-python39", "pip", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.9."))
        self.assertTrue(self.is_package_present("pip"))


@pytest.mark.dotnetcore31.x86_64
class TestBIDotNetCore31(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("dotnetcore3.1", "Dockerfile-dotnetcore31", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("dotnet --version", "3.1"))
        self.assertTrue(self.is_package_present("dotnet"))


@pytest.mark.dotnetcore31.arm64
class TestBIDotNetCore31Arm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("dotnetcore3.1", "Dockerfile-dotnetcore31", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("dotnet --version", "3.1"))
        self.assertTrue(self.is_package_present("dotnet"))


@pytest.mark.ruby25
class TestBIRuby25(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("ruby2.5", "Dockerfile-ruby25", "bundler")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("ruby --version", "ruby 2.5."))
        self.assertTrue(self.is_package_present("bundler"))
        self.assertTrue(self.is_package_present("gem"))
        self.assertTrue(self.is_architecture("x86_64"))


class TestBIRuby27(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("ruby2.7", "Dockerfile-ruby27", "bundler", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("ruby --version", "ruby 2.7."))
        self.assertTrue(self.is_package_present("bundler"))
        self.assertTrue(self.is_package_present("gem"))
        self.assertTrue(self.is_architecture("x86_64"))


class TestBIRuby27ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("ruby2.7", "Dockerfile-ruby27", "bundler", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("ruby --version", "ruby 2.7."))
        self.assertTrue(self.is_package_present("bundler"))
        self.assertTrue(self.is_package_present("gem"))
        self.assertTrue(self.is_architecture("aarch64"))


@pytest.mark.go1x
class TestBIGo1(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("go1.x", "Dockerfile-go1x", "mod")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("go version", "go1."))
        self.assertTrue(self.is_package_present("go"))


@pytest.mark.provided
class TestBIProvided(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("provided", "Dockerfile-provided")


class TestBIProvidedAL2(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("provided.al2", "Dockerfile-provided-al2", tag="x86_64")

    def test_architecture(self):
        """
        Test architecture of this build image
        """
        self.assertTrue(self.is_architecture("x86_64"))


class TestBIProvidedAL2ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("provided.al2", "Dockerfile-provided-al2", tag="arm64")

    def test_architecture(self):
        """
        Test architecture of this build image
        """
        self.assertTrue(self.is_architecture("aarch64"))
