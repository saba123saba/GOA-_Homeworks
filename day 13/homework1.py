score1 = int(input("Enter score1: "))
score2 = int(input("Enter score2: "))
score3 = int(input("Enter score3: "))
score4 = int(input("Enter score4: "))

sum = (score1 + score2 + score3 + score4) / 4 

# print(sum)

if sum > 8 and sum < 4:
    print(" ყოჩაღ, კარგი შედეგია! ")
else:
    print(" ცუდი შედეგია, გამოასწორე! ")