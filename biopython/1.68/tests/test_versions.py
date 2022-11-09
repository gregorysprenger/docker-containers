import unittest
import platform
import Bio

class TestVersions(unittest.TestCase):
    def test_python(self):
        python_version = platform.python_version()
        self.assertEqual(python_version, "2.7.18")

    def test_biopython(self):
        biopython_version = Bio.__version__
        self.assertEqual(biopython_version, "1.68")

if __name__ == "__main__":
    unittest.main()