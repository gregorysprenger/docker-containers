import unittest
import subprocess
from subprocess import PIPE


class TestControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        command = "bash /tests/scripts/run_controls.sh"
        subprocess.run(command, shell=True, stdout=PIPE)

    def test_vsnp_step1(self):
        with open("data/step1.checksum") as f:
            step1_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            step1_checksum,
            "f1e8f6fa7a9fd74d91c634c5e7543012133cb8458f31cc3e58d4cb2e80115dea",
        )

    def test_pilon(self):
        with open("data/step2.checksum") as f:
            step2_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            step2_checksum,
            "77ca573c877e5c4bdd46576e621a5788eeb4e30bd1404eac2b4f549f62d04167",
        )


if __name__ == "__main__":
    unittest.main()
