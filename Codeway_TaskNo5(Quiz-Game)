class Question:
    def __init__(self, quiry, options, correct_answer):
        self.quiry = quiry
        self.options = options
        self.correct_answer = correct_answer

    def display_question(self,question_number):
        print(f"Q.{question_number} {self.quiry}")
        for index, option in enumerate (self.options):
            print(f"{index + 1}. {option}")

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

def run_quiz(questions):
    score = 0
    total_questions = len(questions)
    for i, question in enumerate(questions, 1):
        question.display_question(i)
        while True:
            user_answer = input("Enter the number of your answer or ('q' to quit): ")
            if user_answer == 'q':
                print("Quitting the game.")
                print(f"Your final score is {score} out of {total_questions} questions.")
                return
            elif user_answer.isdigit():
                user_answer = int(user_answer)
                if 1 <= user_answer <= len(question.options):
                    break
                else:
                    print("Invalid option. Please choose a valid option.")
            else:
                print("Invalid input. Please enter a number.")

        if question.check_answer(user_answer):
            print("Correct")
            score += 1
        else:
            print("Incorrect")
            print(f"Correct answer is: {question.options[question.correct_answer - 1]}")
        print()
        
    print(f"You got {score} out of {total_questions} questions correct!")

def play_quiz():
    while True:
        questions = [
            Question("What is the largest ocean on Earth?",
                        ["Atlantic Ocean","Indian Ocean","Pacific Ocean","Arctic Ocean"],
                        3),
            Question("Who was the first person to step on the Moon?",
                        ["Neil Armstrong","Buzz Aldrin","Yuri Gagarin","John Glenn"],
                        1),
            Question("Which animal is known as the 'King of the Jungle'?",
                        ["Tiger","Lion","Leopard","Cheetah"],
                        2),
            Question("What is the chemical symbol for oxygen?",
                        ["O","Oc","Oz","Ox"],
                        1),
            Question("Who is the author of the Harry Potter book series?",
                        ["J.R.R. Tolkien","Stephenie Meyer","J.K. Rowling","George R.R. Martin"],
                        3),
            Question("Which continent is the largest by land area?",
                        ["Africa","Asia","North America","Europe"],
                        2),
            Question("What is the chemical symbol for carbon dioxide?",
                        ["Co","C","Co2","Cd"],
                        3),
            Question("Who painted the famous artwork 'The Starry Night'?",
                        ["Pablo Picasso","Vincent van Gogh","Leonardo da Vinci","Claude Monet"],
                        2),
            Question("Which planet is known as the 'Morning Star' and 'Evening Star'?",
                        ["Mars","Mercury","Jupiter","Venus"],
                        4),
            Question("Who developed the theory of relativity?",
                        ["Isaac Newton","Nikola Tesla","Albert Einstein","Galileo Galilei"],
                        3)
        ]

        print("**** Welcome to Quiz-Game ****\n")
        print("*** Rules of Game ***")
        print("1) You have to choose one correct option out of four.")
        print("2) Enter 'q' at any time to quit the game.\n")
        run_quiz(questions)
        play_again = input("Do you want to play again? (y/n): ")
        
        if play_again.lower() != "y":
            print("Thanks for playing!")
            break

play_quiz()

