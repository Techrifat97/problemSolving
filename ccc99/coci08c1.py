#Sequence creation
number_of_question = int(input())
sample_answer = input()
adrian = ['A','B','C']
ad_list = []
count = 0
for index in range(number_of_question):
   ad_list.append(adrian[count])
   count += 1
   if count == 3:
       count = 0

bruno = ['B','A','B','C'] 
br_list = []
count = 0
for index in range(number_of_question):
   br_list.append(bruno[count])
   count += 1
   if count == 4:
       count = 0

Goran = ['C','C','A','A','B','B']
gr_list = []
count = 0
for index in range(number_of_question):
   gr_list.append(Goran[count])
   count += 1
   if count == 6:
       count = 0
loop_count = 0
ad_value = 0
br_value = 0
gr_value = 0
while loop_count <= number_of_question -1:
    if sample_answer[loop_count] == ad_list[loop_count]:
        ad_value += 1
    if sample_answer[loop_count] == br_list[loop_count]:
        br_value += 1
    if sample_answer[loop_count] == gr_list[loop_count]:
        gr_value += 1
    
    loop_count +=1
if gr_value > br_value and gr_value > ad_value:
    print(gr_value)
    print("Goran")
elif br_value > gr_value and br_value > ad_value:
    print(br_value)
    print('Bruno')
elif ad_value > gr_value and ad_value > br_value:
    print(ad_value)
    print('Adrian')
elif ad_value == gr_value == br_value:
    print(ad_value)
    print('Adrian')
    print('Bruno')
    print('Goran')
elif ad_value == gr_value:
    print(ad_value)
    print('Adrian')
    print('Goran')
elif ad_value == br_value:
    print(ad_value)
    print('Adrian')
    print('Bruno')
elif br_value == gr_value:
    print(gr_value)
    print('Bruno')
    print('Goran')