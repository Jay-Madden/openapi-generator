# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import petstore_api
from petstore_api.models.outer_composite import OuterComposite  # noqa: E501
from petstore_api.rest import ApiException

class TestOuterComposite(unittest.TestCase):
    """OuterComposite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OuterComposite
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OuterComposite`
        """
        model = petstore_api.models.outer_composite.OuterComposite()  # noqa: E501
        if include_optional :
            return OuterComposite(
                my_number = 1.337, 
                my_string = '', 
                my_boolean = True
            )
        else :
            return OuterComposite(
        )
        """

    def testOuterComposite(self):
        """Test OuterComposite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
