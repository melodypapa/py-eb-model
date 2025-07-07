import logging
from .abstract import Module


class BswM(Module):
    def __init__(self, parent) -> None:
        super().__init__(parent, "BswM")

        self.logger = logging.getLogger()