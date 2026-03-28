# AUTOSAR PDU Router (PduR) Module Requirements

**Document ID**: SWR_PDUR
**Version**: 1.0
**Date**: 2026-03-28

## SWR_PDUR_00001: PduR Module Parser
**Description**: The system shall provide a parser for AUTOSAR PduR module XDM files.

**Priority**: High

**Rationale**: PduR module routes PDUs between different AUTOSAR layers.

**Acceptance Criteria**:
- PduRXdmParser class inherits from AbstractEbModelParser
- parse() method validates MODULE-CONFIGURATION = "PduR"
- Successfully extracts ARVersion and SwVersion from XDM

**Verification**: Unit tests in test_pdur_xdm_parser.py

## SWR_PDUR_00002: PduR General Configuration Parsing
**Description**: The parser shall extract PduR general configuration parameters.

**Priority**: High

**Rationale**: General settings control PduR module behavior.

**Acceptance Criteria**:
- Extracts PduRTriggerTransmit (BOOLEAN, optional)
- Extracts PduRTriggerTransmitVersionInfoApi (BOOLEAN, optional)
- Extracts PduRProvideDirectBufferAccess (BOOLEAN, optional)
- Extracts PduRMaximumBufferLength (INTEGER)
- Extracts PduRZeroLengthBufferLength (INTEGER)

**Verification**: Unit test test_read_pdur_general()

## SWR_PDUR_00003: PduR Routing Table Parsing
**Description**: The parser shall extract PduR routing table configuration.

**Priority**: High

**Rationale**: Routing table defines PDU mapping between layers.

**Acceptance Criteria**:
- Parses all PduRRoutingPath elements from XDM
- Extracts PduRRoutingPathId (INTEGER)
- Extracts PduRRoutingPathName (STRING)
- Extracts PduRRoutingPathSourceRef (REFERENCE to source module)
- Extracts PduRRoutingPathTargetRef (REFERENCE to target module)
- Extracts PduRSourcePduRef (REFERENCE to source PDU)
- Extracts PduRDestPduRef (REFERENCE to destination PDU)

**Verification**: Unit test test_read_pdur_routing_table()

## SWR_PDUR_00004: PduR Buffer Configuration Parsing
**Description**: The parser shall extract PduR buffer configuration.

**Priority**: Medium

**Rationale**: Buffers manage PDU data storage and copying.

**Acceptance Criteria**:
- Parses all PduRBuffer elements from XDM
- Extracts PduRBufferName (STRING)
- Extracts PduRBufferSize (INTEGER)
- Extracts PduRBufferType (ENUM: STATIC, DYNAMIC)
- Handles optional PduRBufferPoolRef

**Verification**: Unit test test_read_pdur_buffers()

## SWR_PDUR_00005: PduR Trigger Transmit Parsing
**Description**: The parser shall extract PduR trigger transmit configuration.

**Priority**: Medium

**Rationale**: Trigger transmit enables low-latency communication.

**Acceptance Criteria**:
- Parses all PduRTriggerTransmit elements from XDM
- Extracts PduRTriggerTransmitId (INTEGER)
- Extracts PduRTriggerTransmitName (STRING)
- Extracts PduRTriggerTransmitRef (REFERENCE to source module)

**Verification**: Unit test test_read_pdur_trigger_transmit()

## SWR_PDUR_00006: PduR Model Population
**Description**: The parser shall populate the PduR model object with all parsed data.

**Priority**: High

**Rationale**: Model objects enable downstream processing and Excel export.

**Acceptance Criteria**:
- Creates PduR model with GeneralConfig, RoutingPaths, Buffers, and TriggerTransmits
- Each RoutingPath registered with parent PduR module
- Each Buffer registered with parent PduR module
- All references properly resolved to model objects

**Verification**: Unit test test_pdur_model_population()