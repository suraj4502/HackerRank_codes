N, X = map(int,input().split())

marks = []

for i in range(X):
    marks.append(list(map(float,input().split())))
    
    
for student_marks in zip(*marks):
    avg = sum(student_marks)/X
    print("{:.1f}".format(avg))
