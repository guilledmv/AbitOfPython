#Initialize a counter
i=0
while i<=15:
                #if our variable is divisible between 3 and 5-->"FIZZBUZZ"
                if i%3 == 0 and i%5 == 0:
                        print("FIZZBUZZ")
                #if our variable is divisible between 3-->"FIZZ"
                elif i%3 == 0:
                        print("FIZZ")
                #if our variable is divisible between 5-->"BUZZ"
                elif i%5 == 0:
                        print("BUZZ")
                #else--> print(value)
                else:
                        print(i)
                i+=1
