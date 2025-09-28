# question 1


# برنامج لحساب التقدير النهائي للطلاب

# 1. نطلب من المستخدم عدد المواد
num_subjects = int(input("Enter number of subjects (at least 3): "))

# 2. نتأكد أن العدد مش أقل من 3
while num_subjects < 3:
    num_subjects = int(input(" You must enter at least 3 subjects, try again: "))

# 3. نجهّز قائمة لتخزين الدرجات
grades = []

# 4. نستخدم حلقة لأخذ درجات المواد
for i in range(num_subjects):
    grade = float(input(f"Enter grade for subject {i+1}: "))
    grades.append(grade)  # نضيف الدرجة للقائمة

# 5. نحسب المعدل العام
average = sum(grades) / num_subjects

# 6. نحدد التقدير بناءً على المعدل
if 85 <= average <= 100:
    status = "excellent"
elif 70 <= average < 85:
    status = "very good"
elif 50 <= average < 70:
    status = "good"
else:
    status = "fail"

# 7. نطبع النتيجة النهائية
print("\n=== Final Result ===")
print(f"Student Average: {average:.2f}")
print(f"Grade: {status}")


#question 2


# برنامج لإدارة مستوى النقاط في لعبة

# 1. نطلب من المستخدم إدخال النقاط الحالية (عدد صحيح)
points = int(input("Enter current points: "))

# 2. نحدد الزيادة بناءً على قيمة النقاط
if points < 50:
    points += 10   # نضيف 10 نقاط
elif 50 <= points <= 80:
    points += 5    # نضيف 5 نقاط
else:
    points += 2    # نضيف 2 نقطة فقط

# 3. نحدد حالة اللاعب بناءً على النقاط الجديدة
if points >= 100:
    status = "Winner "
elif points >= 50:
    status = "On the way to win "
else:
    status = "Loser "

# 4. نطبع النتيجة
print("\n=== Game Result ===")
print(f"New Points: {points}")
print(f"Player Status: {status}")

#question 3



# برنامج لتحليل سلسلة من الأعداد وإعطاء إحصائيات عنها

# 1. نطلب من المستخدم إدخال سلسلة أعداد مفصولة بفواصل
numbers_input = input("Enter a series of numbers separated by commas: ")

# 2. نقسم النص المدخل حسب الفواصل ونحوّل القيم إلى أعداد صحيحة
numbers = [int(num) for num in numbers_input.split(",")]

# 3. نحسب المتوسط الحسابي
average = sum(numbers) / len(numbers)

# 4. نحدد أكبر قيمة وأصغر قيمة
maximum = max(numbers)
minimum = min(numbers)

# 5. نحسب كم عدد الأعداد الزوجية وكم عدد الأعداد الفردية
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# 6. نحدد إذا الأعداد الزوجية أكثر أم الفردية
if even_count > odd_count:
    more_type = "More even numbers"
elif odd_count > even_count:
    more_type = "More odd numbers"
else:
    more_type = "Equal number of even and odd numbers"

# 7. نطبع النتائج
print("\n=== Statistics ===")
print(f"Numbers: {numbers}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
print(f"Even count: {even_count}, Odd count: {odd_count}")
print(f"Result: {more_type}")
