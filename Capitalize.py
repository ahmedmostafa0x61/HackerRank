
import os

def solve(s):
    x = 0
    s=s.capitalize()
    for i in s:
        x += 1
        if i.isspace() and x<len(s) and s[x].isalpha():
            s=s[:x]+s[x].upper()+s[x+1:]
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    fptr.write(result + '\n')

    fptr.close()
