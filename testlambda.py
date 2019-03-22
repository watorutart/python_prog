sum = lambda n1, n2: n1 + n2

s1 = sum(10, 20)
print(s1)

people1 = [("c", 30), ("b", 200), ("a", 1000), ("d", 4)]
people2 = sorted(people1, key=lambda t:t[1])
print(people2)
