import unittest
import subprocess


class TestControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        command = "bash /tests/scripts/run_controls.sh"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()

    def test_spades_output(self):
        with open("data/spades_test_output.txt") as f:
            spades_test_output = f.readlines()[0]
        self.assertEqual(spades_test_output, "========= TEST PASSED CORRECTLY.\n")

    def test_contigs_checksum(self):
        with open("data/contigs.fasta.checksum") as f:
            contigs_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            contigs_checksum,
            "d47d87a6838d6c2d5a24d2690357cc3f80746d1756d4b3a0c551df70b58ed295",
        )

    def test_num_contigs(self):
        with open("data/num_contigs.txt") as f:
            num_contigs = f.readlines()[0]
            self.assertEqual(num_contigs, "1\n")

    def test_neg_output_checksum(self):
        with open("data/neg_output.txt.checksum") as f:
            neg_output_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            neg_output_checksum,
            "190a2878a3db0aacaf9f5c5a438e9c2b1a55318f09b890a3cfe59d6cc9b85ba6",
        )

    def test_neg_output(self):
        with open("data/neg_output.txt") as f:
            neg_output = f.readlines()[2]
        self.assertEqual(
            neg_output,
            "== Error ==  you cannot specify --only-error-correction in isolate mode!\n",
        )


if __name__ == "__main__":
    unittest.main()
