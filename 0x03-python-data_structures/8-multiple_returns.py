#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    y = sentence[0]
    if sentence == '':
        return (0, None)
    return (x, y)
