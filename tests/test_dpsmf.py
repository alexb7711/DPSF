#!/usr/bin/python

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Standard Lib
import dpsmf
import unittest

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Packages

# ===============================================================================
#


class TestDPSMF(unittest.TestCase):
    # -------------------------------------------------------------------------------
    #
    def test_dir_search(self):
        d = dpsmf.DPSMF("./example", "None", True)
        d.run()
        # self.assertEqual(first(arr, 1), 0)
        return
