import os
import unittest
import subprocess


class TestPositiveControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        run_positive_controls = "bash /tests/scripts/run_positive_controls.sh"
        process = subprocess.Popen(
            run_positive_controls,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = process.communicate()

    def test_pos_diamond_output(self):
        with open("pos_diamond.tsv.checksum") as f:
            pos_diamond_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            pos_diamond_checksum,
            "426cac3c58d7666fd13d94011fa15ff852404f6a200a55bf3254d80a7f04fe8a",
        )


class TestNegativeControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        run_negative_controls = "bash /tests/scripts/run_negative_controls.sh"
        process = subprocess.Popen(
            run_negative_controls,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = process.communicate()

    def test_neg_diamond_output(self):
        # Check output file size
        diamond_output_filesize = os.path.getsize("neg_diamond.tsv")
        self.assertEqual(diamond_output_filesize, 0)

        # Check stdout file contents
        with open("neg_diamond_stdout.txt") as f:
            neg_diamond_stdout = f.readlines()[-1]
        self.assertTrue(
            neg_diamond_stdout.startswith(
                "Error: The sequences are expected to be proteins but only contain DNA letters"
            )
        )

        # Check the checksum
        with open("neg_diamond.tsv.checksum") as f:
            diamond_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            diamond_checksum,
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )


if __name__ == "__main__":
    unittest.main()
