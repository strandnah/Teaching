import tkinter as tk
from tkinter import messagebox

# Fragen und Antworten
questions = [
    {"question": "Was ist die Hauptstadt von Frankreich?",
     "choices": ["Berlin", "Paris", "Rom", "Madrid"],
     "answer": "Paris"},

    {"question": "Wie viele Kontinente gibt es auf der Erde?",
     "choices": ["5", "6", "7", "8"],
     "answer": "7"},

    {"question": "Welches Element hat das chemische Symbol O?",
     "choices": ["Gold", "Oxygen", "Zink", "Eisen"],
     "answer": "Oxygen"}
]


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz")
        self.root.geometry("400x350")
        self.root.config(bg="lightblue")  # Hintergrundfarbe des Fensters

        # Variablen
        self.current_question = 0
        self.score = 0
        self.user_answer = tk.StringVar()
        self.checkbox_var = tk.BooleanVar()  # Variable für die Checkbox

        # GUI-Elemente
        self.question_label = tk.Label(
            self.root, text="", wraplength=300, bg="lightblue", font=("Arial", 12))
        self.question_label.pack(pady=20)

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.root, text="", variable=self.user_answer,
                                value="", bg="lightblue", font=("Arial", 10), anchor='w')
            rb.pack(anchor='w')
            self.radio_buttons.append(rb)

        # Checkbox erstellen
        self.checkbox = tk.Checkbutton(
            self.root, text="Ich bin bereit!", variable=self.checkbox_var, bg="lightblue", font=("Arial", 10))
        self.checkbox.pack(pady=10)

        self.submit_button = tk.Button(
            self.root, text="Absenden", command=self.submit_answer, bg="lightgreen", font=("Arial", 10))
        self.submit_button.pack(pady=20)

        # Quiz initialisieren
        self.load_question()

    def load_question(self):
        # Lade die aktuelle Frage und Antworten
        current_q = questions[self.current_question]
        self.question_label.config(text=current_q["question"])

        for i, choice in enumerate(current_q["choices"]):
            self.radio_buttons[i].config(text=choice, value=choice)

        self.user_answer.set(None)  # Setze Auswahl zurück
        self.checkbox_var.set(False)  # Setze die Checkbox zurück

    def submit_answer(self):
        # Überprüfe, ob die Checkbox ausgewählt ist
        if not self.checkbox_var.get():
            messagebox.showwarning(
                "Hinweis", "Bitte aktiviere die Checkbox, um fortzufahren!")
            return

        # Überprüfe die Antwort
        if self.user_answer.get() == questions[self.current_question]["answer"]:
            self.score += 1

        self.current_question += 1

        if self.current_question < len(questions):
            self.load_question()
        else:
            self.awdasf()

    def awdasf(self):
        # Zeige das Ergebnis
        messagebox.showinfo("Ergebnis", f"Deine Punktzahl: {
                            self.score}/{len(questions)}")
        self.root.quit()  # Schließe das Fenster


# Hauptprogramm
root = tk.Tk()
quiz = QuizApp(root)
root.mainloop()

