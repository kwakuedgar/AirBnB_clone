#!/usr/bin/python3
"""Class user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User inherits from BaseModel

    Public Class Attributes:
    (string) email: initalized as empty string
    (string) password: initalized as empty string
    (string) first_name: initalized as empty string
    (string) las_name: initalized as empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
