# loop ში გაშვება

# for i in range(1000):
#     print(str(i) + ". l LOVE YOU <3 ") 

question = input("გოა მაგარია? ")

for i in range (10):
    if question == "კი" or question == "დიახ":
        print("მართალიხარ")
    else:
        question = input("გოა მაგარია? ")

    