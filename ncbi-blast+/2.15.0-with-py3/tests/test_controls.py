import os
import unittest
import subprocess


class TestControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        run_controls = "bash /tests/scripts/run_controls.sh"
        process = subprocess.Popen(
            run_controls,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = process.communicate()

    def test_python3_output(self):
        with open("pos_py3.txt") as f:
            python3_output = f.readlines()[0].strip()
        self.assertEqual(python3_output, "AGTACACTGGT")

    def test_python3_checksum(self):
        with open("pos_py3.txt.checksum") as f:
            python3_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            python3_checksum,
            "866789e903d1a0ea9f5666033e7ec3c6b3227d3d70e786400b1e1bc357f11f57",
        )

    def test_python2_output(self):
        with open("neg_py2.txt") as f:
            python2_output = f.readlines()[-1].split(": ")[-1].strip()
        self.assertEqual(python2_output, "command not found")

    def test_python2_output_checksum(self):
        with open("neg_py2.txt.checksum") as f:
            python2_output_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            python2_output_checksum,
            "9c0ff403c592ed3804cbdf27b3dec77cc04b8a466b216826cc3d5758dbe089b2",
        )

    def test_pos_blast_checksum(self):
        with open("pos_blast.tsv.checksum") as f:
            pos_blast_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            pos_blast_checksum,
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )

    def test_neg_blast_output(self):
        with open("neg_blast_error.txt") as f:
            neg_blast_output = f.readlines()[0].split(":")[0].strip()
        self.assertEqual(neg_blast_output, "BLAST query/options error")

    def test_neg_blast_checksum(self):
        with open("neg_blast_error.txt.checksum") as f:
            neg_blast_checksum = f.readlines()[0].split(" ")[0].strip()
        self.assertEqual(
            neg_blast_checksum,
            "12bb9fbfb6582bd9cdfdef45571583cfc61cb64dbf7ba2c6f4f55f12b8fde0f1",
        )


if __name__ == "__main__":
    unittest.main()
