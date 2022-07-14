import unittest
import subprocess
from subprocess import PIPE


class TestControls(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        command = "bash /tests/scripts/run_controls.sh"
        subprocess.run(command, shell=True, stdout=PIPE)

    def test_index(self):
        with open("data/test.cgst.checksum") as f:
            cgst_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(cgst_checksum, "f7c03c7ec44ce1dca23dadc01f7d41a42da90940f34d4241ad86f0cd5f19fc55")
        
    def test_summary(self):
        with open("data/test_summary.tsv.checksum") as f:
            summary_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(summary_checksum, "e6be9f3feff1230f7e4896cb3c8fc21186add20a8868fdf91b2ca04942d801f3")
        

if __name__ == '__main__':
    unittest.main()
