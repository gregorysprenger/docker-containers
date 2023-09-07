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

    def test_pos_output(self):
        with open("total_bp.txt") as f:
            pos_output = f.readlines()[0].strip()
        self.assertEqual(pos_output, "6300000")

    def test_pos_output_checksum(self):
        with open("total_bp.txt.checksum") as f:
            pos_output_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            pos_output_checksum,
            "d8b1d23ab88425cbea2e3baaef66173b96751ac846a2f11e96b99dad0b2d94e2",
        )

    def test_neg_output(self):
        with open("neg_stderr.log") as f:
            neg_output = f.readlines()[0].strip()
        self.assertEqual(neg_output, "Usage: seqtk mergepe <in1.fq> <in2.fq>")

    def test_neg_output_checksum(self):
        with open("neg_stderr.log.checksum") as f:
            neg_output_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            neg_output_checksum,
            "d773172e6db19694219ecba7946c13acf7920bb2f2b00cf6719a7279d98b6546",
        )


if __name__ == "__main__":
    unittest.main()
