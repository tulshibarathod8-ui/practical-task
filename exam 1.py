marks = [78,54,76,89,97,99,90,88,77,76,89,67,89,67,78,89,90,90,78,76]

count = len(marks)

print("Total Students:", count)

top_mark = max(marks)
print("Highest Marks:", top_mark)

low_mark = min(marks)
print("Lowest Marks:", low_mark)

average = sum(marks) / count
print("Average Marks:", average)

passed = 0
failed = 0

for mark in marks:
    if mark >= 40:
        passed += 1
    else:
        failed += 1

print("Passed:", passed)
print("Failed:", failed)

percentage = (passed / count) * 100
print("Pass Percentage:", percentage)

marks.sort()
print("Marks in Ascending Order:", marks)

marks.sort(reverse=True)
print("Marks in Descending Order:", marks)

unique_marks = sorted(set(marks))

second_high = unique_marks[-2]
print("Second Highest:", second_high)

second_low = unique_marks[1]
print("Second Lowest:", second_low)

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

for mark in marks:

    if mark >= 90:
        a += 1
    elif mark >= 80:
        b += 1
    elif mark >= 70:
        c += 1
    elif mark >= 60:
        d += 1
    elif mark >= 40:
        e += 1
    else:
        f += 1

all_pass = f == 0
any_fail = f > 0

print("All Students Passed?", all_pass)
print("Any Student Failed?", any_fail)

search_mark = int(input("Enter a mark to search: "))

if search_mark in marks:
    print("Mark", search_mark, "exists in the list.")
else:
    print("Mark", search_mark, "does not exist in the list.")

print("\nGrade Distribution:")

print("Grade A (90+):", a, "Students")
print("Grade B (80-89):", b, "Students")
print("Grade C (70-79):", c, "Students")
print("Grade D (60-69):", d, "Students")
print("Grade E (40-59):", e, "Students")
print("Grade F (Below 40):", f, "Students")    