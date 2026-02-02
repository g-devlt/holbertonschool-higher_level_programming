"""Base module for a lookup function.
"""


def lookup(obj):
    """Wrapper for dir(obj)
    """
    return dir(obj)


if __name__ == "__main__":
    print(lookup(Base()))
