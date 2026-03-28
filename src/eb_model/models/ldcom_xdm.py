"""
LdCom XDM Model Module - Represents AUTOSAR LdCom configuration.

Implements:
    - SWR_LDCOM_00001: LdCom module model
"""
import logging
from ..models.abstract import EcucParamConfContainerDef, Module  # noqa F401


class LdCom(Module):
    """
    AUTOSAR LdCom (Local Data Communication) module configuration model.

    Represents the LdCom module configuration extracted from EB Tresos XDM files.

    Implements: SWR_LDCOM_00001 (LdCom Module Model)
    """

    def __init__(self, parent) -> None:
        """Initialize LdCom module with parent container."""
        super().__init__(parent, "LdCom")

        self.logger = logging.getLogger()