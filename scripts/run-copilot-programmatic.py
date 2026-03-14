#!/usr/bin/env python3
import sys
import json
import subprocess
import argparse
import shlex
import threading

parser = argparse.ArgumentParser()
parser.add_argument('--timeout', type=int, default=30)
parser.add_argument('args', nargs=argparse.REMAINDER)
args = parser.parse_args()

cmd = ['copilot'] + args.args
try:
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    timer = threading.Timer(args.timeout, proc.kill)
    timer.start()
    out, err = proc.communicate()
    if timer.is_alive():
        timer.cancel()
    exit_code = proc.returncode
except Exception as e:
    out = ''
    err = str(e)
    exit_code = 1

print(json.dumps({'exit': exit_code, 'stdout': out, 'stderr': err}))
