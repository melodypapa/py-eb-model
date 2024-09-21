"""Setup file for py-xdm"""

from setuptools import setup, find_packages

setup(
    name='py_eb_model',
    version = '1.0.0',
    license = 'proprietary',
    description="The parser for EB XDM file",

    author = 'melodypapa',
    author_email = "melodypapa@outlook.com",
    url="",

    packages = find_packages(where='src'),
    package_dir= {'': 'src'},

    install_requires=['openpyxl'],

    include_package_data=True,
    
    extras_require={'pytest': 'pytest-cov'},

    entry_points={
        'console_scripts': [
            'os-xdm-xlsx  = py_eb_model.cli.os_xdm_2_xls_cli:main',
        ]
    }
)