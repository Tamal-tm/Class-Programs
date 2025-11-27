five_digit=int(input("Enter a five digit number: "))
result=0

num_str=str(five_digit)

digits=[]
for char in num_str:
    digit=int(char)
    new_digit=(digit+1)%10
    digits.append(str(new_digit))
result=int("".join(digits))
        
print("Increment in each digit: ",result)
























