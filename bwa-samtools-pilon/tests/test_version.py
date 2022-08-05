import unittest
import subprocess


class TestVersion(unittest.TestCase):
    def test_bwa(self):
        command = "bwa 2>&1 | head -n 3 | tail -1"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out, b"Version: 0.7.17-r1188\n")

    def test_samtools(self):
        command = "samtools --version | head -n 1"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out, b"samtools 1.9\n")

    def test_pilon(self):
        command = "pilon --version"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out, b"Pilon version 1.23 Mon Nov 26 16:04:05 2018 -0500\n")


if __name__ == "__main__":
    unittest.main()
