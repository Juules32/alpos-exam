import random
import uuid
import subprocess

M_UPPER = 1000
I_UPPER = 100
R_UPPER = 10

M_LOWER = 1
I_LOWER = 1
R_LOWER = 1

DEST_DIR = "original_problem/bennysbiggestband/data/secret/"
SOLVER_SCRIPT = "original_problem/bennysbiggestband/submissions/accepted/incremental_updating.py"

def generate_secret_input_file(M, I, R, file_in):
    with open(file_in, "w") as f:
        f.write(str(M) + " " + str(I) + " " + str(R) + "\n")

        instruments = [str(uuid.uuid1()) for _ in range(I)]
        musician_names = [str(uuid.uuid1()) for _ in range(M)]
        musician_to_instruments: dict[str, set[str]] = {m: set() for m in musician_names}

        # Ensure every instrument is played by at least one musician
        for instr in instruments:
            chosen_musician = random.choice(musician_names)
            musician_to_instruments[chosen_musician].add(instr)

        # Add a randomly sized subset of instruments played to each musician
        for m in musician_names:
            sample_instr = random.sample(list(instruments), max(1, random.randint(1, I) - random.randint(1, I)))
            musician_to_instruments[m] = musician_to_instruments[m].union(sample_instr)
            f.write(m + " " + " ".join(musician_to_instruments[m]) + "\n")

        # Write out each intrument count and ranges
        for i in instruments:
            num_inst = max(1, random.randint(0, M) - random.randint(0, M // 2))
            num_ranges = max(1, random.randint(1, R) - random.randint(1, R))
            ranges = random.sample(range(0, R), num_ranges)
            ranges = map(str, ranges)
            f.write(i + " " + str(num_inst) + " " + " ".join(ranges) + "\n")

def solve_and_output(file_in, file_ans):
    with open(file_in, "r") as fin, open(file_ans, "w") as fout:
        subprocess.run(
            ["python3", SOLVER_SCRIPT],
            stdin=fin,
            stdout=fout,
            check=True
        )

for i in range(100):
    M = random.randint(M_LOWER, M_UPPER)
    I = random.randint(I_LOWER, I_UPPER)
    R = random.randint(R_LOWER, R_UPPER)
    file_in = DEST_DIR + str(i) + ".in"
    generate_secret_input_file(M, I, R, file_in)

    file_ans = DEST_DIR + str(i) + ".ans"
    solve_and_output(file_in, file_ans)

M = M_UPPER
I = I_UPPER
R = R_UPPER
file_in = DEST_DIR + "max" + ".in"
generate_secret_input_file(M, I, R, file_in)
file_ans = DEST_DIR + "max" + ".ans"
solve_and_output(file_in, file_ans)
