import calendar

def display_calendar(year, month):
    month_calendar = calendar.month(year, month)
    return month_calendar

year = int(input("表示したいカレンダーの年を入力してください。\n"))
month = int(input("表示したい月を入力してください\n"))

print(str(year) + "年" + str(month) + "月のカレンダーを表示します。\n")
print(display_calendar(year, month))
