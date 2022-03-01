from tkinter import E

# hello world
print("hello world")

# type
number = 1
print(type(number))

# operator
print(4 / 3)
print(4 // 3)
print(4 % 3)
print(2 ** 3)

# string expression
print("hello")
print('hell"o')
print("""hell"o""")
print('''hell'o''')

# string multiply
world = "world"
print(world * 100)

# slice
slice = "hello world"
print(slice[0])
print(slice[1])
print(slice[-1])
print(slice[-2])
print(slice[0:5])
print(slice[6:])
print(slice[::2])
print(slice[::-2])

# print input
print("year: %d, month: %d, %s: 24 " % (2022, 2, "date"))
print("hello {name}".format(name="world"))

# string parsing
str = "hello world"
print(str.count("l"))
print(str.find("o"))
print(",".join("abcd").upper())

# list
list = ["a", "b", ["c", "d"]]
list.append("e")
print(list[2])
print(list)

list[2].sort()
list[2].reverse()

# tuple : immutable array
tuple = (1, 2, 'a', 'b')
print(tuple[0])
tuple = tuple * 2
print(tuple)

tuple1, tuple2 = (1, 2)
print(tuple1)
print(tuple2)

tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)

# dictionary : map
dictionary = {'name': 'Henry', 'age': 30}
print(dictionary['name'])
print(dictionary.get('null'))
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
print('phone' in dictionary)

# set
set1 = set([1, 2, 3, 4, 5, 6])
set2 = {4, 5, 6, 7, 8, 9}
print(set1)
print(set1 & set2) # 교집합
print(set1.intersection(set2)) # 교집합
print(set1 | set2) # 합집합
print(set1.union(set2)) # 합집합
print(set1 - set2) # 차집합
print(set1.difference(set2)) # 차집합
set1.add(10)
set1.update([11, 12, 13, 1])
print(set1)

# boolean
trueStr = "hello"
falseStr = ""
if trueStr :
    print("world")
if falseStr :
    print("not printed")

# shellow copy & deep copy
addr1 = [1, 2, 3]
addr2 = addr1 # shellow copy (address)
addr3 = addr1[:] # deep copy (value)
addr1[0] = 4
print(addr1)
print(addr2)
print(addr3)
print(id(addr1)) # 주소값
print(id(addr2)) # 주소값
print(id(addr3)) # 주소값

# if
con1 = True 
if 1 in [1, 2, 3]:
    pass
elif con1:
    print("hello")
else:
    print("world")

con2 = "hello" if con1 == True else "world"

# for
box = [1, 2, 3, 4]
for i in box:
    print(i)

for i in range(1, 5):
    print(i)

# function
def sum(a, b):
    return a + b
    
def print_all(*agrs):
    for param in agrs:
        print(param, end = " ")

print_all("aaa", "bbb", 333, 444,)

def sum_and_mul(a, b):
    return a + b, a * b # tuple

print(sum_and_mul(7,7))

# lambda
add = lambda a, b: a + b

# input
# my_input = input("input data : ")
# print(my_input)

# file i/o : write mode
f = open("hello.txt", 'w', encoding="UTF-8")
for i in range(1, 11):
    data = "%d번 line 입니다.\n" % i
    f.write(data)
f.close()

with open("foo.txt", "w") as f:
    f.write("Hello Python") 

# file i/o : read mode
f = open("hello.txt", 'r', encoding="UTF-8")
while True:
    line = f.readline()
    if not line: break
    print(line, end=",")
f.close()

f = open("hello.txt", 'r', encoding="UTF-8")
lines = f.readlines() # list 형식으로 가져옴
for line in lines:
    print(line.strip("\n"))
f.close()

f = open("hello.txt", 'r', encoding="UTF-8")
data = f.read() # 전체를 한번에 가져옴
print(data)
f.close()
