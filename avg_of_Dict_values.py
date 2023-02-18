if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # this return the values where the student name is query_name which is a list.
    avg = sum(student_marks[query_name])/ len(student_marks[query_name])
    
    print("{:.2f}".format(avg))s
