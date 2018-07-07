import random

random_list = []
list_length = 20

while len(random_list) < list_length:
  random_list.append(random.randint(0,10))

count_list = [0] * 11
index = 0

while index < len(random_list):
  number = random_list[index]
  count_list[number] = count_list[number] + 1
  index = index + 1

print random_list
print

occurrence_counter = 0
print "Number   |   Occurrence"
while occurrence_counter < len(count_list):
    print "      " + str(occurrence_counter) + "  |   " + "*" * count_list[occurrence_counter]
    occurrence_counter += 1
