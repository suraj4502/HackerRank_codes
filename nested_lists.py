if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        
    scores = set([student[1] for student in students])   # set returns all the  unique values
    second_lowest_score = sorted(scores)[1]              # sorted to get second highest scores.

    students_with_second_lowest_score = [student[0] for student in students 
                                            if student[1]== second_lowest_score]
                                        
    for i in sorted(students_with_second_lowest_score):
        print(i)                              
    


    
        