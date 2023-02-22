#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city with state id and the name of the city"""
    state_id = ""
    name = ""
