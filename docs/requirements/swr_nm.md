# AUTOSAR Network Management (Nm) Module Requirements

**Document ID**: SWR_NM
**Version**: 1.0
**Date**: 2026-03-28

## SWR_NM_00001: Nm Module Parser
**Description**: The system shall provide a parser for AUTOSAR Nm module XDM files.

**Priority**: High

**Rationale**: Nm module handles network management for CAN/FlexRay/Ethernet buses.

**Acceptance Criteria**:
- NmXdmParser class inherits from AbstractEbModelParser
- parse() method validates MODULE-CONFIGURATION = "Nm"
- Successfully extracts ARVersion and SwVersion from XDM

**Verification**: Unit tests in test_nm_xdm_parser.py

## SWR_NM_00002: Nm General Configuration Parsing
**Description**: The parser shall extract Nm general configuration parameters.

**Priority**: High

**Rationale**: General settings control Nm module behavior.

**Acceptance Criteria**:
- Extracts NmUserCallout (BOOLEAN, optional)
- Extracts NmSleepMaster (BOOLEAN, optional)
- Extracts NmRemoteSleepInd (BOOLEAN, optional)
- Extracts NmRemoteShutdownInd (BOOLEAN, optional)
- Extracts NmStateChangeTimeout (INTEGER)
- Extracts NmMaxNumberChannels (INTEGER)

**Verification**: Unit test test_read_nm_general()

## SWR_NM_00003: Nm Channel Configuration Parsing
**Description**: The parser shall extract Nm channel configuration.

**Priority**: High

**Rationale**: Channels represent network interfaces.

**Acceptance Criteria**:
- Parses all NmChannel elements from XDM
- Extracts NmChannelId (INTEGER)
- Extracts NmChannelName (STRING)
- Extracts NmBusType (ENUM: CAN, LIN, FLEXRAY, ETHERNET)
- Extracts NmStationIdentifier (INTEGER)
- Extracts NmMessageHandle (INTEGER)
- Extracts NmNodeRef (REFERENCE to NmNode)
- Handles optional NmChannelCycleTime

**Verification**: Unit test test_read_nm_channels()

## SWR_NM_00004: Nm Node Configuration Parsing
**Description**: The parser shall extract Nm node configuration.

**Priority**: High

**Rationale**: Nodes represent network participants.

**Acceptance Criteria**:
- Parses all NmNode elements from XDM
- Extracts NmNodeId (INTEGER)
- Extracts NmNodeName (STRING)
- Extracts NmStationIdentifier (INTEGER)
- Extracts NmNodeType (ENUM: MASTER, SLAVE)
- Handles optional NmNodeActive

**Verification**: Unit test test_read_nm_nodes()

## SWR_NM_00005: Nm Message Configuration Parsing
**Description**: The parser shall extract Nm message configuration.

**Priority**: High

**Rationale**: Messages define the network management protocol.

**Acceptance Criteria**:
- Parses all NmMessage elements from XDM
- Extracts NmMessageId (INTEGER)
- Extracts NmMessageName (STRING)
- Extracts NmMessagePduRef (REFERENCE to I-PDU)
- Extracts NmMessageType (ENUM: ALIVE, RING, LIMP_HOME)

**Verification**: Unit test test_read_nm_messages()

## SWR_NM_00006: Nm Callback Configuration Parsing
**Description**: The parser shall extract Nm callback configuration.

**Priority**: Medium

**Rationale**: Callbacks notify application of network events.

**Acceptance Criteria**:
- Parses all NmCallback elements from XDM
- Extracts NmCallbackName (STRING)
- Extracts NmCallbackType (ENUM: NM_INDICATION, NM_CONFIRMATION, NM_BUS_SLEEP_MODE, NM_NETWORK_MODE)
- Handles optional NmCallbackChannelRef

**Verification**: Unit test test_read_nm_callbacks()

## SWR_NM_00007: Nm Model Population
**Description**: The parser shall populate the Nm model object with all parsed data.

**Priority**: High

**Rationale**: Model objects enable downstream processing and Excel export.

**Acceptance Criteria**:
- Creates Nm model with GeneralConfig, Channels, Nodes, Messages, and Callbacks
- Each Channel registered with parent Nm module
- Each Node registered with parent Nm module
- All references properly resolved to model objects

**Verification**: Unit test test_nm_model_population()