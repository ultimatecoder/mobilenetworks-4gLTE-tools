import argparse
import re


IP_EXPRESSION = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"


def ip_type(argument, pattern=re.compile(IP_EXPRESSION)):
    if not pattern.match(argument):
        raise argparse.ArgumentTypeError
    return argument
