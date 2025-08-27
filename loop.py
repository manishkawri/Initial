for letter in "python":
    print(letter)

for plate in range (1, 20):
    if plate == 1:
        print("all good")
    elif plate == 5:
        print("Fat")  
    elif plate>=10:
        print("Tata bye bye , Goodbye , Khattam")         
        break

for number in range(0,100):
    if number % 2 == 0:
        print(f"{number} is even")
        continue
       # print(f"{number} is odd")    
        #break
