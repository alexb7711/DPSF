#!/usr/bin/python

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Standard Lib
import dpsmf
import os
import unittest

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Packages

# ===============================================================================
#


class TestDPSMF(unittest.TestCase):
    # -------------------------------------------------------------------------------
    #
    def get_files():
        d = dpsmf.DPSMF("./example", "None", True)
        d.run()
        return d.get_files()

    # -------------------------------------------------------------------------------
    #
    def test_dir_search(self):
        # Find the files
        f = TestDPSMF.get_files()

        # Count the files
        self.assertEqual(len(f["pub"]), 1)
        self.assertEqual(len(f["sub"]), 1)
        self.assertEqual(len(f["mock"]), 1)

        # Check file names
        pwd = os.path.abspath("./example")

        self.assertEqual(pwd + "/publishers/pub_position.yml", f["pub"][0])
        self.assertEqual(pwd + "/subscribers/sub_position.yml", f["sub"][0])
        self.assertEqual(pwd + "/mock/mock_dc_motor.yml", f["mock"][0])

        return

    # -------------------------------------------------------------------------------
    #
    def test_data_structure_content(self):
        # Find the files
        # f = TestDPSMF.get_files()

        # Integer
        # Float
        # Boolean
        return
