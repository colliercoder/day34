from tkinter import *
from data import question_data
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    """Taking in the QuizBrain object from quiz_brain as a parameter"""
    def __init__(self,quiz_brain: QuizBrain ):
        """Creating a quiz object from the quizbrain parameter"""
        self.quiz = quiz_brain
        self.window = Tk()
        self.score = 0
        #Window
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        #Canvas
        self.canvas = Canvas(width=300,height=250)
        self.canvas.grid(row=1,column=0,columnspan=2,padx=20,pady=20)
        """The width=280 property is 20 less than the canvas width of 300. Using width makes the text wrap"""
        self.question = self.canvas.create_text(150,125,text="",font=("Arial",20,"italic"),width=280)

        #Score Label
        self.score_label = Label(text=f"Score: {self.score}")
        self.score_label.grid(row=0,column=1)
        self.score_label.config(bg=THEME_COLOR,highlightthickness=0,fg="white")

        #True button checkmark

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,highlightthickness=0,padx=20,pady=20,command=self.true_click)
        self.true_button.grid(row=2,column=0)

        #False button X

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image,highlightthickness=0,padx=20,pady=20,command=self.false_click)
        self.false_button.grid(row=2,column=1)

        """Calling the question text from the function below"""
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text = q_text)

    def false_click(self):
        user_answer = "False"
        if self.quiz.check_answer(user_answer=user_answer):
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.config(bg="Green")
            self.window.after(300, self.change_back_screen)
            self.get_next_question()
        else:
            self.canvas.config(bg="Red")
            self.window.after(300, self.change_back_screen)
            self.get_next_question()

    def true_click(self):
        user_answer = "True"
        if self.quiz.check_answer(user_answer=user_answer):
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.config(bg="Green")
            self.window.after(300, self.change_back_screen)
            self.get_next_question()
        else:
            self.canvas.config(bg="Red")
            self.window.after(300,self.change_back_screen)
            self.get_next_question()
            # change the score label
    # change the score label
    def change_back_screen(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions()==False:
            self.canvas.itemconfig(self.question, text = f"Your score is {self.score}/{len(self.quiz.question_list)}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


