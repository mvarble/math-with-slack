#!/usr/bin/env python
import sys 
import subprocess
import os

dir = os.path.abspath(os.path.curdir)

with open(os.path.join(dir, "config.json"), mode='r') as handle:
    subprocess.run([
        sys.executable, 
        os.path.join(
            os.path.abspath(os.path.curdir), 
            "math-with-slack", 
            "math-with-slack.py",
        ),
        "--mathjax-tex-options",
        handle.read()
    ])
