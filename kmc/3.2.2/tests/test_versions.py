import unittest
import subprocess


class TestVersions(unittest.TestCase):
    def test_kmc(self):
        command = "kmc --help | head -n 1 | awk -F ' ' '{print $5}'"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out.strip(), b"3.2.2")


if __name__ == "__main__":
    unittest.main()
