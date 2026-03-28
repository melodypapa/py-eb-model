# AUTOSAR I-PDU Multiplexer (IpduM) Module Requirements

**Document ID**: SWR_IPDUM
**Version**: 1.0
**Date**: 2026-03-28

## SWR_IPDUM_00001: IpduM Module Parser
**Description**: The system shall provide a parser for AUTOSAR IpduM module XDM files.

**Priority**: High

**Rationale**: IpduM module handles I-PDU multiplexing for efficient bus utilization.

**Acceptance Criteria**:
- IpduMXdmParser class inherits from AbstractEbModelParser
- parse() method validates MODULE-CONFIGURATION = "IpduM"
- Successfully extracts ARVersion and SwVersion from XDM

**Verification**: Unit tests in test_ipdum_xdm_parser.py

## SWR_IPDUM_00002: IpduM General Configuration Parsing
**Description**: The parser shall extract IpduM general configuration parameters.

**Priority**: High

**Rationale**: General settings control IpduM module behavior.

**Acceptance Criteria**:
- Extracts IpduMDynamicSupport (BOOLEAN, optional)
- Extracts IpduMZeroSignalLength (INTEGER)
- Extracts IpduMMaxContainerLength (INTEGER)

**Verification**: Unit test test_read_ipdum_general()

## SWR_IPDUM_00003: IpduM I-PDU Parsing
**Description**: The parser shall extract IpduM I-PDU configuration.

**Priority**: High

**Rationale**: I-PDUs define the multiplexed protocol data units.

**Acceptance Criteria**:
- Parses all IpduMIPdu elements from XDM
- Extracts IpduMIPduId (INTEGER)
- Extracts IpduMIPduName (STRING)
- Extracts IpduMIPduDirection (ENUM: SEND, RECEIVE)
- Extracts IpduMIPduLength (INTEGER)
- Extracts IpduMIPduHandle (INTEGER)
- Extracts IpduMIPduType (ENUM: STATIC, DYNAMIC)
- Handles optional IpduMIPduCycleTime

**Verification**: Unit test test_read_ipdum_ipdus()

## SWR_IPDUM_00004: IpduM Signal Parsing
**Description**: The parser shall extract IpduM signal configuration.

**Priority**: High

**Rationale**: Signals within I-PDUs contain the actual data.

**Acceptance Criteria**:
- Parses all IpduMSignal elements from XDM
- Extracts IpduMSignalId (INTEGER)
- Extracts IpduMSignalName (STRING)
- Extracts IpduMBitPosition (INTEGER)
- Extracts IpduMBitSize (INTEGER)
- Extracts IpduMByteOrder (ENUM: MSB_FIRST, LSB_FIRST)
- Extracts IpduMSignalType (ENUM: UINT8, UINT16, UINT32, SINT8, SINT16, SINT32, BOOLEAN)
- Extracts IpduMSignalInitValue (any type)

**Verification**: Unit test test_read_ipdum_signals()

## SWR_IPDUM_00005: IpduM Trigger Condition Parsing
**Description**: The parser shall extract IpduM trigger condition configuration.

**Priority**: Medium

**Rationale**: Trigger conditions control when dynamic I-PDUs are sent.

**Acceptance Criteria**:
- Parses all IpduMTriggerCondition elements from XDM
- Extracts IpduMTriggerConditionId (INTEGER)
- Extracts IpduMTriggerConditionName (STRING)
- Extracts IpduMTriggerConditionType (ENUM: ON_CHANGE, ON_REQUEST, CYCLIC)
- Handles optional IpduMTriggerConditionRef

**Verification**: Unit test test_read_ipdum_trigger_conditions()

## SWR_IPDUM_00006: IpduM Model Population
**Description**: The parser shall populate the IpduM model object with all parsed data.

**Priority**: High

**Rationale**: Model objects enable downstream processing and Excel export.

**Acceptance Criteria**:
- Creates IpduM model with GeneralConfig, IPdus, Signals, and TriggerConditions
- Each Signal registered with parent IPdu
- Each IPdu registered with parent IpduM module
- All references properly resolved to model objects

**Verification**: Unit test test_ipdum_model_population()