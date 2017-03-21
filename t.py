import sys
import argparse
import os
import os.path
from sets import Set
import setools
import setools.policyrep

parser = argparse.ArgumentParser(
    description="Pass filename")
parser.add_argument("policy", help="Specify policy file name")
# Set the verbosity level
parser.add_argument(u"-v", u"--verbose", action=u"store_true",
                    help=u"Be verbose [Default: False]")
args = parser.parse_args()
policy = setools.policyrep.SELinuxPolicy(args.policy)
