import unittest
import subprocess


class TestVersions(unittest.TestCase):
    def test_fastANI(self):
        command = "fastANI --version 2>&1 | awk '{print $2}'"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out.strip(), b"1.33")


if __name__ == "__main__":
    unittest.main()
