import pytest
from tests.build_image_base_test import BuildImageBase, AL2023BasedBuildImageBase


@pytest.mark.java8_al2x86_64
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


@pytest.mark.java8_al2arm64
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


@pytest.mark.java11x86_64
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


@pytest.mark.java11arm64
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


@pytest.mark.java17x86_64
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


@pytest.mark.java17arm64
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


@pytest.mark.java17x86_64
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


@pytest.mark.java17arm64
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

@pytest.mark.java21x86_64
class TestBIJava21Maven(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java21", "Dockerfile-java21", "maven", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "21.', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.java21arm64
class TestBIJava21ForArmMaven(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java21", "Dockerfile-java21", "maven", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "21.', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("aarch64"))


@pytest.mark.java21x86_64
class TestBIJava21Gradle(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java21", "Dockerfile-java21", "gradle", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "21', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.java21arm64
class TestBIJava21ForArmGradle(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java21", "Dockerfile-java21", "gradle", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "21', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))
        self.assertTrue(self.is_architecture("aarch64"))


@pytest.mark.nodejs16xx86_64
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


@pytest.mark.nodejs16xarm64
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


@pytest.mark.nodejs18xx86_64
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


@pytest.mark.nodejs18xarm64
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

@pytest.mark.nodejs20xx86_64
class TestBINode20(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("nodejs20.x", "Dockerfile-nodejs20x", "npm", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("node --version", "v20."))
        self.assertTrue(self.is_package_present("npm"))
        self.assertTrue(self.is_architecture("x86_64"))


@pytest.mark.nodejs20xarm64
class TestBINode20ForArm(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("nodejs20.x", "Dockerfile-nodejs20x", "npm", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("node --version", "v20."))
        self.assertTrue(self.is_package_present("npm"))
        self.assertTrue(self.is_architecture("aarch64"))


@pytest.mark.python38x86_64
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


@pytest.mark.python38arm64
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


@pytest.mark.python39x86_64
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


@pytest.mark.python310arm64
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


@pytest.mark.python310x86_64
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

@pytest.mark.python311arm64
class TestBIPython311ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.11", "Dockerfile-python311", "pip", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.11."))
        self.assertTrue(self.is_package_present("pip"))


@pytest.mark.python311x86_64
class TestBIPython311(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.11", "Dockerfile-python311", "pip", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.11."))
        self.assertTrue(self.is_package_present("pip"))

@pytest.mark.python312arm64
class TestBIPython312ForArm(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.12", "Dockerfile-python312", "pip", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.12."))
        self.assertTrue(self.is_package_present("pip"))


@pytest.mark.python312x86_64
class TestBIPython312(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.12", "Dockerfile-python312", "pip", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.12."))
        self.assertTrue(self.is_package_present("pip"))


@pytest.mark.python39arm64
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


@pytest.mark.dotnet6x86_64
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


@pytest.mark.dotnet6arm64
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


@pytest.mark.dotnet7x86_64
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


@pytest.mark.dotnet7arm64
class TestBIDotNet7Arm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            "dotnet7", "Dockerfile-dotnet7", tag="arm64", dep_manager="cli-package"
        )

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("dotnet --version", "7"))
        self.assertTrue(self.is_package_present("dotnet"))


@pytest.mark.dotnet8x86_64
class TestBIDotNet8(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            "dotnet8", "Dockerfile-dotnet8", tag="x86_64", dep_manager="cli-package"
        )

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("dotnet --version", "8"))
        self.assertTrue(self.is_package_present("dotnet"))


@pytest.mark.dotnet8arm64
class TestBIDotNet8Arm(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            "dotnet8", "Dockerfile-dotnet8", tag="arm64", dep_manager="cli-package"
        )

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("dotnet --version", "8"))
        self.assertTrue(self.is_package_present("dotnet"))


@pytest.mark.ruby32x86_64
class TestBIRuby32(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("ruby3.2", "Dockerfile-ruby32", "bundler", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("ruby --version", "ruby 3.2."))
        self.assertTrue(self.is_package_present("bundler"))
        self.assertTrue(self.is_package_present("gem"))
        self.assertTrue(self.is_architecture("x86_64"))

@pytest.mark.ruby32arm64
class TestBIRuby32ForArm(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("ruby3.2", "Dockerfile-ruby32", "bundler", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("ruby --version", "ruby 3.2."))
        self.assertTrue(self.is_package_present("bundler"))
        self.assertTrue(self.is_package_present("gem"))
        self.assertTrue(self.is_architecture("aarch64"))


@pytest.mark.ruby33x86_64
class TestBIRuby33(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("ruby3.3", "Dockerfile-ruby33", "bundler", tag="x86_64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("ruby --version", "ruby 3.3."))
        self.assertTrue(self.is_package_present("bundler"))
        self.assertTrue(self.is_package_present("gem"))
        self.assertTrue(self.is_architecture("x86_64"))

@pytest.mark.ruby33arm64
class TestBIRuby33ForArm(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("ruby3.3", "Dockerfile-ruby33", "bundler", tag="arm64")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("ruby --version", "ruby 3.3."))
        self.assertTrue(self.is_package_present("bundler"))
        self.assertTrue(self.is_package_present("gem"))
        self.assertTrue(self.is_architecture("aarch64"))

@pytest.mark.provided_al2x86_64
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

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("go version", "go1."))
        self.assertTrue(self.is_package_present("go"))


@pytest.mark.provided_al2arm64
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

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("go version", "go1."))
        self.assertTrue(self.is_package_present("go"))


@pytest.mark.provided_al2023x86_64
class TestBIProvidedAL2023(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass(
            "provided.al2023", "Dockerfile-provided-al2023", tag="x86_64"
        )

    def test_architecture(self):
        """
        Test architecture of this build image
        """
        self.assertTrue(self.is_architecture("x86_64"))

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("go version", "go1."))
        self.assertTrue(self.is_package_present("go"))


@pytest.mark.provided_al2023arm64
class TestBIProvidedAL2023ForArm(AL2023BasedBuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("provided.al2023", "Dockerfile-provided-al2023", tag="arm64")

    def test_architecture(self):
        """
        Test architecture of this build image
        """
        self.assertTrue(self.is_architecture("aarch64"))

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("go version", "go1."))
        self.assertTrue(self.is_package_present("go"))
