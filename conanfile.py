from conans import ConanFile, CMake


class CrowConan(ConanFile):
    name = "crow"
    version = "0.1"
    description = "Fast and easy to use modern C++ micro web framework"
    url = "https://github.com/ipkn/crow"
    license = "MIT; see https://github.com/ipkn/crow/blob/master/LICENSE"
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"

    requires = (("boost/1.71.0@conan/stable"),
                ("OpenSSL/1.0.2s@conan/stable"))

    # No exports necessary

    def source(self):
        # this will create a hello subfolder, take it into account
        self.run("git clone https://github.com/ipkn/crow.git")

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake %s/crow %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)
        self.run("make")

    def package(self):
        self.copy("*.h", dst="include", src="amalgamate")
