import unittest
import subprocess


class TestVersion(unittest.TestCase):
    def test_boost(self):
        command = "grep 'BOOST_LIB_VERSION' /usr/include/boost/version.hpp | awk -F ' ' 'NR>1 {print $NF}'"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out, b'"1_72"\n')

    def test_skesa(self):
        command = "skesa --version 2>&1 | grep 'SKESA' | cut -d ' ' -f 2"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out, b"2.4.0\n")
