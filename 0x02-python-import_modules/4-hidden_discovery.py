#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    filt_names = [name for name in names if not name.startswith("__")]
    filt_names.sort()
    for name in filt_names:
        print(name)
