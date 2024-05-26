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


# ==============================================================================
#
class DPSMF:
    """!Dynamic Publisher Subscriber Mock Framework Classy"""

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

        """!
            @var base_d
            Absolute path to the directory from which DPSMF begins searching
            @var out_d
            Absolute path to the directory where the API documentation
            @var sim
            Enables/Disables generating API for mock
            @var _files
            List of files publisher, subscriber, and mock YAML files found
        """

        self.base_d = os.path.abspath(base_d)
        self.out_d = os.path.abspath(out_d)
        self.sim = sim
        self._files = {"pub": [], "sub": [], "mock": []}

        return

    # --------------------------------------------------------------------------
    #
    def run(self) -> None:
        """!Executes the DPSMF process."""

        # Recursively search `base_d` for
        # - pub_[name].[yml,yaml]
        # - sub_[name].[yml,yaml]
        # - mock_[name][yml.yaml]
        #
        for path, d_names, f_names in os.walk(self.base_d):
            print(path, d_names, f_names)

        return
