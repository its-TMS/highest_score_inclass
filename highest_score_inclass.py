student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max = 0

for high in student_scores:
    if high > max:
        max = high

print(f"The highest score in the class is: {max}")
