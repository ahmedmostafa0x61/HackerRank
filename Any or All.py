N=int(input())
l=list(map(int,input().split()))
'''First Check if any of elements is palindromic
    Then check if all of elements are +ve'''
print(any([str(i) ==str(i)[::-1] for i in l]) and all([_ >0 for _ in l ]))
