import unittest
import subprocess


class TestControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        command = "bash /tests/scripts/run_controls.sh"
        subprocess.run(command, shell=True, stdout=subprocess.PIPE)

    def test_skesa(self):
        with open("data/pos_contigs.fasta.checksum") as f:
            skesa_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            skesa_checksum,
            "4045e7ca558db7186517cdf35adf97b4fcb6d3b1dabc16c17467fda8fb59bf74",
        )

    def test_sra_run(self):
        with open("data/neg_control.txt") as f:
            sra_run = f.readlines()[0]
        self.assertEqual(sra_run, "unrecognised option '--sra_run'\n")


if __name__ == "__main__":
    unittest.main()
