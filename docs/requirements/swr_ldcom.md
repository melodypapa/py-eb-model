# AUTOSAR Limited Communication (LdCom) Module Requirements

**Document ID**: SWR_LDCOM
**Version**: 1.0
**Date**: 2026-03-28

## SWR_LDCOM_00001: LdCom Module Parser
**Description**: The system shall provide a parser for AUTOSAR LdCom module XDM files.

**Priority**: High

**Rationale**: LdCom module provides lightweight communication for resource-constrained systems.

**Acceptance Criteria**:
- LdComXdmParser class inherits from AbstractEbModelParser
- parse() method validates MODULE-CONFIGURATION = "LdCom"
- Successfully extracts ARVersion and SwVersion from XDM

**Verification**: Unit tests in test_ldcom_xdm_parser.py

## SWR_LDCOM_00002: LdCom General Configuration Parsing
**Description**: The parser shall extract LdCom general configuration parameters.

**Priority**: High

**Rationale**: General settings control LdCom module behavior.

**Acceptance Criteria**:
- Extracts LdComEnableUserSupport (BOOLEAN)
- Extracts LdComUserInitSignal (BOOLEAN)
- Extracts LdComUserStatusSupport (BOOLEAN, optional)
- Extracts LdComUserTxConfirmation (BOOLEAN, optional)
- Extracts LdComUserRxIndication (BOOLEAN, optional)

**Verification**: Unit test test_read_ldcom_general()

## SWR_LDCOM_00003: LdCom Signal Parsing
**Description**: The parser shall extract LdCom signal configuration.

**Priority**: High

**Rationale**: LdCom signals are simplified versions of Com signals.

**Acceptance Criteria**:
- Parses all LdComSignal elements from XDM
- Extracts LdComSignalId (INTEGER)
- Extracts LdComSignalName (STRING)
- Extracts LdComBitPosition (INTEGER)
- Extracts LdComBitSize (INTEGER)
- Extracts LdComByteOrder (ENUM: MSB_FIRST, LSB_FIRST)
- Extracts LdComSignalType (ENUM: UINT8, UINT16, UINT32, SINT8, SINT16, SINT32, BOOLEAN)
- Extracts LdComSignalInitValue (any type)
- Handles optional LdComSignalExtendedDataType

**Verification**: Unit test test_read_ldcom_signals()

## SWR_LDCOM_00004: LdCom I-PDU Parsing
**Description**: The parser shall extract LdCom I-PDU configuration.

**Priority**: High

**Rationale**: I-PDUs represent protocol data units exchanged on the bus.

**Acceptance Criteria**:
- Parses all LdComIPdu elements from XDM
- Extracts LdComIPduId (INTEGER)
- Extracts LdComIPduName (STRING)
- Extracts LdComIPduDirection (ENUM: SEND, RECEIVE)
- Extracts LdComIPduSignalRef (REFERENCE to LdComSignal)
- Extracts LdComIPduLength (INTEGER)
- Extracts LdComIPduHandle (INTEGER)
- Handles optional LdComIPduCycleTime
- Handles optional LdComIPduTxMode

**Verification**: Unit test test_read_ldcom_ipdus()

## SWR_LDCOM_00005: LdCom Model Population
**Description**: The parser shall populate the LdCom model object with all parsed data.

**Priority**: High

**Rationale**: Model objects enable downstream processing and Excel export.

**Acceptance Criteria**:
- Creates LdCom model with GeneralConfig, Signals, and IPdus
- Each Signal registered with parent IPdu
- Each IPdu registered with parent LdCom module
- All references properly resolved to model objects

**Verification**: Unit test test_ldcom_model_population()