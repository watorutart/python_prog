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

yen = 228080
print(f"{yen:,}円")

n = 255
print(f"n -> 10進数：{n:d}")
print(f"n -> 2進数：{n:b}")
print(f"n -> 8進数：{n:o}")
print(f"n -> 16進数：{n:x}")

print(f"1/3 -> {1/3:.3f}")
print(f"1/3 -> {1/3:.5f}")

print(f"{0.377:.2%}")

s = "Hello Python, Hello world"
print(s.find("Python"))
print(s.find("Hello"))
print(s.find("Hello",3))
