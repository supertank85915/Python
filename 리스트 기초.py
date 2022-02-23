#변수
#a = [12,33,55,14,56]

#리스트 조회
#print(a[-1])





#리스트 추가
#a.append(3)

#print(a)



#리스트 크기 호출 len() 함수
#print(len(a))


#리스트 슬라이싱 [n:m:j] (n번째 부터 m-1까지 호출,j (간격))

#fruit = ["딸기","망고","수박","사과","바나나","배"]
#print(fruit[0:3])

#print(fruit[:3])

#print(fruit[4:])

sport = ["축구","야구","농구","배구","탁구","수영","테니스"]
print(sport[4:7])

for x in range(1,6+1,2):
      print(sport[x])

print(sport[1:4])

print(sport[:3])

#리스트 정렬
a = [12,33,55,12,56]


a.sort(reserve = True) #내림차순
print(a)



#리스트 합치기

c = a +sport

print(c)
