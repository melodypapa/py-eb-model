# 1. py-eb-model

1. The python parser engine for EB Tresos Xdm file.
2. To support EB Tresos data model with python.

# 2. How to create the distribution and upload to pypi

1. Run `python setup.py bdist_wheel` to generate distribution
2. Run `twine check dist/*` to check the validation of distribution
3. Run `twine upload dist/*` to upload to pypi repository
4. Check the website https://pypi.org/project/armodel/ to find out it works or not

And more details can be found at https://packaging.python.org/  

# 3. CLI 

## 3.1. os-task-xlsx

Extract the Os Task information from os.xdm and then report all to Excel file.

```bash
os-xdm-xlsx data/Os.xdm data/Os.xlsx
```

**Result:**

1. OsIsrs

![](doc/ox-xdm-xlsx/excel_os_isrs.png)

2. OsTasks

![](doc/ox-xdm-xlsx/excel_os_tasks.png)


# 4. Change History

**Version 1.0.0** 

1. Create the basic model for EB xdm. (Issue #1)
2. Support to extract the Os Tasks/Isrs from EB xdm and store them in the excel files. (Issue #1)

