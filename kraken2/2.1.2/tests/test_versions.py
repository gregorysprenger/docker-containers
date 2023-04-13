import unittest
import subprocess


class TestVersion(unittest.TestCase):
    def test_kraken2(self):
        command = "kraken2 --version | head -n 1 | awk '{print $3}'"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out, b"2.1.2\n")


if __name__ == "__main__":
    unittest.main()
