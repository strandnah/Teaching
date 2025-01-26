import tkinter as tk  # Importieren der tk-Klasse
from tkinter import Toplevel

root = tk.Tk()  # Definieren der tk-Klasse
root.geometry("800x450")  # Fenstergröße
root.config(bg="grey")

# Checkbox Variablen als IntVar initialisieren
TickBox_1 = tk.IntVar()  # Variable für Checkbutton 1
TickBox_2 = tk.IntVar()  # Variable für Checkbutton 2
TickBox_3 = tk.IntVar()  # Variable für Checkbutton 3
TickBox_4 = tk.IntVar()  # Variable für Checkbutton 4


def aktionbutton_3(Window):
    print("destroy")
    #Window.destroy()


def functions2(Window):  # Fenster 2 schließen, wenn richtige Antworten ausgewählt wurden
    # Logik für das Schließen des Fensters basierend auf Checkbox-Werten
    if TickBox_1.get() == 1 and TickBox_2.get() == 0 and TickBox_3.get() == 0 and TickBox_4.get() == 0:
        print("Richtige Antwort ausgewählt!")
        Window.destroy()
    else:
        print("Falsche Antwort. Versuch es erneut.")

    # Debugging: Zeigt die aktuellen Werte der Checkboxen an
    print("Checkbox 1:", TickBox_1.get())
    print("Checkbox 2:", TickBox_2.get())
    print("Checkbox 3:", TickBox_3.get())
    print("Checkbox 4:", TickBox_4.get())


def aktionbutton_1_2():
    Fenster_Frage1 = Toplevel(root)
    Fenster_Frage1.title("Frage 1")
    Fenster_Frage1.geometry("800x450")

    label_title_1 = tk.Label(Fenster_Frage1, text="Frage 1")
    label_title_1.pack()
    label_Frage_1 = tk.Label(
        Fenster_Frage1, text="Was ist die richtige Antwort?")
    label_Frage_1.pack()
    print("Checkbox 1:", TickBox_1.get())


    # Checkbuttons erstellen
    Checkbutton_1 = tk.Checkbutton(
        Fenster_Frage1, text="Antwort 1", variable=TickBox_1)
    Checkbutton_1.pack()

    Checkbutton_2 = tk.Checkbutton(
        Fenster_Frage1, text="Antwort 2", variable=TickBox_2)
    Checkbutton_2.pack()

    Checkbutton_3 = tk.Checkbutton(
        Fenster_Frage1, text="Antwort 3", variable=TickBox_3)
    Checkbutton_3.pack()

    Checkbutton_4 = tk.Checkbutton(
        Fenster_Frage1, text="Antwort 4", variable=TickBox_4)
    Checkbutton_4.pack()

    # Button zum Überprüfen der Antworten
    button_zu_Frage_2 = tk.Button(
        Fenster_Frage1, text="Prüfen", command=lambda: functions2(Fenster_Frage1))
    button_zu_Frage_2.pack()


def functions():
    aktionbutton_1_2()
    aktionbutton_3(root)


# Hauptfenster: Begrüßungstext und Buttons
label1 = tk.Label(
    root, text="Willkommen zum schwierigsten Allgemeinwissen Quiz der Welt. Hast du Lust?", fg="white", bg="grey")
label1.pack()

Button_1 = tk.Button(root, text="Ja, ich hab mega Bock",
                     bg="grey", command=functions)
Button_1.pack()

Button_2 = tk.Button(root, text="Ne, aber mach ich trotzdem",
                     bg="grey", command=functions)
Button_2.pack()

Button_3 = tk.Button(root, text="Ne, heute wirklich nicht", bg="grey",
                     command=lambda: aktionbutton_3(root))  # Schließt Programm
Button_3.pack()
print("Checkbox 1:", TickBox_1.get())

root.mainloop()
