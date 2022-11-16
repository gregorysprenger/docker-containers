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

    def test_pos_blast_output(self):
        with open("pos_blast.tsv.checksum") as f:
            pos_blast_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            pos_blast_checksum,
            "5c0f155a8190de9252828bd833f24308c9fdd8a3780d0732323a7844f30fcf08",
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

    def test_neg_blast_output(self):
        # Check output file size
        blast_output_filesize = os.path.getsize("neg_blast.tsv")
        self.assertEqual(blast_output_filesize, 0)

        # Check the checksum
        with open("neg_blast.tsv.checksum") as f:
            blast_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            blast_checksum,
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )


if __name__ == "__main__":
    unittest.main()
