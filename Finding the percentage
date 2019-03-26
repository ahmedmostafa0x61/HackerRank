if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    x=student_marks[query_name]
    per='{0:.2f}'.format(sum(x)/len(x))
    print(per)
