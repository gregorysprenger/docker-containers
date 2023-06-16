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
        with open("pos_output.txt") as f:
            pos_output = f.readlines()[1].split("\t")
        self.assertEqual(pos_output[2], "99.14")

    def test_pos_output_checksum(self):
        with open("pos_output.txt.checksum") as f:
            pos_output_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            pos_output_checksum,
            "ee4ee484dc8996c311f26e11e66a9b260774d210fcb5aeb6ee789ab881e74f35",
        )

    def test_neg_output(self):
        with open("neg_output.txt.error") as f:
            neg_output = f.readlines()[0].strip()
        self.assertEqual(
            neg_output,
            "ERROR  No reference sketches/genomes or query sketches/genomes found.",
        )

    def test_neg_output_checksum(self):
        with open("neg_output.txt.error.checksum") as f:
            neg_output_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            neg_output_checksum,
            "ac6b1b9906cc770f4429b27db73aa45489ddb1f9733e8cb749235919bc659cc3",
        )


if __name__ == "__main__":
    unittest.main()
