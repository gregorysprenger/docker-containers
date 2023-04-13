import os
import unittest
import subprocess


class TestControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        command = "bash /tests/scripts/run_controls.sh"
        subprocess.run(command, shell=True, stdout=subprocess.PIPE)

    def test_kraken2_tab(self):
        with open("data/kraken2.tab") as f:
            kraken2_tab = f.readlines()[0].split("\t")[0].strip()
        self.assertEqual(kraken2_tab, "15.27")

    def test_kraken2_tab_checksum(self):
        with open("data/kraken2.tab.checksum") as f:
            kraken2_tab_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            kraken2_tab_checksum,
            "40a91648758fb4cbc0f5f5c9845032d12a62055bd4bbf183088caf5fdc488529",
        )

    def test_missing_database(self):
        with open("data/missing_database.txt") as f:
            missing_database = f.readlines()[0].strip()
        self.assertEqual(
            missing_database,
            "kraken2: Must specify DB with either --db or $KRAKEN2_DEFAULT_DB",
        )

    def test_minikraken_database(self):
        self.assertEqual(os.path.isfile("/kraken2-database/hash.k2d"), True)
        self.assertEqual(os.path.isfile("/kraken2-database/opts.k2d"), True)
        self.assertEqual(os.path.isfile("/kraken2-database/taxo.k2d"), True)


if __name__ == "__main__":
    unittest.main()
