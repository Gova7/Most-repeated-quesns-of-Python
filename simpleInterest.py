# WAP to enter time, rate, and principle from the user & calculate the
# simple interest. (using functions)

def simpleInterest(time, rate, principle):
  SI = (principle * rate * time) / 100
  return SI


time = int(input("Enter time: "))
rate = int(input("Enter rate: "))
principle = int(input("Enter principle amount: "))

SI = simpleInterest(time, rate, principle)

print("SI : ", SI)
