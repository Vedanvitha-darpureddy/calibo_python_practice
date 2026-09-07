#basic print statements
student_name=input("enter your name:") 
student_no=int(input("enter your student number:"))
maths=int(input("enter your maths marks:"))
science=int(input("enter your science marks:"))
english=int(input("enter your english marks:"))
total_marks=maths+science+english
average_marks=total_marks/3
print("student name:",student_name)
print("student number:",student_no)
print("total marks:",total_marks)
print("average marks:",average_marks)
#if statements
if average_marks>=90:
    print("grade:A")
elif average_marks>=80:
    print("grade:B")    
elif average_marks>=70:
    print("grade:C")
elif average_marks>=60:
    print("grade:D")
else :
    print("grade:F")   

