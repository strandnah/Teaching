import tkinter as tk  # Importieren der tk-Klasse
from tkinter import Toplevel


root = tk.Tk()  # Definieren der tk-Klasse
root.geometry("800x450")  # Fenstergröße
root.config(bg="grey")


def aktionbutton_3(Window):  # Fenster 1 schließen, wenn man nicht spielen will
    Window.destroy()


def functions2(Window, TickBox1, TickBox2, TickBox3, TickBox4):  # TickBox Werte von Frage 1

    if TickBox1.get() == 0 and TickBox2.get() == 0 and TickBox3.get() == 1 and TickBox4.get() == 0:
        Window.destroy()
        aktionbutton_2()


def functions3(Window, TickBox5, TickBox6, TickBox7, TickBox8):  # TickBox Werte von Frage 2

    if TickBox5.get() == 0 and TickBox6.get() == 0 and TickBox7.get() == 1 and TickBox8.get() == 0:
        Window.destroy()
        aktionbutton_4()


def functions4(Window, TickBox9, TickBox10, TickBox11, TickBox12):  # TickBox Werte von Frage 3

    if TickBox9.get() == 0 and TickBox10.get() == 1 and TickBox11.get() == 0 and TickBox12.get() == 0:
        Window.destroy()
        aktionbutton_5()


def functions5(Window, TickBox13, TickBox14, TickBox15, TickBox16):  # TickBox Werte von Frage 4

    if TickBox13.get() == 1 and TickBox14.get() == 0 and TickBox15.get() == 0 and TickBox16.get() == 0:
        Window.destroy()
        aktionbutton_6()


def functions6(Window, TickBox17, TickBox18, TickBox19, TickBox20):  # TickBox Werte von Frage 5

    if TickBox17.get() == 0 and TickBox18.get() == 0 and TickBox19.get() == 1 and TickBox20.get() == 0:
        Window.destroy()
        aktionbutton_7()


def aktionbutton_1_2():  # Fenster Frage 1
    Fenster_Frage1 = Toplevel(root)
    Fenster_Frage1.title("Frage 1")
    Fenster_Frage1.geometry("800x450")
    label_title_1 = tk.Label(Fenster_Frage1, text="Frage 1")
    label_title_1.pack()
    label_Frage_1 = tk.Label(
        Fenster_Frage1, text="Welcher dieser Konflikte endete zuletzt?")
    label_Frage_1.pack()
    TickBox_1 = tk.IntVar()  # Variable für Checkbutton
    Checkbutton_1 = tk.Checkbutton(
        Fenster_Frage1, text="Koreakrieg (UN und Nordkorea, China, Sowjetunion)", variable=TickBox_1, onvalue=1, offvalue=0)
    Checkbutton_1.pack()
    TickBox_2 = tk.IntVar()  # Variable für Checkbutton
    Checkbutton_2 = tk.Checkbutton(
        Fenster_Frage1, text="Kubakrise (Vereinigte Staaten und Sowjetunion)", variable=TickBox_2, onvalue=1, offvalue=0)
    Checkbutton_2.pack()
    TickBox_3 = tk.IntVar()  # Variable für Checkbutton
    Checkbutton_3 = tk.Checkbutton(
        Fenster_Frage1, text="Sechstagekrieg (Israel und Ägypten, Jordanien, Syrien)", variable=TickBox_3, onvalue=1, offvalue=0)
    Checkbutton_3.pack()
    TickBox_4 = tk.IntVar()  # Variable für Checkbutton
    Checkbutton_4 = tk.Checkbutton(
        Fenster_Frage1, text="Mau-Mau Krieg (Britische Besatzung und Kenianische Unabhängigkeitskämpfer)", variable=TickBox_4, onvalue=1, offvalue=0)
    Checkbutton_4.pack()
    # Erstellen eines Buttons um Fenster zur Frage 2 zu öffnen & Fenster 1 zu schließen
    button_zu_Frage_2 = tk.Button(Fenster_Frage1, text="Prüfen", command=lambda: functions2(
        Fenster_Frage1, TickBox_1, TickBox_2, TickBox_3, TickBox_4))
    button_zu_Frage_2.pack()


