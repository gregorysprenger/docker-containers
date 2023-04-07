import unittest
import subprocess


class TestVersion(unittest.TestCase):
    def test_spades(self):
        command = "spades.py --version 2>&1 | awk '{print $4}'"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out, "v3.15.3\n")

    def test_python(self):
        command = "python --version 2>&1 | awk '{print $2}'"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out, "2.7.18\n")

if __name__ == "__main__":
    unittest.main()