# Fuction that prints yaml.
# !/user/bin/env python

import yaml
import sys
from pprint import pprint


def read_yaml(filename):
    with open(filename) as f:
        return yaml.safe_load(f)


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        filename = input("Enter YAML file name: ")
    pprint(read_yaml(filename))