def aktionbutton_2():  # Fenster Frage 2
    Fenster_Frage2 = Toplevel(root)
    Fenster_Frage2.title("Frage 2")
    Fenster_Frage2.geometry("800x450")
    label_title_2 = tk.Label(Fenster_Frage2, text="Frage 2")
    label_title_2.pack()
    label_Frage_2 = tk.Label(
        Fenster_Frage2, text="Was wird am 03. Oktober bundesweit gefeiert?")
    label_Frage_2.pack()
    TickBox_5 = tk.IntVar()  # Variable für Checkbutton
    Checkbutton_5 = tk.Checkbutton(
        Fenster_Frage2, text="Maria Himmelfahrt", variable=TickBox_5, onvalue=1, offvalue=0)
    Checkbutton_5.pack()
    TickBox_6 = tk.IntVar()  # Variable für Check #Zwei weitere Checkbuttons
    Checkbutton_6 = tk.Checkbutton(
        Fenster_Frage2, text="Tag des Mauerfalls", variable=TickBox_6, onvalue=1, offvalue=0)
    Checkbutton_6.pack()
    TickBox_7 = tk.IntVar()  # Variable für Checkbutton
    Checkbutton_7 = tk.Checkbutton(
        Fenster_Frage2, text="Tag der deutschen Einheit", variable=TickBox_7, onvalue=1, offvalue=0)
    Checkbutton_7.pack()
    TickBox_8 = tk.IntVar()  # Variable für Checkbutton
    Checkbutton_8 = tk.Checkbutton(
        Fenster_Frage2, text="Neujahr", variable=TickBox_8, onvalue=1, offvalue=0)
    Checkbutton_8.pack()
    # Erstellen eines Buttons um Fenster zur Frage 3 zu öffnen & Fenster 2 zu schließen
    button_zu_Frage_3 = tk.Button(Fenster_Frage2, text="Prüfen", command=lambda: functions3(
        Fenster_Frage2, TickBox_5, TickBox_6, TickBox_7, TickBox_8))
    button_zu_Frage_3.pack()


def aktionbutton_4():  # Fenster Frage 3
    Fenster_Frage3 = Toplevel(root)
    Fenster_Frage3.title("Frage 3")
    Fenster_Frage3.geometry("800x450")
    label_title_3 = tk.Label(Fenster_Frage3, text="Frage 3")
    label_title_3.pack()
    label_Frage_3 = tk.Label(
        Fenster_Frage3, text="Welche der folgenden Aussagen ist immer wahr für die Ableitung einer Funktion?")
    label_Frage_3.pack()
    TickBox_9 = tk.IntVar()  # Variable für Checkbutton
    Checkbutton_9 = tk.Checkbutton(
        Fenster_Frage3, text="Die Ableitung einer Funktion ist immer positiv", variable=TickBox_9, onvalue=1, offvalue=0)
    Checkbutton_9.pack()
    TickBox_10 = tk.IntVar()  # Variable für Checkbutton
    Checkbutton_10 = tk.Checkbutton(
        Fenster_Frage3, text="Die Ableitung gibt die Steigung des Funktionsgraphen an einem bestimmten Punkt an", variable=TickBox_10, onvalue=1, offvalue=0)
    Checkbutton_10.pack()
    TickBox_11 = tk.IntVar()  # Variable für Checkbutton
    Checkbutton_11 = tk.Checkbutton(
        Fenster_Frage3, text="Die Ableitung einer Funktion ist immer konstant", variable=TickBox_11, onvalue=1, offvalue=0)
    Checkbutton_11.pack()
    TickBox_12 = tk.IntVar()  # Variable für Checkbutton
    Checkbutton_12 = tk.Checkbutton(
        Fenster_Frage3, text="Die Ableitung existiert nur für lineare Funktionen", variable=TickBox_12, onvalue=1, offvalue=0)
    Checkbutton_12.pack()
    # Erstellen eines Buttons um Fenster zur Frage 4 zu öffnen & Fenster 3 zu schließen
    button_zu_Frage_4 = tk.Button(Fenster_Frage3, text="Prüfen", command=lambda: functions4(
        Fenster_Frage3, TickBox_9, TickBox_10, TickBox_11, TickBox_12))
    button_zu_Frage_4.pack()


