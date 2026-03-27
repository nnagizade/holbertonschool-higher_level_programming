#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        for i in my_list[::-1]:
            print("{:d}".format(i))
