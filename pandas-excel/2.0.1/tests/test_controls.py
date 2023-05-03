import unittest
import pandas as pd
import xlrd3
from xlwt import Workbook


class TestControls(unittest.TestCase):
    def test_xlsx(self):
        # Create dataframe and save to XLSX file
        df = pd.DataFrame(
            [["a", "b"], ["c", "d"]],
            index=["row 1", "row 2"],
            columns=["col 1", "col 2"],
        )
        df.to_excel("output.xlsx", sheet_name="Sheet1", index=False)

        # Read XLSX file as dataframe and check length
        df2 = pd.read_excel("output.xlsx")
        self.assertEqual(len(df2), 2)

    def test_xls(self):
        # Create Excel workbook and save as XLS file
        wb = Workbook()
        sheet1 = wb.add_sheet("Sheet 1")
        sheet1.write(0, 0, "col 1")
        sheet1.write(0, 1, "col 2")
        sheet1.write(1, 0, "a")
        sheet1.write(1, 1, "b")
        sheet1.write(2, 0, "c")
        sheet1.write(2, 1, "d")
        wb.save("output.xls")

        # Read XLS file as dataframe and check length
        df2 = pd.read_excel("output.xls")
        self.assertEqual(len(df2), 2)

    def test_ods(self):
        # Create dataframe and save to ODS file
        df = pd.DataFrame(
            [["a", "b"], ["c", "d"]],
            index=["row 1", "row 2"],
            columns=["col 1", "col 2"],
        )
        df.to_excel("output.ods", index=False)

        # Read ODS file as dataframe and check length
        df2 = pd.read_excel("output.ods")
        self.assertEqual(len(df2), 2)


if __name__ == "__main__":
    unittest.main()
