import os
import unittest
import subprocess


class TestControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        run_positive_controls = "bash /tests/scripts/run_controls.sh"
        process = subprocess.Popen(
            run_positive_controls,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = process.communicate()

    def test_python_output(self):
        with open("pos_test.txt") as f:
            python_output = f.readlines()[0].strip()
        self.assertEqual(python_output, "AGTACACTGGT")

    def test_python_checksum(self):
        with open("pos_test.txt.checksum") as f:
            python_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            python_checksum,
            "866789e903d1a0ea9f5666033e7ec3c6b3227d3d70e786400b1e1bc357f11f57",
        )

    def test_python3_output(self):
        with open("py3_test.txt") as f:
            python3_output = f.readlines()[-1].split(": ")[-1].strip()
        self.assertEqual(python3_output, "command not found")

    def test_python3_output_checksum(self):
        with open("py3_test.txt.checksum") as f:
            python3_output_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            python3_output_checksum,
            "99252d6ba98f31d4db4c4d54a64a052f03961035d0d22039c5ddacd73f4ef187",
        )

    def test_biopython_misprint_output(self):
        with open("misprint_test.txt") as f:
            biopython_misprint_output = f.readlines()[-1].strip()
        self.assertEqual(biopython_misprint_output, "ImportError: No module named bio")

    def test_biopython_misprint_checksum(self):
        with open("misprint_test.txt.checksum") as f:
            biopython_misprint_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            biopython_misprint_checksum,
            "da993c34273dcfc6429b3eba1a8cb12c79bbd7c9660075a2d45839b8fa5ef107",
        )


if __name__ == "__main__":
    unittest.main()
