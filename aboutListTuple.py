import random

l1 = ["春", "夏"]
l2 = ["秋", "冬"]

l3 = l1 + l2
print("l3 = " + str(l3))
print(random.choice(l3)) # l3からランダムに要素を取り出す
print("l3.index(秋) = " + str(l3.index("秋")))

random.shuffle(l3) # リストの要素をシャッフル
print(l3)

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

# リストの内包表記
months = [str(m) + "月" for m in range(1, 13)]
print(months)

heisei = [13, 15, 20, 3, 7]
seireki = [y + 1988 for y in heisei]
print(seireki)

colors1 = ["white", "black", "red", "blue"]
colors2 = [f"{i}:{v}" for i, v in enumerate(colors1)]
print(colors2)

nums1 = [6, 2, 53, 72, 83, 16, 20, 41, 93]
nums2 = [n for n in nums1 if n % 2 == 0]
print(nums2)

names = [("abe", "male"), ("baba", "male"), ("caty", "female"), ("daigo", "male"), ("eibon", "female")]
man1 = list(filter(lambda n: n[1] == "male", names))
print("man1 = " + str(man1))
man2 = [n for n in names if n[1] == "male"]
print("man2 = " + str(man2))

rate = 108
dolls = [9.5, 2.0, 13.8, 17.0, 6.6, 19.0]
yens1 = list(map(lambda d: d * rate, dolls))
print("yens1 = " + str(yens1))
yens2 = [d * rate for d in dolls]
print("yens2 = " + str(yens2))

yens3 = list(map(lambda d: d * rate, filter(lambda d: d >= 10, dolls)))
print(yens3)
yens4 = [d * rate for d in dolls if d >= 10]
print(yens4)
