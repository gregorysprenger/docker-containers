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
        with open("pos_stdout.log") as f:
            pos_output = f.readlines()[9].split(":")[-1].strip()
        self.assertEqual(pos_output, "1309672")

    def test_pos_output_checksum(self):
        with open("pos_stderr.log.checksum") as f:
            pos_output_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            pos_output_checksum,
            "4e7bd5a9303b78b2a5f82d58714d96e2125f01941ec17c2f0bcfe2f68f5fbbe0",
        )

    def test_neg_output_filesize(self):
        neg_output_filesize = os.path.getsize("neg_stdout.log")
        self.assertEqual(neg_output_filesize, 0)

    def test_neg_output(self):
        with open("neg_stderr.log") as f:
            pos_output = f.readlines()[0].split(":")[-1].strip()
        self.assertEqual(pos_output, "k must be from range <1,256>")

    def test_neg_output_checksum(self):
        with open("neg_stderr.log.checksum") as f:
            neg_output_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            neg_output_checksum,
            "5cd7bbaa204d2a4a2e45ec6d4c4b3cfbeed82a11246f03419d4dba57c1733357",
        )


if __name__ == "__main__":
    unittest.main()
