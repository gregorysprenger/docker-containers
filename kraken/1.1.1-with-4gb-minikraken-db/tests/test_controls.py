import os
import unittest
import subprocess


class TestControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        command = "bash /tests/scripts/run_controls.sh"
        subprocess.run(command, shell=True, stdout=subprocess.PIPE)

    def test_kraken_tab(self):
        with open("data/kraken.tab") as f:
            kraken_tab = f.readlines()[0].split("\t")[0]
        self.assertEqual(kraken_tab, " 14.35")

    def test_kraken_tab_checksum(self):
        with open("data/kraken.tab.checksum") as f:
            kraken_tab_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            kraken_tab_checksum,
            "67e311f158ea94ca5625add741e3cd380360fb655957a4c290948501063068cd",
        )

    def test_kraken_missing_fastq_param(self):
        with open("data/kraken_missing_fastq_input_param.txt") as f:
            kraken_missing_fastq_param = f.readlines()[0].split("-")[0]
        self.assertEqual(kraken_missing_fastq_param, "classify: malformed fasta file ")

    def test_minikraken_database(self):
        self.assertEqual(os.path.isfile("/kraken-database/database.idx"), True)
        self.assertEqual(os.path.isfile("/kraken-database/database.kdb"), True)


if __name__ == "__main__":
    unittest.main()
