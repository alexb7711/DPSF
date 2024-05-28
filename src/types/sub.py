"""!@file sub.py"""

from dataclasses import dataclass
from typing import TextIO


@dataclass
class Subscriber:
    """!
    Defines the allowed parameters for a subscriber object.

    @param name String defining the name of the subscriber
    @param data Defines the set of data types and data structures in the
           subscriber
    @param description Description of the subscriber
    """

    # ==========================================================================
    # Data
    name: str
    data: dict
    desc: str

    # ==========================================================================
    # Helper methods
    def format_data(yml: TextIO) -> dict:
        return {}
