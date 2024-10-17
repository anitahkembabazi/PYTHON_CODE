math_grade = int(input("Enter your math grade  :"))
hist_grade= int(input("Enter your history grade: "))
chem_grade= int(input("Enter your chem grade:  "))
geog_grade= int(input("Enter your geography grade: "))
physics_grade =int(input("Enter your physics grade: "))

grades_user={math_grade, hist_grade, chem_grade, geog_grade,physics_grade}
for grade in grades_user:
    if grade > 50:
        print("Pass")
    else:
        print("Fail")
