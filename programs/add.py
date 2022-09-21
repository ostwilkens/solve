# human description: a program which adds two integers
# logic description: transform <integer X, integer Y> into <integer Z>
# sample recognized solution: "1+2" => "3"

# transform into local data structure
def parse(input):
    if "+" not in input:
        return None

    integers = []
    for part in input.split("+"):
        if not part.isdigit():
            return None
        integers.append(int(part))
    
    return integers


# transform local data structure into solution
def solve(data):
    sum = 0
    for integer in data:
        sum += integer
    return str(sum)