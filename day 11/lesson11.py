#მომხარებელს შემოატანინეთ მშობლების ასაკი, დედის და მამის ასაკი, შემდეგ თუ დედის ასაკი მეტი იქნება მამის ასაკზდაგვიბეჭდოს რომ დედა დიდი მამაზე, თუ პირიქით მამის ასაკი მეტი იქნება დედის ასაკზე მაგ შემთხვევაში დაგვიბეჭდოს რომ მამა დიდია დედაზე. მინიშნება დაგჭირდებათ (if)

mom_age = int(input("deda! sheiyvane sheni asaki:  "))
dad_age = int(input("mama! sheiyvane sheni asaki:  "))

if mom_age > dad_age:
    print(" deda ufro didia vidre mama ")

if dad_age > mom_age:
    print(" mama ufro didia vidre deda ")
    