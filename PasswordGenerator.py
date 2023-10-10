import random
def generateRandomNumbers():
    Secret_PasswordsList = []
    for L in range(50):
        randomNumbers = ""   
        for i in range(4):                   
           randomNumbers = randomNumbers + str(random.randint(0,9))
        Secret_PasswordsList.append(randomNumbers)
    return Secret_PasswordsList



y = generateRandomNumbers()
x = open("Secret_Passwords","w")
for r in y:
    x.write(r + "\n")
    