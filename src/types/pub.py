"""!@file pub.py"""

from dataclasses import dataclass
from typing import TextIO, Self


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
    def format_data(yml: TextIO) -> Self:
        """!
        Extracts the data from a YAML file and formats it in a data class.

        @param: yml File handle to the publisher YAML file.

        @return
        Data class containing the allowed parameters for publishers.
        """

        # Extract the data
        Publisher.name = yml["name"]
        Publisher.publish = yml["publish"]
        Publisher.desc = yml["desc"]

        return Publisher
