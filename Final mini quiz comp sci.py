#Mini Quiz for cs4sof

print("WELCOME TO THE OFFICIAL SOF QUIZ MY BOI!!!! LETS GET DOWN TO BIDNISS")

print("Question 1, How many exhibitions do we need? ") #Question 1, up to 3 points
q1 = input("How many exhibitions? ")
if q1 == "4" or q1 == "too many" or q1 == "Too many" or q1 == "four":
    print("Correct! Plus 3 points!")
else:
    print("Eh.. not quite.")

print("Question 2, Mr. Wilson has signature catchphrases A, B and C.") #Question 2, up to
print("A: That's right!")
print("B: Eh...")
print("C: Ask a friend")
q2 = input("Q2, how do you know if you got a question right in math?")
if q2 == "A" or q2 == "a":
    print("Eh... That's not right. Do better.")
elif q2 == "B" or q2 == "b":
    print("CORRECT! MR WILSON NEVER HELPS!!!!!!!!!!!!!!!! +5")
elif q2 == "C" or q2 == "c":
    print("The correct answer is B but this works too, thanks Mr. Wilson... +3")
else: #This can leave you with either 8 or 6 points
    print("How did you mess up??? A B OR C!")
print("Question 3, What does SOF stand for?")  #Question 3, either 8 or 10 points
q3 = input("SOF: ")
if q3 == "School of the Future" or q3 == "school of the future" or q3 == "School of Future":
    print("Correct! Duh. +2 points")
else:
    print("You've been at this school for at least a few years now and you dont know what sof stands for???")

print("Question 4, What is the square root of 144?")
q4 = input("sqrt(144) = ") #Q4, either 11 or 13
if q4 == "12" or q4 == "Twelve" or q4 == "twelve":
    print("Ayy you know basic math, +3 points")
else:
    print("Well, all that matters is that you tried..")

print("Question 5, Who said 'It do not matter'? ")
print("A: 21 Savage")
print("B: Lil Yachty")
print("C: Lil Uzi Vert")
print("D: Kodak Black")
print("E: 22 Savage")
q5 = input("A, B, C, D or E? ")
#Question 5, either 16 or 18.
if q5 == "C" or q5 == "c" or q5 == "Yuh":
    print("Yuh you was right, +5 points.")
elif q5 == "b" or q5 == "B":
    print("It wasn't lil boat but you're close.")
else:
    print("You got this wrong? I bet you listen to Kodak smh..")
#Question 6, up to 19
print("Question 6, What's a great way to waste time?")
print("A. Doing your exhibitions")
print("B. Studying online")
print("C. Using Quizlet.live in irimina's class")
q6 = input("A, B or C? ")
if q6 == "C" or q6 == "c":
    print("Correct! I hope we never do that again! +3")
else:
    print("You can't be serious..")

print("Question 7, What does STEM stand for?")#Question 7, up to 23
q7 = input("STEM: ")
if q7 == "Science Technology Engineering Math" or q7 == "science technology engineering math":
    print("Correct! +4 points")
else:
    print("Not quite, make sure your spelling is correct")
print("Question 8, True or False;")#Question 8, up to 25 points
q8 = input("There is a robotics club here at SOF: ")
if q8 == "True" or "true" or "facts" or "Facts":
    print("Heck yeah there is SOF RC!!! +2 points")
else:
    print("ACTUALLY there is a robotics club. Smh.")

print("Question 9: What does CD stand for?")#Question 9, up to 30 points
q9 = input("CD: ")
if q9 == "Compact Disc" or q9 == "comapct disc":
    print("Correct! You really know your stuff! + 5 points")
elif q9 == "Compact Disk" or q9 == "compact disk":
    print("Actually, Disc and Disk are two different things! This was close enough though.")
else:
    print("Not quite, please move on to the next question. ")

print("Question 10: What time does high school advisory START officially?")
q10 = input("Start of advisory: ")
if q10 == "8:35" or q10 == "Eight Thirtyfive":
    print("Correct! You know when to get to school! +3")#Question 10, 33 points.
else:
    print("Make sure you put the time in Hour:Minute format!")

print("You have made it to the end of the SOF Quiz! Let's see how you did...")

print("If you got all questions right, congratulations!")
print("If not, keep trying!")
print("You can get a maximum of 33 points. Keep that in mind when grading.")

if q1 == "4" or q1 == "too many" or q1 == "Too many" or q1 == "four":
    print("3 points plus..")
else:
    print("0 points plus..")

if q2 == "B" or q2 == "b":
    print("5 points plus..")
elif q2 == "C" or q2 == "c":
    print("3 points plus..")
else:
    print("0 points plus..")

if q3 == "School of the Future" or q3 == "school of the future" or q3 == "School of Future":
    print("2 points plus..")
else:
    print("0 points plus..")

if q4 == "12" or q4 == "Twelve" or q4 == "twelve":
    print("3 points plus..")
else:
    print("0 points plus..")

if q5 == "C" or q5 == "c" or q5 == "Yuh":
    print("5 points plus...")
else:
    print("0 points plus..")
if q6 == "C" or q6 == "c":
    print("3 points plus...")
else:
    print("0 points plus...")
if q7 == "Science Technology Engineering Math" or q7 == "science technology engineering math":
    print("4 points plus...")
else:
    print("0 points plus...")
if q8 == "True" or "true" or "facts" or "Facts":
    print("2 points plus...")
else:
    print("0 points plus...")
if q9 == "Compact Disc" or q9 == "comapct disc":
    print("5 points plus...")
else:
    print("0 points plus...")
if q10 == "8:35" or q10 == "Eight Thirtyfive":
    print("3 points.")#Question 10, 33 points.
else:
    print("0 points.")


print("To calculate your total, insert your values!")
q1i = int(input("Score for q1: "))
q2i = int(input("Score for q2: "))
q3i = int(input("Score for q3: "))
q4i = int(input("Score for q4: "))
q5i = int(input("Score for q5: "))
q6i = int(input("Score for q6: "))
q7i = int(input("Score for q7: "))
q8i = int(input("Score for q8: "))
q9i = int(input("Score for q9: "))
q10i = int(input("Score for q10: "))
Total = q1i + q2i + q3i + q4i + q5i + q6i + q7i + q8i +q9i + q10i

print("Your total was: ", Total, "Out of 33.")

print("Thanks for taking my quiz!")
