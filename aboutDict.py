dict = {} # 空の辞書の作成

dict = {"number":1234, "name":"python", "age":3}
print("dict = " + str(dict))

dict["age"] = 2 # 要素の変更
dict["color"] = "blue" # 存在しないキーを指定するとその要素が追加
print("変更後1 dict = " + str(dict))

# 辞書のキーは変更不可な値ならＯＫのため、タプルでも良い
dict[("abc", 123)] = "def456"
print("変更後2 dict = " + str(dict))

# 辞書の要素にはリスト、タプル、他の辞書もＯＫ
dict[(1000,"aaa")] = ["bbb", 2000]
print("変更後3 dict = " + str(dict))

# itemsメソッドでキーと値のペアをまとめたオブジェクトを取得
print(dict.items())
for (c1, c2) in dict.items():
    print(c1, c2)

# keysメソッドでキーのみをまとめたオブジェクトを取得
print(dict.keys())
for c1 in dict.keys():
    print(c1)

# valuesメソッドで要素のみをまとめたオブジェクトを取得
print(dict.values())
for c1 in dict.values():
    print(c1)

# キーや値があるか調べる
if "name" in dict: # nameというキーがあるか調べる
    print("true")
else :
    print("false")

if 2 not in dict.values(): # 2という要素がないか調べる
    print("true")
else :
    print("false")

# 要素がリストの部分の値のみの出力
dict["exp"] = ["123", "abc", "456", "def"]
for elm in dict["exp"]:
    print(elm)

# 辞書の内包表記
enw = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
jaw = ["日", "月", "火", "水", "木", "金", "土"]
weekdays = {e:j for e, j in zip(enw, jaw)}
print("weekdays = " + str(weekdays))

years1 = [1989, 2018, 1989, 1972, 2001, 1972, 2018]
years2 = {str(y) + "年" for y in years1}
print("years2 = " + str(years2)) # 重複する要素は削除される
years3 = {str(y) + "年" for y in years1 if y >= 2000}
print("years3 = " + str(years3))
