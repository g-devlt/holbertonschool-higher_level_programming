#!/usr/bin/python3
def multiple_returns(sentence):
    if not (sentence is str):
        return 0, None
    if len(sentence) == 0:
        return None
    return len(sentence), sentence[0]
