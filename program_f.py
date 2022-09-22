#%% _program F
# human goal: reverse a [user-input] string [and display the result]
# as in: provide:<reversed string>, 'reverse':<string>, display:<string>

# should produce machine requirements:
# - program 'user input' () -> (string)
# - program 'reverse' (string) -> (string)
# - program 'display' (string) -> ()


# requires these existing programs
def user_string_input():
    return input("Input text: ")

def reverse_string(string):
    return string[::-1]

def display_string(string):
    print(string)


def program_f():
    x = user_string_input()
    x = reverse_string(x)
    x = display_string(x)

program_f()