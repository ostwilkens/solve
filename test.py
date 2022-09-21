#%%
import programs.add
import programs.mul
import hashlib
import sys


def hash(data):
    m = hashlib.sha256()

    if type(data) is list:
        for segment in data:
            m.update(segment.encode("utf-8"))
            m.update(b";")
    else:
        m.update(data.encode("utf-8"))

    return m.hexdigest()


# X is what i have, and Y is what i want

# A) X is what i have, and i want exactly Y
# a 'pure' program could also have a lookup table of cached solutions
# B) X is what i have, and i want anything
# C) X is what i have, and i want a result with these characteristics
# D) X is what i have, and i want something that is similar to Z in _this_ way

# solution for A), a global lookup table: "<INPUT_HASH;OUTPUT_HASH>" -> "PROGRAM_ID"
PROGRAM_TABLE = {}
all_programs = [programs.__dict__[x] for x in dir(programs) if not x.startswith("__")]
sample_inputs = ["1+2", "1*2"]
for program in all_programs:
    for input in sample_inputs:
        data = program.parse(input)
        if data is None:
            continue
        output = program.solve(data)
        problem_key = hash([input, output])
        if problem_key not in PROGRAM_TABLE:
            PROGRAM_TABLE[problem_key] = []

        PROGRAM_TABLE[problem_key].append(program.__name__)

def find_programs(input, output):
    problem_key = hash([input, output])
    if problem_key in PROGRAM_TABLE:
        hits = PROGRAM_TABLE[problem_key]
        return hits
    else:
        return None


##%% find a program that does what i want, and solve a few problems with it
# X is what i have, and i want exactly Y

program_id = find_programs("1+2", "3")[0]
program = sys.modules[program_id]
print(program.solve(program.parse("2+2")))
print(program.solve(program.parse("42+42")))
