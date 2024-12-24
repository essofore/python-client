import sys
import argparse

class ParseKeyValuePairs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        result_dict = {}
        for item in values:
            try:
                key, value = item.split('=', 1)
                result_dict[key] = value
            except ValueError:
                raise argparse.ArgumentError(self, f"Invalid key=value pair: '{item}'")
        setattr(namespace, self.dest, result_dict)
        
# this is to fix broken exit_on_error. see: https://github.com/python/cpython/issues/85427
# https://stackoverflow.com/a/5943381
# https://hg.python.org/cpython/file/v3.5.2/Lib/argparse.py#l2369
# https://hg.python.org/cpython/file/v3.5.2/Lib/argparse.py#l1763
class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise argparse.ArgumentError(None, message)
        