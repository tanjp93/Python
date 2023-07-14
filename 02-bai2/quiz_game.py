print ("Welcome to my computer quiz! ")
playing= input("Do you want to play? ")
if playing.lower()!="yes":
     quit()
else:
     print("OK! Let 's start !")
score=0
answer=input("What does CPU stand for? ")
if answer.lower()== "central proccessing unit": score+=1;print("Correct!")
else: print("Incorrect!")
answer = input("What does GPU stand for? ")
if answer.lower()=="graphics processing unit": score+=1;print("Correct")
else :print ("Incorrect")
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:  print("Incorrect!")
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
print("You got "+str(score)+"/4")
print("You got "+str(score*100/4)+"%")
