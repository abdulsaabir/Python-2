print("Welcome to my computer quiz!")

willPlay = input("Do you want to play? ").lower()

if willPlay not in ['yes', 'y']:
    print("Okay, maybe next time!")
    quit()

print("Okay! Let's play :)")

score = 0
questions = ["cpu", "gpu", "ram", "psu", "hdd", "ssd", "os", "lan", "wan", "usb"]
answers = ["central processing unit", "graphics processing unit", "random access memory", 
           "power supply", "hard disk drive", "solid state drive", 
           "operating system", "local area network", "wide area network", 
           "universal serial bus"]

# Loop through the questions using zip
for question, answer in zip(questions, answers):
    ans = input(f"What does {question} stand For?:  ").strip().lower()
    if ans == answer:
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

# Calculate and print the score
percentage_correct = (score / len(questions)) * 100
print("\nYou got", score, "questions correct!")
print("You got {:.2f}%.".format(percentage_correct))
