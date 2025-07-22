"""Setup file for py-xdm"""

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='py_eb_model',
    version='1.2.1',
    license='proprietary',
    description="The parser for EB XDM file",
    long_description=long_description,
    long_description_content_type="text/markdown",

    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='EB Tresos XDM',

    author='melodypapa',
    author_email="melodypapa@outlook.com",
    url="",

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=['openpyxl'],

    include_package_data=True,

    extras_require={'pytest': 'pytest-cov'},

    entry_points={
        'console_scripts': [
            'os-xdm-xlsx            = eb_model.cli.os_xdm_2_xls_cli:main',
            'rte-xdm-xlsx           = eb_model.cli.rte_xdm_2_xls_cli:main',
            'nvm-xdm-xlsx           = eb_model.cli.nvm_xdm_2_xls_cli:main',
            'ecuc-xdm-xlsx          = eb_model.cli.ecuc_xdm_2_xls_cli:main',
            'PrefSystemImporter     = eb_model.cli.pref_system_importer_cli:main',
        ]
    }
)
