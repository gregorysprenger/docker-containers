import unittest
import platform
import pandas
import openpyxl
import xlrd3
import xlwt
import odf.namespaces


class TestVersions(unittest.TestCase):
    def test_python(self):
        python_version = platform.python_version()
        self.assertEqual(python_version, "3.11.3")

    def test_pandas(self):
        pandas_version = pandas.__version__
        self.assertEqual(pandas_version, "2.0.1")

    def test_openpyxl(self):
        openpyxl_version = openpyxl.__version__
        self.assertEqual(openpyxl_version, "3.1.2")

    def test_xlrd(self):
        xlrd3_version = xlrd3.__version__
        self.assertEqual(xlrd3_version, "1.1.0")

    def test_odf(self):
        odf_version = odf.namespaces.__version__
        self.assertEqual(odf_version, "1.4.1")

    def test_xlwt(self):
        xlwt_version = xlwt.__VERSION__
        self.assertEqual(xlwt_version, "1.3.0")


if __name__ == "__main__":
    unittest.main()
