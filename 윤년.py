y = int(input("년도 입력:"))

if y % 400 == 0:
       print("윤년")
elif y % 4 == 0 and y % 100 != 0:
       print("윤년")
else:
       print("평년")
