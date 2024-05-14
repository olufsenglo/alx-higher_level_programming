#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argVector = sys.argv
    argLen = len(argVector) - 1

    plural = '' if argLen == 1 else 's'
    punc = '.' if argLen == 0 else ':'

    print(f'{argLen} argument{plural}{punc}')
    if argLen:
        for index, param in enumerate(argVector[1:]):
            print(f'{index + 1}: {param}')
