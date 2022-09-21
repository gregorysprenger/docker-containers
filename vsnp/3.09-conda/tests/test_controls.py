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
            "2b8df3595ebf349e8a9eda992e6fe2ac0ec1a809ace35684ef8c004a8eecab3c",
        )

    def test_vsnp_step2(self):
        with open("data/step2.checksum") as f:
            step2_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            step2_checksum,
            "f1e8f6fa7a9fd74d91c634c5e7543012133cb8458f31cc3e58d4cb2e80115dea",
        )


if __name__ == "__main__":
    unittest.main()
