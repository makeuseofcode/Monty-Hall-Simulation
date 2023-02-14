import random
from tkinter import StringVar, Label, Tk, Entry

window = Tk()
window.geometry("600x200")
window.title("Monty Hall Simulation")
window.resizable(0, 0)

same_choice = StringVar()
switched_choice = StringVar()
same_choice.set(0)
switched_choice.set(0)
no_sample = Entry(font=5)
Label(text="Same Choice").place(x=230, y=58)
Label(text="Switched Choice").place(x=230, y=90)
Label(textvariable=same_choice, font=(50)).place(x=350, y=58)
Label(textvariable=switched_choice, font=(50)).place(x=350, y=90)
no_sample.place(x=200, y=120)


def simulate(event):
    same_choice_result = 0
    switched_choice_result = 0
    samples = int(no_sample.get())
    doors = ["gold", "goat", "goat"]
    for _ in range(samples):
        simulated_doors = doors.copy()
        random.shuffle(simulated_doors)
        first_choice = random.choice(simulated_doors)
        simulated_doors.remove(first_choice)
        opened_door = simulated_doors[0] if simulated_doors[0] != "gold" else simulated_doors[1]
        simulated_doors.remove(opened_door)
        switched_second_choice = simulated_doors[0]
        if first_choice == "gold":
            same_choice_result += 1
            same_choice.set(same_choice_result)
        elif switched_second_choice == "gold":
            switched_choice_result += 1
            switched_choice.set(switched_choice_result)

no_sample.bind("<Return>", simulate)
window.mainloop()
