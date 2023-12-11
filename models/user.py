#!/usr/bin/python3

"""
User module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User inherits from BaseModel

    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
