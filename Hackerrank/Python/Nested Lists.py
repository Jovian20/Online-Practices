if __name__ == '__main__':
    
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        
    students.sort(key= lambda x: (x[1], x[0]))
    
    second_lowest_grade = None
    for student in students:
        if second_lowest_grade is None or student[1] > second_lowest_grade:
            if student[1] != students[0][1]: 
                second_lowest_grade = student[1]
                break
    
    for student in students:
        if student[1] == second_lowest_grade:
            print(student[0])
        
