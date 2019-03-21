import random

l1 = ["春", "夏"]
l2 = ["秋", "冬"]

l3 = l1 + l2
print("l3 = " + str(l3))
print(random.choice(l3)) # l3からランダムに要素を取り出す
print("l3.index(秋) = " + str(l3.index("秋")))

print("春 in l3 = ", end="")
if "春" in l3:
    print("true")
else :
    print("false")

print("春 not in l1 = ", end="")
if "春" not in l1:
    print("true")
else :
    print("false")

t = (77, 7)
l4 = l1 + list(t) # tはタプルのため l1+t にするとTypeError
print(l4)

l5 = l1 * 4
print(l5)

# 要素が１つのリスト
single_l = ["abc"]

# 要素が１つのタプル
t1 = ("abc",) # これはタプル
t2 = ("abc")  # これは文字列
print("t1 type = " + str(type(t1)))
print("t2 type = " + str(type(t2)))
