# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from petstore_api.models.basque_pig import BasquePig
from petstore_api.models.danish_pig import DanishPig
from typing import Any, List
from pydantic import StrictStr, Field

ANYOFPIG_ANY_OF_SCHEMAS = ["BasquePig", "DanishPig"]

class AnyOfPig(BaseModel):
    """
    AnyOfPig
    """

    # data type: BasquePig
    anyof_schema_1_validator: Optional[BasquePig] = None
    # data type: DanishPig
    anyof_schema_2_validator: Optional[DanishPig] = None
    actual_instance: Any
    any_of_schemas: List[str] = Field(ANYOFPIG_ANY_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = AnyOfPig.construct()
        error_messages = []
        # validate data type: BasquePig
        if not isinstance(v, BasquePig):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BasquePig`")
        else:
            return v

        # validate data type: DanishPig
        if not isinstance(v, DanishPig):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DanishPig`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in AnyOfPig with anyOf schemas: BasquePig, DanishPig. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> AnyOfPig:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> AnyOfPig:
        """Returns the object represented by the json string"""
        instance = AnyOfPig.construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[BasquePig] = None
        try:
            instance.actual_instance = BasquePig.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[DanishPig] = None
        try:
            instance.actual_instance = DanishPig.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into AnyOfPig with anyOf schemas: BasquePig, DanishPig. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_dict()
        else:
            return json.dumps(self.actual_instance)

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

