if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    
    def avg(li :list):
        return float(sum(li) / len(li))
    for key,value in student_marks.items():
        if key == query_name:
            average = avg(value)
            print("{:.2f}".format(average))
