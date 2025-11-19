def add(number):
    if not (10000<= number <=99999):
        return "Input must be 5 digit."

    
    num_str=str(number)
    digits=[]
    for char in num_str:
        digit=int(char)
        new_digit=(digit+1)%10
        digits.append(str(new_digit))
        
    return int("".join(digits))

five_digit=int(input("Enter a five digit number: "))
result=add(five_digit)
print("Increment in each digit: ",result)






