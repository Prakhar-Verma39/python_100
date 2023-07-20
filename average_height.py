student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

c = 0
a = 0
for n in student_heights:
    a += n
    c += 1
    
n = a  / c
print(f"Average height is: {n}")