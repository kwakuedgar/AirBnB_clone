#!/usr/bin/python3
""" module for City class """
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel

    Attributes:
       (string) state_id: initialized as empty string
       (string) name: initialized as empty string
    """
    state_id = ""
    name = ""
