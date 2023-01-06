#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Write your code here
    return len([i for i in s if i.isupper()]) + 1

if __name__ == '__main__':

    s = input()

    result = camelcase(s)

    print(result)
