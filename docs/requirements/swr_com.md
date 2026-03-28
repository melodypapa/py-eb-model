# AUTOSAR Communication (Com) Module Requirements

**Document ID**: SWR_COM
**Version**: 1.0
**Date**: 2026-03-28

## SWR_COM_00001: Com Module Parser
**Description**: The system shall provide a parser for AUTOSAR Com module XDM files.

**Priority**: High

**Rationale**: Com module is core to AUTOSAR communication layer.

**Acceptance Criteria**:
- ComXdmParser class inherits from AbstractEbModelParser
- parse() method validates MODULE-CONFIGURATION = "Com"
- Successfully extracts ARVersion and SwVersion from XDM

**Verification**: Unit tests in test_com_xdm_parser.py

## SWR_COM_00002: Com General Configuration Parsing
**Description**: The parser shall extract Com general configuration parameters.

**Priority**: High

**Rationale**: General settings control Com module behavior.

**Acceptance Criteria**:
- Extracts ComEnableUserSupport (BOOLEAN)
- Extracts ComUserInitSignal (BOOLEAN)
- Extracts ComUserStatusSupport (BOOLEAN, optional)
- Extracts ComUserTxConfirmation (BOOLEAN, optional)
- Extracts ComUserRxIndication (BOOLEAN, optional)

**Verification**: Unit test test_read_com_general()

## SWR_COM_00003: Com Signal Parsing
**Description**: The parser shall extract Com signal configuration.

**Priority**: High

**Rationale**: Signals are the fundamental data units in AUTOSAR communication.

**Acceptance Criteria**:
- Parses all ComSignal elements from XDM
- Extracts ComSignalId (INTEGER)
- Extracts ComSignalName (STRING)
- Extracts ComBitPosition (INTEGER)
- Extracts ComBitSize (INTEGER)
- Extracts ComByteOrder (ENUM: MSB_FIRST, LSB_FIRST)
- Extracts ComSignalType (ENUM: UINT8, UINT16, UINT32, SINT8, SINT16, SINT32, BOOLEAN)
- Extracts ComSignalInitValue (any type)
- Handles optional ComSignalExtendedDataType

**Verification**: Unit test test_read_com_signals()

## SWR_COM_00004: Com I-PDU Parsing
**Description**: The parser shall extract Com I-PDU configuration.

**Priority**: High

**Rationale**: I-PDUs represent protocol data units exchanged on the bus.

**Acceptance Criteria**:
- Parses all ComIPdu elements from XDM
- Extracts ComIPduId (INTEGER)
- Extracts ComIPduName (STRING)
- Extracts ComIPduDirection (ENUM: SEND, RECEIVE)
- Extracts ComIPduSignalRef (REFERENCE to ComSignal)
- Extracts ComIPduLength (INTEGER)
- Extracts ComIPduHandle (INTEGER)
- Handles optional ComIPduCycleTime
- Handles optional ComIPduTxMode

**Verification**: Unit test test_read_com_ipdus()

## SWR_COM_00005: Com Model Population
**Description**: The parser shall populate the Com model object with all parsed data.

**Priority**: High

**Rationale**: Model objects enable downstream processing and Excel export.

**Acceptance Criteria**:
- Creates Com model with GeneralConfig, Signals, and IPdus
- Each Signal registered with parent IPdu
- Each IPdu registered with parent Com module
- All references properly resolved to model objects

**Verification**: Unit test test_com_model_population()