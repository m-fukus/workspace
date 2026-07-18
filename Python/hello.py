from datetime import datetime

name = input("名前を入力してください: ")
print("Hello, " + name + "!")

while True:
    birthday_str = input("生年月日を入力してください(yyyyMMdd): ")
    if len(birthday_str) != 8 or not birthday_str.isdigit():
        print("yyyyMMddの形式で入力してください")
        continue
    try:
        birthday = datetime.strptime(birthday_str, "%Y%m%d")
        break
    except ValueError:
        print("正しい日付を入力してください")

today = datetime.today()
age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
print("年齢: " + str(age))
