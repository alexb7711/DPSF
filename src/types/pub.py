"""!@file pub.py"""

from dataclasses import dataclass
from typing import TextIO


@dataclass
class Publisher:
    """!
    Defines the allowed parameters for a publisher object.

    @param name String defining the name of the publisher
    @param data Defines the set of data types and data structures in the
           publisher
    @param description Description of the publisher
    """

    # ==========================================================================
    # Data
    name: str
    publish: dict
    desc: str

    # ==========================================================================
    # Helper methods
    def format_data(yml: TextIO) -> dict:
        """!
        Extracts the data from a YAML file and formats it in a dictionary.

        @param: yml File handle to the publisher YAML file.

        @return
        Dictionary containing the name, publisher data, and description
        """

        # Extract the data
        Publisher.name = yml["name"]
        Publisher.pub = yml["publish"]
        Publisher.desc = yml["desc"]

        return {
            "name": Publisher.name,
            "publish": Publisher.pub,
            "desc": Publisher.desc,
        }
