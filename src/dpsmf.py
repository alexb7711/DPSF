"""!
@file dpsmf.py
@package dpsmf
@brief This file defines the core for the Dynamic Publisher Subscriber Mock Framework.

The DPSMF object requires:

- 'base_d': Base path of project to recursively search (Default: pwd)
- 'out_d': Output path for the documentation (Default: pwd)
- 'sim': Flag indicating the project is being built for simulation
  (Default false)

At this point, the program shall execute, recursively searching directories for
appropriately named YAML files. The appropriate boilerplate code shall generate
with the specified language at the location that the file was located.

The allowed languages are: Python, Rust, C/C++.

After all of the files have been generated, a documentation file of the API
generated will be created and placed in the `out_d` directory.
"""

# ==============================================================================
# Imports
import os
import re


# ==============================================================================
#
class DPSMF:
    """!Dynamic Publisher Subscriber Mock Framework Classy"""

    ############################################################################
    # PUBLIC
    ############################################################################

    # --------------------------------------------------------------------------
    #
    def __init__(self, base_d: str = ".", out_d: str = ".", sim: bool = False) -> None:
        """! Constructor for DPSMF.

        @param base_d Base path to begin searching (Default: "."):
        @param out_d Output directory for the documentation (Default: ".")
        @param sim Enables/disables the generation of mock YAML files for
               simulation (Default: False)

        @return
        - Generates source code for the associated YAML file in the directory
          that the YAML file was found
        - Generates the API documentation
        """

        # fmt: off
        ## @var base_d
        # Absolute path to the directory from which DPSMF begins searching
        self.base_d = os.path.abspath(base_d)

        ## @var out_d
        # Absolute path to the directory where the API documentation
        self.out_d = os.path.abspath(out_d)

        ## @var sim
        # Enables/Disables generating API for mock
        self.sim = sim

        ## @var _files
        # List of files publisher, subscriber, and mock YAML files found
        self._files = {"pub": [], "sub": [], "mock": []}
        # fmt: on

        return

    # --------------------------------------------------------------------------
    #
    def run(self) -> None:
        """!Executes the DPSMF process."""

        # Search for YAML files
        self._search_for_yaml()

        # Generate the file's

        # Create documentation

        return

    # --------------------------------------------------------------------------
    #
    def get_files(self) -> dict:
        """!
        Returns a dictonary of the stored YAML file location's

        @return Dictionary of file paths separated by type.
        Example: dict["pub"][0] -> [path]
        """
        return self._files.copy()

    ############################################################################
    # PRIVATE
    ############################################################################

    # --------------------------------------------------------------------------
    #
    def _search_for_yaml(self) -> None:
        """!
        The search for YAML function recursively searches `base_d` for
        appropriately named files and returns the found absolute file paths.

        @return Dictionary of YAML file locations
        """
        # Recursively search `base_d` for
        # - pub_[name].[yml,yaml]
        # - sub_[name].[yml,yaml]
        # - mock_[name][yml.yaml]
        #
        for path, _, f_names in os.walk(self.base_d):
            # For all the files in `f_names`
            for f in f_names:
                if re.match(".*yml$", f) or re.match(".*yaml$", f):
                    # If the file type is a publisher
                    if re.match("^pub.*", f):
                        self._files["pub"].append(path + "/" + f)
                    # If the file type is a publisher
                    elif re.match("^sub.*", f):
                        self._files["sub"].append(path + "/" + f)
                    # If the file type is a mock and `sim` is enabled
                    elif self.sim and re.match("^mock.*", f):
                        self._files["mock"].append(path + "/" + f)

        # Sort the files
        self._files["pub"].sort()
        self._files["sub"].sort()
        self._files["mock"].sort()

        return
