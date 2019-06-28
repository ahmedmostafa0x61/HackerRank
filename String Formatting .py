def print_formatted(number):
    width=len(bin(number)[2:])
    for i in range(1,number+1):
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i,width=width-1))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)