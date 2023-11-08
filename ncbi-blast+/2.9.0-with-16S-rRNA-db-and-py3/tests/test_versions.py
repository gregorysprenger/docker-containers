import unittest
import platform
import subprocess


class TestVersions(unittest.TestCase):
    def test_python(self):
        python_version = platform.python_version()
        self.assertEqual(python_version, "3.8.15")

    def test_blast(self):
        command = "blastn -version | awk 'NR==1 {print $2}'"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out.strip(), b"2.9.0+")


if __name__ == "__main__":
    unittest.main()
