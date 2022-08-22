#!/usr/bin/env python3
"""
8. List all documents in Python
"""


def list_all(mongo_collection):
    """
    Write a Python function that lists all documents in a collection:
    """
    return [collect for collect in mongo_collection.find()]
