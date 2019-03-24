nums = [1, -4, 6, 5, 4, -10]
plus = filter(lambda n: n>0, nums) # filterオブジェクトとして格納
print(plus)

plus = list(plus) # リストに変換
print(plus)

nums2 = map(lambda n: n*2, nums)
print(nums2)

nums2 = list(nums2)
print(nums2)

people = ["abe,11", "baba,37", "caty,51", "daigo,23", "eibon,44"]
ages = list(map(lambda p: int(p.split(",")[1]), people))
ages.sort()
print(ages)
