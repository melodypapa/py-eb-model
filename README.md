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

![](doc/os-xdm-xlsx/os_isr_in_excel.png)

1. OsTasks

![](doc/os-xdm-xlsx/os_task_in_excel.png)

3. OsScheduleTable

![](doc/os-xdm-xlsx/os_schedule_table_in_excel.png)

4. OsCounter

![](doc/os-xdm-xlsx/os_counter_in_excel.png)

## 3.2. rte-task-xls

Extract the Rte Configuration information from rte.xdm and then report all to Excel file.

1. Export the Rte Configuration information to excel file

```bash
rte-xdm-xlsx data/Rte.xdm data/Rte.xlsx
```

2. Export the Runnable Entities information to excel file

```bash
rte-xdm-xlsx -r data/Rte.xdm data/Os.xdm data/Runnable.xlsx
```

## 3.3. PrefSystemImporter

Read the EB preference XDM and generate the ARXML file list into text file or create the AUTOSAR builder project file.

```bash
$ pref-system-importer.exe -h
usage: pref-system-importer [-h] [-v] [--file-list] [--ab-project] [--base-path BASE_PATH] [--TRESOS_OUTPUT_BASE_DIR TRESOS_OUTPUT_BASE_DIR] [--project PROJECT] INPUTS [INPUTS ...] OUTPUT

positional arguments:
  INPUTS                The path of perf_imp_xxx.xdm.
  OUTPUT                The path of output file.

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         print debug information.
  --file-list           generate the file list (Default)
  --ab-project          generate the AUTOSAR builder project
  --base-path BASE_PATH
                        base Path for EB tresos
  --env ENV [ENV ...]   specify the environment variable
  --project PROJECT     specify the project name
```
### 3.3.1. Configuration

**h, help**
> Show the usage information 

**-v, --verbose**
> Print the extra debug information during execution.

**--file-list or --ab-project**
> Generate ARXML file list text file or AUTOSAR builder project.

**--base-path**
> Base path for the EB tresos project. **For example**: c:/EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte
>
> If the base path is specified, all input preference XDM configuration files will be based on this BasePath, which can solve the problem of the input preference configuration file name being too long.

**--project**

> The project name will be generate in the AUTOSAR build project. 
>
> It is meaningless if you choose to generate ARXML file list text file.

**--env**

> Replace the variable definition of ${env_var:xxx} which is defined in the EB preference XDM file.

### 3.3.2. Example

**To generate the ARXML file list:**

* Base path: c:/EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte
* INPUT: 
  * c:/EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte/.prefs/pref_imp_exp_Imp_System.xdm 
* OUTPUT: output.lst

```bash
PrefSystemImporter --base-path c:/EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte .prefs/pref_imp_exp_Imp_System.xdm output.lst 
```

**To generate the AUTOSAR builder project:**

All ARXML files in the .project file will use relative path names, so it is recommended to run PrefSystemImporter in the directory where the .project is located.

* Base Path: c:/EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte
* INPUTs:
  *  c:/EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte/.prefs/pref_imp_exp_Bswm_rte.xdm 
  *  c:/EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte/.prefs/pref_imp_exp_Imp_System.xdm
* OUTPUT
  * c:/EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte/ab_project/.project
* Project Name: SimpleDemoRte

```bash
cd c:/EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte/ab_project
PrefSystemImporter --base-path c:/EB/ACG-8_8_8_WIN32X86/workspace/simple_demo_rte --ab-project --project SimpleDemoRte .prefs/pref_imp_exp_Bswm_rte.xdm .prefs/pref_imp_exp_Imp_System.xdm .project 
```

# 4. Change History

**Version 0.8.0** 

1. Create the basic model for EB xdm. (Issue #1)
2. Support to extract the Os Tasks/Isrs from EB xdm and store them in the excel files. (Issue #1)

**Version 1.0.1**

1. Change the attribute to start with lowercase 
2. *read_ref_value* and *read_optional_ref_value* method returns EcucRefType.
3. Read the OsScheduleTable and export to excel
4. Read the OsCounter and export to excel

**Version 1.0.2**

1. Fix the setOsAlarmCallbackName bug

**Version 1.0.3**

1. Generate the System import file list based on EB preference Xdm.
2. Add the support to read OsTaskAutostart element.
3. Add the support to read OsTaskType element.

**Version 1.1.1**

1. Add the support to append SystemMod/EcuExtract.arxml into list automatically for PrefSystemImporter.

**Version 1.1.2**

1. Read the OsAppAlarmRef/OsAppTaskRef/OsAppScheduleTableRef/OsAppResourceRef/OsAppIsrRef from OsApplication.


