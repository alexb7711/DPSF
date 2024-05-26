"""@package docstring
This file defines the core for the Dynamic Publisher Subscriber Mock Framework.

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
class dpsmf:
    """Dynamic Publisher Subscriber Mock Framework Classy"""

    # --------------------------------------------------------------------------
    #
    def __init__(self, base_d: str = ".", out_d: str = ".", sim: bool = False):
        """Constructor for DPSMF.

        # Input
        - `base_d`: Base path to begin searching (Default: ".")
        - `out_d`: Output directory for the documentation (Default: ".")
        - `sim`: Enables/disables the generation of mock YAML files for
          simulation (Default: False)

        # Output
        - Generates source code for the associated YAML file in the directory
          that the YAML file was found
        - Generates the API documentation
        """

        # Member variables
        self.base_d = os.path.abspath(base_d)
        self.out_d = os.path.abspath(out_d)
        self.sim = sim
        return

    # --------------------------------------------------------------------------
    #
    def run():
        """Executes the DPSMF process.

        # Input
        - NONE

        # Output
        - NONE
        """
        return
