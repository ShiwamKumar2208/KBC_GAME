import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def check():
    nm = input("Enter your name last time: ")
    gender = input("Enter your gender: ")
    am = input("Amount won: ")
    speak("this is your check")
    print("----------------check---------------------")
    print(f"|   NAME:- {nm}                  ")
    print(f"|   GENDER:- {gender}            ")
    print("|   ACCOUNT NUMBER:- **************        ")
    print(f"|   AMOUNT SEND:- {am}            ")
    print("------------------------------------------")

def intro():
    nm = input("Enter your name: ")
    print("                                    |-------------------------|                                        ")
    print("                                    |!!KAUN BANEGA CROREPATI!!|                                        ")
    print("                                    |-------------------------|                                        ")
    speak(f"i AM Amitab Bachchan with {nm} so without any lost of time lets plays who will be the millionare")
    print(f"i AM Amitab Bachchan with {nm} so without any lost of time lets plays who will be the millionare")
    speak("let me explain you the rules")
    print("RULES:-")
    speak("first there will be twelve questions those you should have to answer")
    print("1.There will be 12 questions\n1>> 1,000 INR\n2>> 5,000 INR\n3>> 10,000 INR\n4>> 25,000 INR\n5>> 50,000 INR\n6>> 1,00,000 INR\n7>> 3,00,000 INR\n8>> 6,00,000 INR\n9>> 15,00,000 INR\n10>> 50,00,000 INR\n11>> 1,00,00,000 INR\n12>> JACKPOT QUESTION = 7,00,00,000")
    speak("second you have full time to answer the questions")
    print("2.No time limits")
    speak("third jackpot questions winning amount is seven crore")
    print("3.Jackpot Question = 7,00,00,000 INR")
    speak("fourth their will be quiz round first then main questions")
    print("4.QUIZ Round (quiz round have a simple question you needs to answer it correctly to qualify to the main round)")
    speak("fifth you have to answer it correctly to go to the next question")
    print("5.You have to answer all the questions(NOTE: if you give the wrong answer you will not get any money")
    speak("ask shiwam kumar for more information")
    print("6.Ask SHIWAM KUMAR for more info")
    speak("overall its a fun game and you will not get a single money")
    print("7.Overall its a fun game and you will not get a single money\nMADE BY:- SHIWAM KUMAR")


