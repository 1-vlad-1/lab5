def get_vowels(String):
    return [each for each in String if each in "aeiou"]#fiveth commit to master
get_vowels("animal") # [a, i, a]
get_vowels("bell") # [e] Third commit to master
get_vowels("football") # [o, o, a]

def capitalize(String):#sixth commit to master
    return String.title()
capitalize("shop") # [Shop]
capitalize("python programming") # [Python Programming]
capitalize("how are you!") # [How Are You!]
capitalize("hello world")# fourth commit to master

def merge(dic1,dic2):
    dic3=dic1.copy()
    dic3.update(dic2)
    return dic3
dic1={1:"hello", 2:"world"}
dic2={3:"Python", 4:"Programming"}
merge(dic1,dic2) # {1: 'hello', 2: 'world', 3: 'Python', 4: 'Programming'}

import time
start_time= time.time()
def fun():
    a=2
    b=3
    c=a+b
end_time= time.time()
fun()
timetaken = end_time - start_time
print("Your program takes: ", timetaken) # 0.0345

def check_duplicate(lst):
    return len(lst) != len(set(lst))
check_duplicate([1,2,3,4,5,4,6]) # True
check_duplicate([1,2,3,4,5]) # False
#First commit to master
check_duplicate([1,2,3,4,9]) # False