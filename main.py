import calc_bmi

print("BMI計算アプリ")
s = int(input("身長:"))
t = int(input("体重:"))

print(f"BMI:{calc_bmi.get_area(s,t)}")


print("2回目")
s = int(input("スン超"))
t = int(input("体重"))

print(f"BMI:{calc_bmi.get_area(s,t)}")


