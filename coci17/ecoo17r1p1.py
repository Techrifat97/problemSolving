cost_per_trip = []
percentage_of_students = []
sum_total_student = []
student_list = []

for i in range(10):
    cost_per_trip.append(int(input()))
    input_list = input().split()
    percentage_of_students.append([float(num) for num in input_list])
    sum_total_student.append(int(input()))

def student_calculation(student_proportions, total_student):
    student_list = []
    total_student_value = total_student[0] 
    student_list.append(int(student_proportions[0] * total_student_value))
    student_list.append(int(student_proportions[1] * total_student_value))
    student_list.append(int(student_proportions[2] * total_student_value))
    student_list.append(int(student_proportions[3] * total_student_value))

    if total_student != sum(student_list):
        most_student = max(student_list)
        uncounted = total_student_value - sum(student_list)
        index_of_most_student = student_list.index(most_student)
        student_list[index_of_most_student] += uncounted
        return student_list
    else:
        return student_list

for i in range(10):
     student_list.append(student_calculation(percentage_of_students[i], [sum_total_student[i]]))

def cost_calculate(student_list):
    total_cost = ((student_list[0] * 12) / 2 ) + ((student_list[1] * 10) / 2 ) + ((student_list[2] * 7) / 2 ) + ((student_list[3] * 5) / 2)
    return total_cost


for i in range(10):
    cost = cost_calculate(student_list[i])
    if cost_per_trip[i] > cost:
        print('YES')
    else:
        print('NO')

"""Alternative approach""" 
   
YEAR_COSTS = [12, 10, 7, 5]
for dataset in range(10):
    trip_cost = int(input())
    proportions = input().split()
    num_students = int(input())
    
    for i in range(len(proportions)):
        proportions[i] = float(proportions[i])
    
    students_per_year = []
    for proportion in proportions:
        students = int(num_students * proportion)
        students_per_year.append(students)
    
    counted = sum(students_per_year) 
    uncounted = num_students - counted 
    most = max(students_per_year)
    where = students_per_year.index(most)
    students_per_year[where] = students_per_year[where] + uncounted
    
    total_raised = 0
    
    for i in range(len(students_per_year)):
        total_raised = total_raised + students_per_year[i] * YEAR_COSTS[i]
    if total_raised / 2 < trip_cost:
        print('YES')
    else:
        print('NO')