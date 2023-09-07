import unittest
import subprocess


class TestVersions(unittest.TestCase):
    def test_seqtk(self):
        command = "seqtk 2>&1 | grep 'Version' | awk '{print $2}'"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out.strip(), b"1.4-r122")


if __name__ == "__main__":
    unittest.main()
