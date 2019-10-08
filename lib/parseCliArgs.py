import argparse

def stringToBoolean(value):
    if isinstance(value, bool):
       return value
    if value.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif value.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

# Construct the argument parser
parser = argparse.ArgumentParser()

# Add the arguments to the parser
parser.add_argument("-f", "--file", required=True, help="The configuration file that you want to run")
parser.add_argument("-p", "--pretend", type=stringToBoolean, nargs='?',const=True, default=True, help="Don't run any commands")

cliArgs = parser.parse_args()