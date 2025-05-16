import sys
import re

musicians = set()
instruments = set()

def int_no_leading_zeroes(s) -> int:
    if re.match(r'^0[0-9]+$', s) is None:
        return int(s)
    else:
        sys.exit(1)

try:
    m, i, r = map(int_no_leading_zeroes, sys.stdin.readline().split())
    for _ in range(m):
        line = sys.stdin.readline().split()
        musician = line[0]
        played_instruments = line[1:]
        if len(played_instruments) == 0:
            sys.exit(1)
        musicians.add(musician)
        for instrument in played_instruments:
            instruments.add(instrument)
    for _ in range(i):
        line = sys.stdin.readline().split()
        instrument = line[0]
        instrument_count = int_no_leading_zeroes(line[1])
        instrument_ranges = map(int_no_leading_zeroes, line[2:])
        if instrument not in instruments:
            sys.exit(1)
        for range in instrument_ranges:
            if range < 0 or range >= r:
                sys.exit(1)
except:
    sys.exit(1)

if sys.stdin.readline() != "":
    sys.exit(1)

sys.exit(42)
