"""!@file mock.py"""

from dataclasses import dataclass
from typing import TextIO


@dataclass
class Mock:
    """!
    Defines the allowed parameters for a mock object.

    @param name String defining the name of the mock
    @param data Defines the set of data types and data structures in the mock
    @param description Description of the mock
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
