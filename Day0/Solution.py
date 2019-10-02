from __future__ import print_function
import sys

PY_VERSION = sys.version_info.major


# Read a full line of input from stdin and save it to our dynamically
# typed variable, input_string.
if PY_VERSION == 2:
    inputString = raw_input()
else:
    inputString = input()

# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')
print(inputString)
