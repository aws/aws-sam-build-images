from tests.build_image_base_test import BuildImageBase


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


class TestBIJava8AL2(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java8.al2", "Dockerfile-java8-al2", "gradle")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "1.8', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))


class TestBIJava11(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("java11", "Dockerfile-java11", "maven")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(
            self.check_package_output("java -version", 'openjdk version "11.0.', True)
        )
        self.assertTrue(self.is_package_present("mvn"))
        self.assertTrue(self.is_package_present("gradle"))


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


class TestBINode12(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("nodejs12.x", "Dockerfile-nodejs12x", "npm")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("node --version", "v12."))
        self.assertTrue(self.is_package_present("npm"))


class TestBINode14(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("nodejs14.x", "Dockerfile-nodejs14x", "npm")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("node --version", "v14."))
        self.assertTrue(self.is_package_present("npm"))


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


class TestBIPython38(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.8", "Dockerfile-python38", "pip")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.8."))
        self.assertTrue(self.is_package_present("pip"))

class TestBIPython39(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("python3.9", "Dockerfile-python39", "pip")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("python --version", "Python 3.9."))
        self.assertTrue(self.is_package_present("pip"))




class TestBIDotNetCore31(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("dotnetcore3.1", "Dockerfile-dotnetcore31")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("dotnet --version", "3.1"))
        self.assertTrue(self.is_package_present("dotnet"))

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


class TestBIRuby27(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("ruby2.7", "Dockerfile-ruby27", "bundler")

    def test_packages(self):
        """
        Test packages specific to this build image
        """
        self.assertTrue(self.check_package_output("ruby --version", "ruby 2.7."))
        self.assertTrue(self.is_package_present("bundler"))
        self.assertTrue(self.is_package_present("gem"))


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


class TestBIProvided(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("provided", "Dockerfile-provided")


class TestBIProvidedAL2(BuildImageBase):
    __test__ = True

    @classmethod
    def setUpClass(cls):
        super().setUpClass("provided.al2", "Dockerfile-provided-al2")
