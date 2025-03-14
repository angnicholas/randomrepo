from typing import Dict
import json

"""
Let S be the naive json schema defined by the following grammar:

S := int | str | float | {M} | [L] 
M := null | (key : S) , M               (without trailing commas, but wtev)
L := S | L, S


After squashing, we collapse all the lists into Optional Types using the
subset relation on schemas.

Rationale is if I have

[ {"id":"int", "name":"str"}, {"id":"int"}] -> collapse

[ {"id": "int", "name":"Optional[str]" }]


"""

from abc import abstractmethod, ABC


class DataType(ABC):
    def __init__(self, required=True):
        self.required = required

    def __json__(self):
        return {"required": self.required}
    
    @abstractmethod
    def __hash__(self):
        return None
    
    @abstractmethod
    def __eq__(self, other):
        return True

    
def primitive(class_object):

    name = class_object.name
    def __eq__(self, other):
        if not isinstance(other, class_object):
            return False
        return self.required == other.required

    def __json__(self):
        return super().__json__() | {"type": name}
    
    def __hash__(self):
        return hash(name)

    setattr(class_object, '__hash__', __hash__)
    setattr(class_object, '__json__', __json__)
    setattr(class_object, '__eq__', __eq__)
    
    return class_object


@primitive
class String(DataType):
    name = 'str'


@primitive
class Int(DataType):
    name = 'int'


@primitive
class Float(DataType):
    name = 'float'
