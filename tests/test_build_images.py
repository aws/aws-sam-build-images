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


@pytest.mark.java8_al2
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


@pytest.mark.java8_al2
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


@pytest.mark.java11
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


@pytest.mark.java11
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


@pytest.mark.java17
class TestBIJava17Maven(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java17", "Dockerfile-java17", "maven", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "17.0.', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.java17
class TestBIJava17ForArmMaven(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java17", "Dockerfile-java17", "maven", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "17.0.', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("aarch64"))


@pytest.mark.java17
class TestBIJava17AL2Gradle(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java17", "Dockerfile-java17", "gradle", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "17.0', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.java17
class TestBIJava17AL2ForArmGradle(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java17", "Dockerfile-java17", "gradle", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "17.0', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("aarch64"))


@pytest.mark.nodejs12x
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


@pytest.mark.nodejs12x
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


@pytest.mark.nodejs14x
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


@pytest.mark.nodejs14x
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


@pytest.mark.nodejs16x
class TestBINode16(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("nodejs16.x", "Dockerfile-nodejs16x", "npm", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("node --version", "v16."))
        self.assertTrue(self.is_package_present("npm"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.nodejs16x
class TestBINode16ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("nodejs16.x", "Dockerfile-nodejs16x", "npm", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("node --version", "v16."))
        self.assertTrue(self.is_package_present("npm"))
        self.assertTrue(self.is_architecture("aarch64"))


@pytest.mark.nodejs18x
class TestBINode18(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("nodejs18.x", "Dockerfile-nodejs18x", "npm", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("node --version", "v18."))
        self.assertTrue(self.is_package_present("npm"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.nodejs18x
class TestBINode18ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("nodejs18.x", "Dockerfile-nodejs18x", "npm", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("node --version", "v18."))
        self.assertTrue(self.is_package_present("npm"))
        self.assertTrue(self.is_architecture("aarch64"))


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


@pytest.mark.python38
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


@pytest.mark.python38
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


@pytest.mark.python39
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


@pytest.mark.python310
class TestBIPython310ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.10", "Dockerfile-python310", "pip", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.10."))
        self.assertTrue(self.is_package_present("pip"))


@pytest.mark.python310
class TestBIPython310(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.10", "Dockerfile-python310", "pip", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.10."))
        self.assertTrue(self.is_package_present("pip"))


@pytest.mark.python39
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


@pytest.mark.dotnet6
class TestBIDotNet6(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            "dotnet6", "Dockerfile-dotnet6", tag="x86_64", dep_manager="cli-package"
        )

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("dotnet --version", "6"))
        self.assertTrue(self.is_package_present("dotnet"))


@pytest.mark.dotnet6
class TestBIDotNet6Arm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            "dotnet6", "Dockerfile-dotnet6", tag="arm64", dep_manager="cli-package"
        )

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("dotnet --version", "6"))
        self.assertTrue(self.is_package_present("dotnet"))


@pytest.mark.dotnet7
class TestBIDotNet7(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            "dotnet7", "Dockerfile-dotnet7", tag="x86_64", dep_manager="cli-package"
        )

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("dotnet --version", "7"))
        self.assertTrue(self.is_package_present("dotnet"))


@pytest.mark.ruby27
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


@pytest.mark.ruby27
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


@pytest.mark.provided_al2
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


@pytest.mark.provided_al2
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
