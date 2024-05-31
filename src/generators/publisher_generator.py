"""!@file publisher_generator.py

This module calls the appropriate generators to create the publisher file with
the correct language.
"""

from src.types.publisher import Publisher


# ==============================================================================
#
def generate(fp: list[str], p: list[Publisher]):
    """!
    Call the correct generation module to create each of the provided publisher
    YAML files in their respective locations.

    @param fp List of file paths to each of the publisher YAML files
    @param p List of dictionaries containing the publisher data

    @return
    None
    """
    return
