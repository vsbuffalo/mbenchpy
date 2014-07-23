import sys
import os
from timeit import repeat
from operator import itemgetter
from numpy import percentile, mean
import json

DEVNULL = open(os.devnull, 'wb')

def timed_run(name, command, n):
    """
    Run a subprocess n times, and time it.
    """
    cmd = json.dumps(command).replace("'", "\\'") # for quote safety, FIXME
    cmd = """\
retval = subprocess.call('bash -c %s', shell=True, stderr=open(os.devnull, 'wb'), stdout=open(os.devnull, 'wb'))
if retval != 0:
    raise subprocess.CalledProcessError(retval, '%s', None)
""" % (cmd, name)
    results = repeat(stmt=cmd, setup="import subprocess, os", number=n)
    return [r/float(n) for r in results]

def summary(x):
    """
    Numerical summary of data.
    """
    return [min(x), percentile(x, 0.25), percentile(x, 0.5), percentile(x, 0.75), max(x), mean(x)]

def timing_table(times, header=True):
    """
    Pretty print a table of the times.
    """
    rows = list()
    if header:
        rows.append("command min lq median up max mean".split())
    for name, runtimes in times.items():
        rows.append([name] + summary(runtimes))
    return rows

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Benchmark some commands.')
    parser.add_argument('-n', type=int, default=50, help="number of times")

    parser.add_argument('commands', type=str, nargs='+', metavar="N",
                        help='commands to run, in format \'name="command args"\'')
    args = parser.parse_args()

    # extract programs
    key_vals = [tuple(s.partition('=')) for s in args.commands]
    keys = map(itemgetter(0), key_vals)
    if (len(set(keys)) != len(keys)):
        raise argparse.ArgumentTypeError('commands must be in name="command" format, with unique names')
    commands = dict([(k, v) for k, _, v in key_vals]) # ignore '=' in partition tuples

    times = dict([(key, timed_run(key, cmd, args.n)) for key, cmd in commands.items()])
    results = timing_table(times)
    print "\t".join(results.pop(0))
    for row in results:
        name = row.pop(0)
        print name + "\t" + "\t".join(map(lambda x: "%0.5f" % x, row))


