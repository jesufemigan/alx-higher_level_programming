#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (None, 0)
    return (len(sentence), sentence[0])
