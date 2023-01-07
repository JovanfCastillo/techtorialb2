
first_exam=70
second_exam=90
third_exam=78

#I want to create a string variable where I can display 
#all grades of this student

str="First exam score is {},second exam score is {}, third exam score is {}"

print(str.format(first_exam,second_exam,third_exam))



str="First exam score is {2},second exam score is {1}, third exam score is {0}"
print(str.format(first_exam,second_exam,third_exam))