def aktionbutton_5():  # Fenster Frage 4
    Fenster_Frage4 = Toplevel(root)
    Fenster_Frage4.title("Frage 4")
    Fenster_Frage4.geometry("800x450")
    label_title_4 = tk.Label(Fenster_Frage4, text="Frage 4")
    label_title_4.pack()
    label_Frage_4 = tk.Label(
        Fenster_Frage4, text="Was ist kein Content Management System?")
    label_Frage_4.pack()
    TickBox_13 = tk.IntVar()  # Variable für Checkbutton
    Checkbutton_13 = tk.Checkbutton(
        Fenster_Frage4, text="cURL", variable=TickBox_13, onvalue=1, offvalue=0)
    Checkbutton_13.pack()
    TickBox_14 = tk.IntVar()  # Variable für Checkbutton
    Checkbutton_14 = tk.Checkbutton(
        Fenster_Frage4, text="Joomla", variable=TickBox_14, onvalue=1, offvalue=0)
    Checkbutton_14.pack()
    TickBox_15 = tk.IntVar()  # Variable für Checkbutton
    Checkbutton_15 = tk.Checkbutton(
        Fenster_Frage4, text="WordPress", variable=TickBox_15, onvalue=1, offvalue=0)
    Checkbutton_15.pack()
    TickBox16 = tk.IntVar()  # Variable für Checkbutton
    Checkbutton_16 = tk.Checkbutton(
        Fenster_Frage4, text="TYPO3", variable=TickBox16, onvalue=1, offvalue=0)
    Checkbutton_16.pack()
    # Erstellen eines Buttons um Fenster zur Frage 5 zu öffnen & Fenster 4 zu schließen
    button_zu_Frage_5 = tk.Button(Fenster_Frage4, text="Prüfen", command=lambda: functions5(
        Fenster_Frage4, TickBox_13, TickBox_14, TickBox_15, TickBox16))
    button_zu_Frage_5.pack()


def aktionbutton_6():  # Fenster Frage 5
    Fenster_Frage5 = Toplevel(root)
    Fenster_Frage5.title("Frage 5")
    Fenster_Frage5.geometry("800x450")
    label_title_5 = tk.Label(Fenster_Frage5, text="Frage 5")
    label_title_5.pack()
    label_Frage_5 = tk.Label(
        Fenster_Frage5, text="Welches Land führte als erstes eine Sozialversicherung auf nationaler Ebene ein, die von Bestand war?")
    label_Frage_5.pack()
    TickBox_17 = tk.IntVar()  # Variable für Checkbutton
    Checkbutton_17 = tk.Checkbutton(
        Fenster_Frage5, text="England", variable=TickBox_17, onvalue=1, offvalue=0)
    Checkbutton_17.pack()
    TickBox_18 = tk.IntVar()  # Variable für Checkbutton
    Checkbutton_18 = tk.Checkbutton(
        Fenster_Frage5, text="China", variable=TickBox_18, onvalue=1, offvalue=0)
    Checkbutton_18.pack()
    TickBox_19 = tk.IntVar()  # Variable für Checkbutton
    Checkbutton_19 = tk.Checkbutton(
        Fenster_Frage5, text="Deutschland", variable=TickBox_19, onvalue=1, offvalue=0)
    Checkbutton_19.pack()
    TickBox_20 = tk.IntVar()  # Variable für Checkbutton
    Checkbutton_20 = tk.Checkbutton(
        Fenster_Frage5, text="Argentinien", variable=TickBox_20, onvalue=1, offvalue=0)
    Checkbutton_20.pack()
    Button_für_Ende = tk.Button(Fenster_Frage5, text="Prüfen", command=lambda: functions6(
        # Erstellen eines Buttons um das Programm zu schließen & Fenster 5 zu schließen
        Fenster_Frage5, TickBox_17, TickBox_18, TickBox_19, TickBox_20))
    Button_für_Ende.pack()


def aktionbutton_7():  # Schluss Fenster
    Fenster_Schluss = tk.Toplevel(root)
    Fenster_Schluss.title("Schluss")
    Fenster_Schluss.geometry("800x450")
    label_Schluss = tk.Label(
        Fenster_Schluss, text="Super, du hast alle Fragen richtig beantwortet!")
    label_Schluss.pack()
    label_Schluss_2 = tk.Label(
        Fenster_Schluss, text="Vielen Dank fürs Mitmachen & alles gute Nachträglich von GPT-4o")
    button_Schließen = tk.Button(
        Fenster_Schluss, text="Schließen", command=root.quit)  # Schließt Programm
    button_Schließen.pack()


def functions():
    aktionbutton_1_2()


label1 = tk.Label(root, text="Willkommen zum schwierigsten Allgemeinwissen Quiz der Welt. Hast du Lust?",
                  fg="white", bg="grey")  # Erstellen eines Labels; mit fg Textfarbe anpassen
label1.pack()

Button_1 = tk.Button(root, text="Ja ich hab mega Bock",
                     bg="grey", command=functions)
Button_1.pack()

Button_2 = tk.Button(root, text="Ne, aber mach ich trotzdem",
                     bg="grey", command=functions)
Button_2.pack()

Button_3 = tk.Button(root, text="Ne, heute wirklich nicht", bg="grey",
                     command=lambda: aktionbutton_3(root))  # Schließt Programm
Button_3.pack()

root.mainloop()
