# pandas 2.0.1

This image implements:
- [Python 3.11.3](https://www.python.org/)
- [pandas 2.0.1](https://pandas.pydata.org/)
- [OpenPyXL 3.1.2](https://openpyxl.readthedocs.io/en/stable/)
- [xlrd3 1.1.0](https://pythonhosted.org/xlrd3/)
- [odfpy 1.4.1](https://github.com/eea/odfpy)
- [odswriter 0.4.0](https://github.com/mmulqueen/odswriter)
- [xlwt 1.3.0](https://xlwt.readthedocs.io/en/latest/)

and can be accessed at [docker hub](https://hub.docker.com/u/gregorysprenger).

## Example analysis:

This example is from the [pandas.to_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html) documentation.

```
# Create dataframe
df = pd.DataFrame([["a", "b"], ["c", "d"]], index=["row 1", "row 2"], columns=["col 1", "col 2"])

# Save dataframe to XLSX file
df.to_excel("output.xlsx", sheet_name="Sheet1", index=False)

# Read XLSX file
df2 = pd.read_excel("output.xlsx", engine="openpyxl")
```