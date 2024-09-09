marks=[]
for mark in range(10):
    mark = int(input("enter marks :"))
    marks.append(mark)

students = len(marks)

passed = sum(mark >=40 for mark in marks)
failed = sum(mark <40 for mark in marks)

pass_per = (passed/students)*100
fail_per = (failed/students)*100

print("____________________")
print(f"pass percentage:{pass_per:.2f}")
print(f"fail percentage:{fail_per:.2f}")
print("_____________________________")
print("The out of {0} student's,{1} student's is passed,and {2} student's is failed".format(students,passed,failed))
print("___________________________")
