from __future__ import print_function
import sys

PY_VERSION = sys.version_info.major

# Read and save an integer, double, and String to your variables.
j = int(raw_input())
e = float(raw_input())

if PY_VERSION == 2:
    t = raw_input()
else:
    t = input()
# Print the sum of both integer variables on a new line.
print(i + j)
# Print the sum of the double variables on a new line.
print(d + e)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + t)
