five_digit=int(input("Enter a five digit number: "))
result=0

if not (10000<= five_digit <=99999):
    print("Input must be 5 digit.")

num_str=str(five_digit)

digits=[]

for char in num_str:
    digit=int(char)
    new_digit=(digit+1)%10
    digits.append(str(new_digit))
result=int("".join(digits))
        
print("Increment in each digit: ",result)


















