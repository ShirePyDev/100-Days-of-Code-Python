import random

# random_for_Integers = random.randint(1, 10)
# print(random_for_Integers)

# random_rand = random.random() * 10
# print(random_rand)

# random_Uniform = random.uniform(1, 10)
# print(random_Uniform)

# random_head_or_tail = random.randint(0,1)
# if random_head_or_tail == 0:
#     print("Head")
# else:
#     print("Tail")

#test_list = [1, 2, 3, 4]
# random_num = random.choices(test_list)
# print(random_num)


#             RANDOMING THE LIST USING DIFF TYPES OF RANDOMISATION FUNC()
friends = ["Khalid", "Khathar", "Yaxye", "Nasri", "Ayanle"]
random_name = random.choices(friends)

num_index = random.randint(0, 4)
print(friends[num_index])
print(random.choice(friends))
print(random_name)
