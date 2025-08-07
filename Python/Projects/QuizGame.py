print("Welcome user!")

playing = input("Do you want to play? (yes/no) ")
if playing.lower() != "yes":
    quit()

print("Okay....let's go!")
score = 0

answer = input("What does TPU stand for? ")
if answer.lower() == "tensor processing unit":
    print("Yahoo!")
    score += 1
else:
    print("Head back to ur studies my nigga!")
    
answer = input("Where is Amazon Rainforest? ")
if answer.lower() == "south america":
    print("Yahoo!")
    score += 1
else:
    print("Head back to ur studies my nigga!")
    
answer = input("What is the theory of the origin of the universe called? ")
if answer.lower() == "big bang":
    print("Yahoo!")
    score += 1
else:
    print("Nah man you are cooked!")
    
answer = input("What is the leftover radiation from the Big Bang called? ")
if answer.lower() == "cosmic microwave radiation":
    print("Yahoo!")
    score += 1
else:
    print("Head back to ur studies my nigga!")
    
answer = input("Smallest Unit of Matter? ")
if answer.lower() == "quark":
    print("Yahoo!")
    score += 1
else:
    print("Head back to ur studies my nigga!")
    
answer = input("What is a rapidly spinning neutron star that emits radiation? ")
if answer.lower() == "supernova":
    print("Yahoo!")
    score +=1
else:
    print("Alright man, u need to get off of your phone and do some studies.")
    
print("Congrats mate, your score is " +str(score)+ " Out of 6")