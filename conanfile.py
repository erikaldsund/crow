from conans import ConanFile, CMake


class CrowConan(ConanFile):
    name = "crow"
    version = "0.1"
    description = "Fast and easy to use modern C++ micro web framework"
    url = "https://github.com/erikaldsund/crow"
    license = "MIT; see https://github.com/erikaldsund/crow/blob/master/LICENSE"
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"

    requires = (("boost/1.71.0@conan/stable"),
                ("OpenSSL/1.0.2s@conan/stable"))

    # No exports necessary

    def source(self):
        self.run("git clone {}.git".format(self.url))

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="crow")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="amalgamate")
        self.copy("*.h", dst="include", src="crow/include")
        self.copy("*.h", dst="include/crow", src="crow/include/crow")
        self.copy("*.hpp", dst="include/crow", src="crow/include/crow")
