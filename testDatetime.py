import datetime

weekdays = ["月", "火", "水", "木", "金", "土", "日"]
today = datetime.date.today()

ny_day = datetime.date(today.year + 1, 1, 1)
print(f"来年の1月1日は{weekdays[ny_day.weekday()]}曜日")

my_birthday = datetime.date(today.year, 9, 26)
print(f"今年の誕生日は{weekdays[my_birthday.weekday()]}曜日")

print("今年の13日の金曜日は...")
for m in range(1, 13):
    day13 = datetime.date(today.year, m, 13)
    if day13.weekday() == 4:
        print(f"{day13.month}月{day13.day}日")

xmas = datetime.date(today.year, 12, 25)
diff = xmas - today
if diff.days > 0:
    print(f"クリスマスまであと{diff.days}日")
elif diff.days == 0:
    print("今日はクリスマスです")
else :
    print(f"クリスマスは{-diff.days}日過ぎました")

two_weeks = today + datetime.timedelta(days=14)
print(f"二週間後は {two_weeks.year}年{two_weeks.month}月{two_weeks.day}日{weekdays[two_weeks.weekday()]}曜日")

now = datetime.datetime.now()
tomorrow = datetime.datetime(now.year, now.month, now.day + 1, 0, 0)

tdiff = tomorrow - now
print(f"今日は残り{tdiff.seconds/60:.1f}分")
