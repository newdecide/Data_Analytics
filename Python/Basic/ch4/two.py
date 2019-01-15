kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30 ,90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_scroe = [0,0,0,0,0]
i =0
for subjust in midterm_score:
    for score in subjust:
        print(score)
        student_scroe[i] += score
        i += 1
    print(student_scroe)
    i=0
else:
    a,b,c,d,e = student_scroe
    student_average = [a/3, b/3, c/3, d/3, e/3]
    print(student_average)

