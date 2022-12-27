
nt = 0 
score = 0
question = ["Where is the capital of Nigeria", 
            "Number of states in Nigeria", "Number of LGAs in Nigeria",
            "Who is INEC chairman", 
            "How many political parties participated in 2019 presidential election"]
option = [
           "(a) Lagos \n (b) Kano \n (c) Abuja",
           "(a) 37 \n (b) 36 \n (c) 44",
           "(a) 768 \n (b) 774 \n (c) 780",
           "(a) Prof. Mamhood Yakubu \n (b) Prof. Mohamed Yakub \n (c) Muhamad Yakubu",
           "(a) 18 \n (b) 77 \n (c) 73"
        ]
answer = ["c", "b", "b", "a", "c"]
for que in question:
    print(que)
    print(option[nt])
    ans = input("Your answer > ")
    if ans == answer[nt]:
        score += 5
        # print("you are correct")    
    else:
        pass
        # print("you are wrong")
    nt +=1
print("you total score is ", score)