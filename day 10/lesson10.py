#2) მომხმარებელს შემოატანინეთ ორი ბულიან ტიპის მნიშვნელობა(true, false), შემდეგ კი დაბეჭდეთ ერკანზე ეს მნიშვნელობები      შედარებული ერთმანეთზე, ამისთვის გამოიყენეთ ლოგიკური ოპერატორები (and და or)

question1 = bool (input(" type first answer(true and false):  "))
question2 = bool (input(" type second answer:  "))

answer1 = question1 and question2
answer2 = question1  or  question2

print(answer1)
print(answer2)