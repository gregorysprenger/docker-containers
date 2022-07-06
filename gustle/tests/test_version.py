import unittest
import subprocess


class TestVersion(unittest.TestCase):

    def test_version(self):
        command = "gustle version"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        err, out = process.communicate()
        self.assertEqual(out, b'gustle version 0.2.1\n')  


if __name__ == '__main__':
    unittest.main()