import unittest
import subprocess
import platform
import Bio
import numpy


class TestVersions(unittest.TestCase):
    def test_python(self):
        python_version = platform.python_version()
        self.assertEqual(python_version, "2.7.18")

    def test_biopython(self):
        biopython_version = Bio.__version__
        self.assertEqual(biopython_version, "1.68")

    def test_numpy(self):
        numpy_version = numpy.__version__
        self.assertEqual(numpy_version, "1.16.6")

    def test_blast(self):
        command = "blastn -version 2>&1| head -n 1 | awk '{print $2}'"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out.strip(), "2.9.0+")


if __name__ == "__main__":
    unittest.main()
