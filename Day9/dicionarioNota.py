student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = 0

for score in student_scores:
    student_grades = student_scores[score]
    if student_grades >= 90 :
        print(f"{score} {student_grades} Outstanding")
    elif student_grades >= 81 :
        print(f"{score} {student_grades} Exceeds Expectations")
    elif student_grades >= 71 :
        print(f"{score} {student_grades} Acceptable")
    else:
        print(f"{score} {student_grades} Fail")    

'''student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for studend in student_scores:
    score = student_scores[studend]
    
    if score >= 90:
        student_grades[studend] = "Outstanding"
        
    elif score >= 81:
        student_grades[studend] = "Exceeds Expectations"
        
    elif score >= 71:
        student_grades[studend] = "Acceptable"
        
    else:
        student_grades[studend] = "Fail"   
print(student_grades)    '''
                
        