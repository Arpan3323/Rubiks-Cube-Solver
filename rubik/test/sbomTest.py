'''
Created on Jan 26, 2023

@author: Arpan
'''
import unittest
import app


class SbomTest(unittest.TestCase):


    def test_sbom_AuthorName(self):
        myName = "azs0239"
        result = app._getAuthor("../../")
        returnedAuthorName = result["author"]
        self.assertEqual(returnedAuthorName, myName)


