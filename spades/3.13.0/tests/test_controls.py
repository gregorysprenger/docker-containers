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
            "4e648ed7702a0c3e458e126119a234a298367b433b300a120e56575f6e23b302",
        )

    def test_num_contigs(self):
        with open("data/num_contigs.txt") as f:
            num_contigs = f.readlines()[0]
            self.assertEqual(num_contigs, "2\n")


if __name__ == "__main__":
    unittest.main()
