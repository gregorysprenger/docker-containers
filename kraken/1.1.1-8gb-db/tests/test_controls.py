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
            kraken_tab = f.readlines()[0].split("\t")[0].strip()
        self.assertEqual(kraken_tab, "2.02")

    def test_kraken_tab_checksum(self):
        with open("data/kraken.tab.checksum") as f:
            kraken_tab_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            kraken_tab_checksum,
            "ed2725c3009c13f2bab6df72522f0447f032a5599884b3221b33e6ebc10d8c97",
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
