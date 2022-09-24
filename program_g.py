#%% _program F
import sys

# human goal: reverse a string
# assumptions: (reverse) a ([input] string) [and return the result]
# as in: provide:<reversed string>, 'reverse':<string>, display:<string>

# should produce machine requirements:
# - program (string) -> (`reverse` string)

# look up if there exists a program with signature (string) -> (`reverse` string)


# existing programs
# "type[alias_a|alias_b]"


# def _program_0(a: "text") -> "text[reversed|mirrored]":
def _program_0(a: "text") -> "reversed text":
    return a[::-1]


# def _program_1(a: "number", b: "number") -> "total number":
#     return a + b


# def _program_2(a: "text[math_problem]") -> "number[solution]":
#     # TODO: replace eval
#     return eval(a)


def _program_3(a: "text") -> "display none":
    print(a)


# def _program_4(a: "text[user]") -> "image[user]":
#     # TODO: implement
#     return None

def _program_5() -> "user text":
    return input("Input: ")

# build program db
def annotations_to_signature(annotations: dict) -> str:
    args = [f"{v} {k}" for k, v in annotations.items() if k != "return"]
    return f'({",".join(args)}) -> ({annotations.get("return")})'


program_db = {}
for name in [x for x in dir() if x.startswith("_program_")]:
    function = getattr(sys.modules[__name__], name)
    signature = annotations_to_signature(function.__annotations__)

    if signature not in program_db:
        program_db[signature] = []

    program_db[signature].append(name)


# translate human goal to program
def find_programs_for_goal(human_goal):
    words = human_goal.split(" ")
    adjective = words[0]
    subject = words[1]

    # find signature where input is text, and output type contains tag "reverse"
    program_hits = []
    for (signature, program_ids) in program_db.items():
        splat = signature.split(" -> ")
        args = splat[0][1:-1].split(",")
        returns = splat[1][1:-1]

        args_types = [x.split(" ")[0] for x in args]
        arg_hits = [x for x in args_types if subject in x]

        tag_hit = adjective in returns

        if tag_hit and len(arg_hits) > 0:
            program_hits.extend(program_ids)

    return [getattr(sys.modules[__name__], x) for x in program_hits]


def do_x_to_y(x, y):
    human_goal = x
    return find_programs_for_goal(human_goal)[0](y)


# do_x_to_y("reverse text", "hehu")
# do_x_to_y("solve math_problem", "1+1")

# machine goals

# "[action ]([input_alias, input alias ]input_type)[ -> ([return_alias] return_type)]""
# action is a consuming function without return

# a simple program that reverses input text and returns it
machine_goal_a = "(text) -> (reversed text)"

# a program that displays input text
machine_goal_b = "display (text)"

# # a program that takes user text input and displays a generated image
# machine_goal_d = "display (user from_text image)"

# a program that takes user text input and displays it reversed
# machine_goal_c = "display (reversed user text)"
machine_goal_c = "(display reversed user text)"

# produce (reversed user text)
x = _program_5()  # () -> (user text)
xt = "user text"
x = _program_0(x) # (text) -> (reversed text)
xt = "reversed user text"
x = _program_3(x) # (text) -> (display none)
xt = "display reversed user text"


# a program which rotates an image by n (user input) degrees
machine_goal_e = "(rotated) image"


# a program which combines two user-input strings
machine_goal_f = "user text + user text"

# a program which hashes a string with a (user input) seed string
machine_goal_g = "hash user text with user text"

# the 'goal language' doesn't necessarily need to be english
machine_goal_h = "hash(#user text, #user text)"


