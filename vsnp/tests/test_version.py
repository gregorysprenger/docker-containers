import unittest
import subprocess


class TestVersion(unittest.TestCase):
    def test_vsnp(self):
        command = "vsnp3_step1.py --version"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out, b"vsnp3_step1.py: version 3.09\n")


if __name__ == "__main__":
    unittest.main()
