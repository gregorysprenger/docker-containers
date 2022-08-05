import unittest
import subprocess
from subprocess import PIPE


class TestControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        command = "bash /tests/scripts/run_controls.sh"
        subprocess.run(command, shell=True, stdout=PIPE)

    def test_bwa(self):
        with open("data/test.sam.checksum") as f:
            bwa_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            bwa_checksum,
            "821f4f4bd08f50035f7f99c3180d1ec8a7ff028d1e743530cc7bd775ca3757b5",
        )

    def test_samtools(self):
        with open("data/paired.bam.checksum") as f:
            samtools_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            samtools_checksum,
            "d3d9c8bc14c3c81b26d5cc0eaec5c8f687c696a269afeb5edacb1982fd2f00f1",
        )

    def test_pilon(self):
        with open("data/pilon.fasta.checksum") as f:
            pilon_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            pilon_checksum,
            "77056766761cd2b117445dd700cf31d1e99e3657110885992bb2ce4e9148404b",
        )


if __name__ == "__main__":
    unittest.main()
