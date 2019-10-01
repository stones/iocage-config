import argparse

# Construct the argument parser
parser = argparse.ArgumentParser()

# Add the arguments to the parser
parser.add_argument("-f", "--file", required=True, help="first operand")

cliArgs = parser.parse_args()