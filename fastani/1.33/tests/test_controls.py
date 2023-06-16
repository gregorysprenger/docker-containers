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
            pos_output = f.readlines()[0].split("\t")
        self.assertEqual(pos_output[2], "99.1465")

    def test_pos_output_checksum(self):
        with open("pos_output.txt.checksum") as f:
            pos_output_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            pos_output_checksum,
            "05213815b5cf1924f18c5f27033349923f09b3ec293a120795f951679f564d56",
        )

    def test_neg_output_filesize(self):
        neg_output_filesize = os.path.getsize("neg_output.txt")
        self.assertEqual(neg_output_filesize, 0)

    def test_neg_output_checksum(self):
        with open("neg_output.txt.checksum") as f:
            neg_output_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            neg_output_checksum,
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )

    def test_neg_output_errors(self):
        with open("neg_output_errors.txt") as f:
            neg_output_errors = f.readlines()[-1].split("...")[-1]
        self.assertEqual(neg_output_errors.strip(), "Segmentation fault (core dumped)")


if __name__ == "__main__":
    unittest.main()