def questions():
    nm = input("Enter your name again plz: ")
    speak("first lets take the quiz round")
    print("                                          |QUIZ ROUND|                                                  ")
    speak("question of the quiz round")
    speak("Pongal is a popular festival of which state?")
    print("Q.Pongal is a popular festival of which state?")
    print("A.Karnataka\nB.Kerala\nC.Tamil Nadu\nD.Andhra Pradesh")
    qu = input("Enter your choice:- ")

    if "a" in qu:
        speak("wrong answer sorry you are not eligible for the main round")
        print("wrong answer sorry you are not eligible for the main round")
    elif "b" in qu:
        speak("wrong answer sorry you are not eligible for the main round")
        print("wrong answer sorry you are not eligible for the main round")
    elif "d" in qu:
        speak("wrong answer sorry you are not eligible for the main round")
        print("wrong answer sorry you are not eligible for the main round")
    elif "c" in qu:
        speak("correct answer")
        print("correct answer you was qualified for the main round")
        print("                                      |MAIN ROUND|                                                   ")
        speak("first question of main round")
        speak("the first questions pize money is 1,000")
        speak("Which of the following is observed as Sports Day every year?")
        print("Q.1.Which of the following is observed as Sports Day every year?")
        print("A.22nd April\nB.26th july\nC.29th August\nD.2nd October")
        q1 = input(f"Enter a choice {nm}:- ")

        if "a" in q1:
            speak(f"wrong answer sorry you are not eligible for the main round {nm}")
            print(f"wrong answer sorry you are not eligible for the main round {nm}")
        elif "b" in q1:
            speak(f"wrong answer sorry you are not eligible for the main round {nm}")
            print(f"wrong answer sorry you are not eligible for the main round {nm}")
        elif "d" in q1:
            speak(f"wrong answer sorry you are not eligible for the main round {nm}")
            print(f"wrong answer sorry you are not eligible for the main round {nm}")
        elif "c" in q1:
            speak(f"correct answer {nm}")
            print(f"correct answer {nm} you got 1,000 rupees")
            if "c" in q1:
                speak("second question of main round")
                speak("the second questions pize money is 5,000")
                speak("World Health Day is observed on?")
                print("Q.2.World Health Day is observed on?")
                print("A.Apr 7\nB.Mar 6\nC.Mat I5\nD.Apr 28")
                q2 = input(f"Enter a choice {nm}:- ")

                if "c" in q2:
                    speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                    print(f"wrong answer sorry you are not eligible for the main round {nm}")
                elif "b" in q2:
                    speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                    print(f"wrong answer sorry you are not eligible for the main round {nm}")
                elif "d" in q2:
                    speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                    print(f"wrong answer sorry you are not eligible for the main round {nm}")
                elif "a" in q2:
                    speak(f"correct answer {nm}")
                    print(f"correct answer {nm} you got 5,000 rupees")
                    if "a" in q2:
                        speak("third question of main round")
                        speak("the third questions pize money is 10,000")
                        speak("Who is the author of the epic 'Meghdoot'?")
                        print("Q.1.Who is the author of the epic 'Meghdoot'?")
                        print("A.Vishakadatta\nB.Valmiki\nC.Banabhatta\nD.Kalidas")
                        q3 = input(f"Enter a choice {nm}:- ")

                        if "a" in q3:
                            speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                            print(f"wrong answer sorry you are not eligible for the main round {nm}")
                        elif "b" in q3:
                            speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                            print(f"wrong answer sorry you are not eligible for the main round {nm}")
                        elif "c" in q3:
                            speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                            print(f"wrong answer sorry you are not eligible for the main round {nm}")
                        elif "d" in q3:
                            speak(f"correct answer {nm}")
                            print(f"correct answer {nm} you got 10,000 rupees")
                            if "d" in q3:
                                speak("fourth question of main round")
                                speak("the fourth questions pize money is 20,000")
                                speak("Which day is observed as the World Standards  Day?")
                                print("Q.1.Which day is observed as the World Standards  Day?")
                                print("A.June 26\nB.Oct 14\nC.Nov 15\nD.Dec 2")
                                q4 = input(f"Enter a choice {nm}:- ")

                                if "a" in q4:
                                    speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                                    print(f"wrong answer sorry you are not eligible for the main round {nm}")
                                elif "d" in q4:
                                    speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                                    print(f"wrong answer sorry you are not eligible for the main round {nm}")
                                elif "c" in q4:
                                    speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                                    print(f"wrong answer sorry you are not eligible for the main round {nm}")
                                elif "b" in q4:
                                    speak(f"correct answer {nm}")
                                    print(f"correct answer {nm} you got 20,000 rupees")
                                    if "b" in q4:
                                        speak("fifth question of main round")
                                        speak("the fifth questions pize money is 50,000")
                                        speak("The language of Lakshadweep. a Union Territory of India, is?")
                                        print("Q.1.The language of Lakshadweep. a Union Territory of India, is?")
                                        print("A.Tamil\nB.Hindi\nC.Malayalam\nD.Telugu")
                                        q5 = input(f"Enter a choice {nm}:- ")

                                        if "a" in q5:
                                            speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                                            print(f"wrong answer sorry you are not eligible for the main round {nm}")
                                        elif "d" in q5:
                                            speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                                            print(f"wrong answer sorry you are not eligible for the main round {nm}")
                                        elif "b" in q5:
                                            speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                                            print(f"wrong answer sorry you are not eligible for the main round {nm}")
                                        elif "c" in q5:
                                            speak(f"well played {nm}")
                                            print(f"well played {nm} you got 50,000 rupees")
                                            if "c" in q5:
                                                speak("sixth question of main round")
                                                speak("the sixth questions pize money is 1,00,000")
                                                speak("Ghototkach in Mahabharat was the son of?")
                                                print("Q.1.Ghototkach in Mahabharat was the son of?")
                                                print("A.Duryodhana\nB.Arjuna\nC.Yudhishthir\nD.Bhima")
                                                q6 = input(f"Enter a choice {nm}:- ")

                                                if "a" in q6:
                                                    speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                                                    print(f"wrong answer sorry you are not eligible for the main round {nm}")
                                                elif "c" in q6:
                                                    speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                                                    print(f"wrong answer sorry you are not eligible for the main round {nm}")
                                                elif "b" in q6:
                                                    speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                                                    print(f"wrong answer sorry you are not eligible for the main round {nm}")
                                                elif "d" in q6:
                                                    speak(f"well played {nm}")
                                                    print(f"well played {nm} you got 1,00,000 rupees")
                                                    if "d" in q6:
                                                        speak("seven question of main round")
                                                        speak("the seven questions pize money is 3,00,000")
                                                        speak("Which of the following Muslim festivals is based on the 'Holy Quran'?")
                                                        print("Q.1.Which of the following Muslim festivals is based on the 'Holy Quran'?")
                                                        print("A.Id -ul-Zuha\nB.Id -ul-Fitr\nC.Bakri-id\nD.Moharram")
                                                        q7 = input(f"Enter a choice {nm}:- ")

                                                        if "c" in q7:
                                                            speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                                                            print(f"wrong answer sorry you are not eligible for the main round {nm}")
                                                        elif "d" in q7:
                                                            speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                                                            print(f"wrong answer sorry you are not eligible for the main round {nm}")
                                                        elif "b" in q7:
                                                            speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                                                            print(f"wrong answer sorry you are not eligible for the main round {nm}")
                                                        elif "a" in q7:
                                                            speak(f"well played {nm}")
                                                            print(f"well played {nm} you got 3,00,000 rupees")
                                                            if "a" in q7:
                                                                speak("eight question of main round")
                                                                speak("the eight questions pize money is 6,00,000")
                                                                speak("The first month of the Indian national calendar is?")
                                                                print("Q.1.The first month of the Indian national calendar is?")
                                                                print("A.Magha\nB.Chaitra\nC.Ashadha\nD.Vaishakha")
                                                                q8 = input(f"Enter a choice {nm}:- ")

                                                                if "c" in q8:
                                                                    speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                                                                    print(f"wrong answer sorry you are not eligible for the main round {nm}")
                                                                elif "d" in q8:
                                                                    speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                                                                    print(f"wrong answer sorry you are not eligible for the main round {nm}")
                                                                elif "a" in q8:
                                                                    speak(f"wrong answer sorry you are not eligible for the main round {nm}")
                                                                    print(f"wrong answer sorry you are not eligible for the main round {nm}")
                                                                elif "b" in q8:
                                                                    speak(f"well played {nm}")
                                                                    print(f"well played {nm} you got 6,00,000 rupees")
                                                                    if "b" in q8:
                                                                        speak("nine question of main round")
                                                                        speak("the nine questions pize money is 15,00,000")
                                                                        speak("Which of the following is not a dance from Kerala?")
                                                                        print("Q.1.Which of the following is not a dance from Kerala?")
                                                                        print("A.Kathakali\nB.Mohiniattam\nC.Ottan Thullal\nD.Yaksha Gana")
                                                                        q9 = input(f"Enter a choice {nm}:- ")

                                                                        if "c" in q9:
                                                                            speak(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                            print(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                        elif "b" in q9:
                                                                            speak(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                            print(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                        elif "a" in q9:
                                                                            speak(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                            print(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                        elif "d" in q9:
                                                                            speak(f"well played {nm}")
                                                                            print(f"well played {nm} you got 15,00,000 rupees")
                                                                            if "d" in q9:
                                                                                speak("tenth question of main round")
                                                                                speak("the tenth questions pize money is 50,00,000")
                                                                                speak("Which of the followiing is a folk dance of India?")
                                                                                print("Q.1.Which of the followiing is a folk dance of India?")
                                                                                print("A.Kathakali\nB.Mohiniattam\nC.Garba\nD.Manipuri")
                                                                                q0 = input(f"Enter a choice {nm}:- ")

                                                                                if "b" in q0:
                                                                                    speak(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                                    print(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                                elif "d" in q0:
                                                                                    speak(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                                    print(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                                elif "a" in q0:
                                                                                    speak(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                                    print(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                                elif "c" in q0:
                                                                                    speak(f"well played {nm}")
                                                                                    print(f"well played {nm} you got 50,00,000 rupees")
                                                                                    if "c" in q0:
                                                                                        speak("eleventh question of main round")
                                                                                        speak("the eleventh questions pize money is 1,00,00,000")
                                                                                        speak("Dogri is spoken in which of the following states?")
                                                                                        print("Q.1.Dogri is spoken in which of the following states?")
                                                                                        print("A.Bihar\nB.Orissa\nC.Assam\nD.Jammu & Kashmir")
                                                                                        q11 = input(f"Enter a choice {nm}:- ")

                                                                                        if "c" in q11:
                                                                                            speak(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                                            print(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                                        elif "b" in q11:
                                                                                            speak(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                                            print(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                                        elif "a" in q11:
                                                                                            speak(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                                            print(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                                        elif "d" in q11:
                                                                                            speak(f"you are great {nm} i have never seen anyone like you")
                                                                                            print(f"you are great {nm} i have never seen anyone like you and you got 1,00,00,000 rupees")
                                                                                            if "d" in q11:
                                                                                                print("                                                |--------------------------|")
                                                                                                print("                                                |      JAKPOT QUESTION     |")
                                                                                                print("                                                |--------------------------|")
                                                                                                speak("jackpot question!!!!!")
                                                                                                speak("you are really great")
                                                                                                speak("twelfth question of main round")
                                                                                                speak("the twelfth questions pize money is 7,00,00,000")
                                                                                                speak("who roled as thanos in the fiction movie Avengers Endgame?")
                                                                                                print("Q.1.who roled as thanos in the fiction movie Avengers Endgame?")
                                                                                                print("A.Chris Pratt\nB.Josh Brolin\nC.Mark Ruffalo\nD.Paul Rudd")
                                                                                                q12 = input(f"Enter a choice {nm}:- ")

                                                                                                if "c" in q12:
                                                                                                    speak(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                                                    print(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                                                elif "d" in q12:
                                                                                                    speak(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                                                    print(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                                                elif "a" in q12:
                                                                                                    speak(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                                                    print(f"wrong answer  sorry you are not eligible for the main round {nm}")
                                                                                                elif "b" in q12:
                                                                                                    speak(f"you are the winner {nm} you played very well")
                                                                                                    print(f"well played {nm} you got 7,00,00,000 rupees")

if __name__ == "__main__":
    while True:
        intro()
        questions()
        check()