#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        return(0, None)
    len_first = (len(sentence), sentence[0])
    return(len_first)

print(multiple_returns(''))
