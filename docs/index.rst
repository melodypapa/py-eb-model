.. py-eb-model documentation master file

Welcome to py-eb-model's Documentation
=======================================

py-eb-model is a Python library for parsing and converting EB Tresos XDM configuration files to various formats, including Excel spreadsheets. It provides comprehensive support for AUTOSAR OS modules and other automotive software components.

**Current Version**: 1.3.1  
**Python Requirements**: >= 3.9  
**License**: MIT

.. image:: https://badge.fury.io/py/eb-model.svg
   :target: https://badge.fury.io/py/eb-model
   :alt: PyPI version

.. image:: https://img.shields.io/badge/docs-latest-brightgreen.svg
   :target: https://py-eb-model.readthedocs.io/en/latest/
   :alt: Documentation Status

.. image:: https://img.shields.io/github/actions/workflow/status/melodypapa/py-eb-model/ci.yml?branch=main
   :target: https://github.com/melodypapa/py-eb-model/actions
   :alt: Build Status

.. contents:: Table of Contents
   :depth: 2
   :local:
   :backlinks: none

Overview
--------

py-eb-model provides a complete XDM (EB Tresos Data Model) file parser and Excel reporter, supporting various AUTOSAR modules configured in EB Tresos. It implements data structures, parsers, and reporters for AUTOSAR Basic Software modules.

Key Features
------------

* **XDM Parsing**: Parse EB Tresos XDM configuration files
* **Excel Export**: Convert configuration data to Excel spreadsheets
* **AUTOSAR Support**: Full support for AUTOSAR OS modules
* **CLI Tools**: Command-line interface for easy conversion
* **Extensible**: Plugin architecture for custom modules
* **Well Tested**: Comprehensive test suite with 100% coverage

Supported Modules
-----------------

Core Modules
~~~~~~~~~~~~

* **OS**: Operating System (Tasks, ISRs, Alarms, Counters, etc.)
* **EcuC**: ECU Configuration
* **RTE**: Runtime Environment
* **BSW**: Basic Software Modules
* **Det**: Default Error Tracer
* **EcuM**: ECU State Manager
* **PbcfgM**: Post-Build Configuration Manager

Communication Stacks
~~~~~~~~~~~~~~~~~~~~

* **CAN Stack**: CanIf, CanNm, CanSm, CanTp
* **Ethernet Stack**: EthIf, EthSm, SoAd, SomeIpTp, TcpIp, UdpNm, DoIP
* **LIN Stack**: LinIf, LinSm, LinTp
* **FlexRay Stack**: FrIf, FrNm, FrSm, FrTp, FrArTp
* **J1939 Stack**: J1939Dcm, J1939Nm, J1939Rm, J1939Tp

Memory Stack
~~~~~~~~~~~~

* **NvM**: NVRAM Manager
* **Fee**: Flash EEPROM Emulation
* **Ea**: EEPROM Abstraction
* **MemIf**: Memory Abstraction Interface
* **MemAcc**: Memory Access
* **MemMap**: Memory Mapping

Diagnostic Stack
~~~~~~~~~~~~~~~~

* **DCM**: Diagnostic Communication Manager
* **DEM**: Diagnostic Event Manager
* **DLT**: Diagnostic Log and Trace
* **FIM**: Function Inhibition Manager

Security Stack
~~~~~~~~~~~~~~

* **Crypto**: Crypto Service Manager
* **CryIf**: Crypto Interface
* **CSM**: Crypto Service Manager
* **SecOC**: Secure Onboard Communication

Quick Start
-----------

Installation
~~~~~~~~~~~~

.. code-block:: bash

   pip install eb-model

Basic Usage
~~~~~~~~~~~

Convert OS XDM to Excel:

.. code-block:: bash

   os-xdm-2-xls -i Os.xdm -o os_config.xlsx

Convert CanIf XDM to Excel:

.. code-block:: bash

   canif-xdm-2-xls -i CanIf.xdm -o canif_config.xlsx

Convert NvM XDM to Excel:

.. code-block:: bash

   nvm-xdm-2-xls -i NvM.xdm -o nvm_config.xlsx

Documentation Structure
-----------------------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   getting-started/index
   usage/cli
   requirements/index
   testing/index

.. toctree::
   :maxdepth: 3
   :caption: API Reference

   api/modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
