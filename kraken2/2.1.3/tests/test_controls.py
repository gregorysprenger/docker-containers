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
        self.assertEqual(kraken2_tab, "16.54")

    def test_kraken2_tab_checksum(self):
        with open("data/kraken2.tab.checksum") as f:
            kraken2_tab_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            kraken2_tab_checksum,
            "58091f72b39329fc947103febf824fefb954079e00c78b02a8fb3ebbdd5d8e28",
        )

    def test_missing_database(self):
        with open("data/missing_database.txt") as f:
            missing_database = f.readlines()[0].strip()
        self.assertEqual(
            missing_database,
            "kraken2: Must specify DB with either --db or $KRAKEN2_DEFAULT_DB",
        )


if __name__ == "__main__":
    unittest.main()
