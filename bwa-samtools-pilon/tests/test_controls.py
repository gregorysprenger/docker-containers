import unittest
import subprocess
from subprocess import PIPE


class TestControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        command = "bash /tests/scripts/run_controls.sh"
        subprocess.run(command, shell=True, stdout=PIPE)

    def test_bwa(self):
        with open("test.sam.checksum") as f:
            bwa_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            bwa_checksum,
            "cdfb47712f8a4e79da7969518fcde1ed7469d9d495072f7286cc9271b48ab769",
        )

    def test_samtools(self):
        with open("paired.bam.checksum") as f:
            samtools_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            samtools_checksum,
            "20e892e75472b5f2a8a2bd8e5b03c8227300bbf356601012b72f839ed13fe86e",
        )

    def test_pilon(self):
        with open("pilon.fasta.checksum") as f:
            pilon_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            pilon_checksum,
            "77056766761cd2b117445dd700cf31d1e99e3657110885992bb2ce4e9148404b",
        )


if __name__ == "__main__":
    unittest.main()
