amt=int(input("Enter amount ending with 0s: "))
hundred=amt//100
amt=amt-hundred*100
fifty=amt//50

amt=amt-fifty*50
ten=amt//10



print("Each denomination notes for the amount:", "\n in hundred: ", hundred,"\n in fifties: ", fifty,"\n in tens: ", ten)
