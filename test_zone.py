import random

Easy_math = []
Easy_ans = []
Mid_math = []
Ex_math = []
Devil_math = []
def Easy_gen():
    for _ in range(10):
        first_num = random.randint(1,100)
        sec_num = random.randint(1,100)
        Easy_math.append = "What is the answer of " + str(first_num) + "+" + str(sec_num) + "?"
        Easy_ans.append= str(first_num + sec_num)
    # for _ in range(10):
    #     first_num = random.randint(1,100)
    #     sec_num = random.randint(1,100)
    #     Easy_math.append = "What is the answer of " + {first_num} + "-" + {sec_num} + "?"
    #     Easy_ans.append= str(first_num - sec_num)
        
print(Easy_math)
print(Easy_ans)

Easy_gen()