#!/usr/bin/python3
"""A module holding IO utilities,
This files holds from_json_string(my_str):
"""


import json


def from_json_string(my_str):
    """from_json_string - decodes an object
    from json format
    """

    return json.loads(my_str)