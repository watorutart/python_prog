s = "0123456789"

# スライス
print(s[1:4])
print(s[2:])
print(s[:])

# ステップを指定
print(s[1:8:2])
print(s[::3])
print(s[::-1])  # s[9:-1:-1]は×

year = 2020
s = f"東京オリンピックは{year}年です"
print(s)
