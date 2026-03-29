"""
FlexRay bus family model classes.

Implements: SWR_FR_00001 (FlexRay stack model organization)
"""

from eb_model.models.fr_stack.frif_xdm import FrIfGeneral, FrIfCluster, FrIfController, FrIf
from eb_model.models.fr_stack.frnm_xdm import FrNmGeneral, FrNmChannelIdentifiers, FrNmRxPdu, FrNmTxPdu, FrNmChannel, FrNm
from eb_model.models.fr_stack.frsm_xdm import FrSMGeneral, FrSMClusterDemEventParameterRefs, FrSMCluster, FrSM
from eb_model.models.fr_stack.frtp_xdm import FrTpGeneral, FrTpConnectionLimitConfig, FrTpConnectionControl, FrTpRxSdu, FrTpTxSdu, FrTpConnection, FrTp
from eb_model.models.fr_stack.frartp_xdm import FrArTpGeneral, FrArTpRxSdu, FrArTpTxSdu, FrArTpPdu, FrArTpConnection, FrArTpChannel, FrArTp
