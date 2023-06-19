# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import typing
import re  # noqa: F401
import json


from typing import  Any, Dict, Optional
from pydantic import BaseModel, StrictStr

class SecondRef(BaseModel):
    """
    SecondRef
    """
    if typing.TYPE_CHECKING:
        # Mypy does not understand pydantic constrained types, Use the python builtin type when linting is run
        category: Optional[str]
    else:
        category: Optional[StrictStr] = None

    if typing.TYPE_CHECKING:
        # Mypy does not understand pydantic constrained types, Use the python builtin type when linting is run
        circular_ref: Optional[CircularReferenceModel]
    else:
        circular_ref: Optional[CircularReferenceModel] = None

    additional_properties: Dict[str, Any] = {}
    __properties = ["category", "circular_ref"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SecondRef:
        """Create an instance of SecondRef from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict:
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of circular_ref
        if self.circular_ref:
            _dict['circular_ref'] = self.circular_ref.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SecondRef:
        """Create an instance of SecondRef from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SecondRef.parse_obj(obj)

        _obj = SecondRef.parse_obj({
            "category": obj.get("category"),
            "circular_ref": CircularReferenceModel.from_dict(obj.get("circular_ref")) if obj.get("circular_ref") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

