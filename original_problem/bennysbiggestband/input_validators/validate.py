import sys
import re

try:
    n = sys.stdin.readline()
except EOFError:
    sys.exit(1)

try:
    if n[0] == '0':
        sys.exit(1)

    n = int(n)

    if not 1 <= n <= 1000000:
        sys.exit(1)
except ValueError:
    sys.exit(1)
except IndexError:
    sys.exit(1)

for _ in range(n):
    try:
        line = sys.stdin.readline()
    except EOFError:
        sys.exit(1)

    if not re.match(r"(0|\-?([1-9][0-9]*))\n", line):
        sys.exit(1)
    try:
        x = int(line)

        if not -1000 <= x <= 1000:
            sys.exit(1)
    except ValueError:
        sys.exit(1)

if sys.stdin.readline() != "":
    sys.exit(1)
sys.exit(42)
