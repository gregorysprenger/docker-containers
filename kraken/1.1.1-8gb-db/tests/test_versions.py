import unittest
import subprocess


class TestVersion(unittest.TestCase):
    def test_jellyfish(self):
        command = "jellyfish --version | awk '{print $2}'"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out, b"1.1.12\n")

    def test_kraken(self):
        command = "kraken --version | head -n 1 | awk '{print $3}'"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out, b"1.1.1\n")

    def test_kraken_databse(self):
        command = "grep 'minikraken' /kraken-database/MiniKraken.README | head -n 1 | awk '{print $3}'"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out, b"minikraken_20171013\n")


if __name__ == "__main__":
    unittest.main()
