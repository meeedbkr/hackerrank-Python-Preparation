import textwrap

def wrap(string, max_width):
    stri = []
    for i in range(0, len(string), max_width):
        # Extract a substring of length max_width
        line = string[i:i+max_width]
        # Append the substring to the list of wrapped lines
        stri.append(line)
    return '\n'.join(stri)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)