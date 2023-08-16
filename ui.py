from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

# creating interface object
class Interface:
    def __init__(self, quiz_brain: QuizBrain):
        # Quiz functionality
        self.quiz = quiz_brain

        # Interface creation
        self.window = Tk()
        self.window.title("Random Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     fill=THEME_COLOR,
                                                     text="Placeholder",
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons for the interface
        wrong_button_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=self.wrong_answer)
        self.wrong_button.grid(row=2, column=0)

        right_button_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_button_img, highlightthickness=0, command=self.right_answer)
        self.right_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    # Function for when the program goes to the next question
    def get_next_question(self):
        # window background colour will be white, each time the program moves onto a new question
        self.canvas.config(bg="white")

        """
         Conditions to determine if there are still questions left to answer; 
         otherwise, buttons will be disabled, signalling the end of the quiz  
        """
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz. Your final score is: {self.quiz.score}/{self.quiz.question_number}. Exit to try again.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    # Functions for the buttons
    def wrong_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def right_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    # Conditions that will run, depending on whether the question is true or false
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
