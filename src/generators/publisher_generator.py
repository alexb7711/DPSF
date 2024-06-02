"""!@file publisher_generator.py

This module calls the appropriate generators to create the publisher file with
the correct language.
"""

from src.types.publisher import Publisher
from src.generators.python.python_publisher import pygen
from src.generators.rust.rust_publisher import rsgen
from src.generators.c.c_publisher import cgen


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

    if p["lang"] == "python":
        pygen(fp, p)
    elif p["lang"] == "rust":
        rsgen(fp, p)
        pass
    elif p["lang"] == "C++":
        cgen(fp, p)
        pass
    elif p["lang"] == "C":
        cgen(fp, p)
        pass

    return
