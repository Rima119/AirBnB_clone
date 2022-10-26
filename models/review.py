#!/usr/bin/python3
"""Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherit from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
