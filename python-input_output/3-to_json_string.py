#!/usr/bin/python3
"""A module holding IO utilities,
This files holds to_json_string(my_obj)
"""

import json


def to_json_string(my_obj):
    """ to_json_string - Converts
    an object to its json reprensentation
    """

    return json.dumps(my_obj)