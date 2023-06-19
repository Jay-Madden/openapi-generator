# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg

from typing import Any, Dict



class EnumString2(str, Enum):
    """
    EnumString2
    """

    """
    allowed enum values
    """
    C = 'c'
    D = 'd'

    @classmethod
    def from_json(cls, json_str: str) -> EnumString2:
        """Create an instance of EnumString2 from a JSON string"""
        return EnumString2(json.loads(json_str))


