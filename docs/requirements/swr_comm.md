# AUTOSAR Communication Manager (ComM) Module Requirements

**Document ID**: SWR_COMM
**Version**: 1.0
**Date**: 2026-03-28

## SWR_COMM_00001: ComM Module Parser
**Description**: The system shall provide a parser for AUTOSAR ComM module XDM files.

**Priority**: High

**Rationale**: ComM module manages communication states and modes.

**Acceptance Criteria**:
- ComMXdmParser class inherits from AbstractEbModelParser
- parse() method validates MODULE-CONFIGURATION = "ComM"
- Successfully extracts ARVersion and SwVersion from XDM

**Verification**: Unit tests in test_comm_xdm_parser.py

## SWR_COMM_00002: ComM General Configuration Parsing
**Description**: The parser shall extract ComM general configuration parameters.

**Priority**: High

**Rationale**: General settings control ComM module behavior.

**Acceptance Criteria**:
- Extracts ComMUserCallout (BOOLEAN, optional)
- Extracts ComMStateTransitionTimeout (INTEGER)
- Extracts ComMMaxNumberChannels (INTEGER)
- Extracts ComMMaxNumberChannelsRequested (INTEGER)
- Extracts ComMMaxNumberRequests (INTEGER)

**Verification**: Unit test test_read_comm_general()

## SWR_COMM_00003: ComM Channel Configuration Parsing
**Description**: The parser shall extract ComM channel configuration.

**Priority**: High

**Rationale**: Channels represent communication interfaces.

**Acceptance Criteria**:
- Parses all ComMChannel elements from XDM
- Extracts ComMChannelId (INTEGER)
- Extracts ComMChannelName (STRING)
- Extracts ComMChannelType (ENUM: FULL_DUPLEX, SIMPLE)
- Extracts ComMBusType (ENUM: CAN, LIN, FLEXRAY, ETHERNET)
- Extracts ComMComMEcuModeRef (REFERENCE to ComMMode)
- Handles optional ComMChannelCycleTime

**Verification**: Unit test test_read_comm_channels()

## SWR_COMM_00004: ComM Mode Configuration Parsing
**Description**: The parser shall extract ComM mode configuration.

**Priority**: High

**Rationale**: Modes define communication states.

**Acceptance Criteria**:
- Parses all ComMMode elements from XDM
- Extracts ComMModeName (STRING)
- Extracts ComMModeType (ENUM: NO_COMMUNICATION, FULL_COMMUNICATION, SILENT_COMMUNICATION)
- Handles optional ComMModeRef

**Verification**: Unit test test_read_comm_modes()

## SWR_COMM_00005: ComM Request Configuration Parsing
**Description**: The parser shall extract ComM request configuration.

**Priority**: Medium

**Rationale**: Requests control channel activation.

**Acceptance Criteria**:
- Parses all ComMRequest elements from XDM
- Extracts ComMRequestId (INTEGER)
- Extracts ComMRequestName (STRING)
- Extracts ComMRequestChannelRef (REFERENCE to ComMChannel)
- Handles optional ComMRequestType

**Verification**: Unit test test_read_comm_requests()

## SWR_COMM_00006: ComM Model Population
**Description**: The parser shall populate the ComM model object with all parsed data.

**Priority**: High

**Rationale**: Model objects enable downstream processing and Excel export.

**Acceptance Criteria**:
- Creates ComM model with GeneralConfig, Channels, Modes, and Requests
- Each Channel registered with parent ComM module
- Each Mode registered with parent ComM module
- All references properly resolved to model objects

**Verification**: Unit test test_comm_model_population()