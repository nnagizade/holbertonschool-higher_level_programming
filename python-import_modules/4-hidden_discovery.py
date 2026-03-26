#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for i in sorted(dir(hidden_4)):
        if i[:2] != "__":
            print("{}".format(i))
