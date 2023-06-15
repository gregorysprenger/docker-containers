import unittest
import platform
import subprocess


class TestVersions(unittest.TestCase):
    def test_skani(self):
        command = "skani --version | awk '{print $2}'"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out.strip(), b"0.1.3")

    def test_cargo(self):
        command = "cargo --version | awk '{print $2}'"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out.strip(), b"1.70.0")

    def test_rustc(self):
        command = "rustc --version | awk '{print $2}'"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out.strip(), b"1.70.0")


if __name__ == "__main__":
    unittest.main()
