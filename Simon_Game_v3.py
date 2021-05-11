from tkinter import *
import random


class SimonGame:
    blinking_sequence = []
    pattern_list = []
    user_pattern = []

    colors = ['green', 'red', 'yellow', 'blue']
    flash_color = ['white']

    var2 = ''
    score = 0
    x = 0
    y = 0

    def __init__(self):
        self.root = Tk()
        self.root.configure(bg='black')
        self.root.title('Simon Game')
        self.root.resizable(False, False)

        self.scoreboard = Label(self.root, text="Score : {}".format(self.score), height=3, font=10, bg='black',
                                fg='white')
        self.scoreboard.grid(row=0, column=2)

        g = Button(self.root, height=13, width=28, bg='green', bd=20, command=self.green)
        g.grid(row=1, column=1)

        r = Button(self.root, height=13, width=28, bg='red', bd=20, command=self.red)
        r.grid(row=1, column=2)

        y = Button(self.root, height=13, width=28, bg='yellow', bd=20, command=self.yellow)
        y.grid(row=2, column=1)

        b = Button(self.root, height=13, width=28, bg='blue', bd=20, command=self.blue)
        b.grid(row=2, column=2)

        self.myButtons = [g, r, y, b]

    def green(self):
        print('green')
        self.check(color='green')

    def red(self):
        print('red')
        self.check(color='red')

    def yellow(self):
        print('yellow')
        self.check(color='yellow')

    def blue(self):
        print('blue')
        self.check(color='blue')

    def add_to_pattern(self):
        rand_color = random.choice(self.colors)
        self.pattern_list.append(rand_color)
        self.x = 0
        self.y = 0

        if rand_color == 'green':
            self.blinking_sequence.append(self.myButtons[0])

        elif rand_color == 'red':
            self.blinking_sequence.append(self.myButtons[1])

        elif rand_color == 'yellow':
            self.blinking_sequence.append(self.myButtons[2])

        elif rand_color == 'blue':
            self.blinking_sequence.append(self.myButtons[3])

        self.highlight_sequence()
        print(self.pattern_list)

    def check(self, color):
        for i in range(len(self.pattern_list)):
            print(i)
            if color == self.pattern_list[self.x]:
                print('Correct')
            else:
                self.game_over()
        self.x += 1
        if len(self.pattern_list) == self.x:
            print('executed')
            self.update_scoreboard()

    def update_scoreboard(self):
        self.score = self.score + 1
        self.scoreboard['text'] = "Score : {}".format(self.score)
        self.add_to_pattern()

    def game_over(self):
        self.x = 0
        self.y = 0
        self.scoreboard['text'] = "Final score : {}".format(self.score)
        l1 = Label(self.root, text="GAME OVER!", height=3, font=10, bg='black', fg='red')
        l1.grid(row=0, column=1)
        for i in self.myButtons:
            i.configure(state=DISABLED)
            i.configure(bg='black')

    def highlight_sequence(self):
        self.blinking_sequence[self.y].configure(bg='white')
        self.root.after(700, self.highlight_off)

    def highlight_off(self):
        button_colors = zip(self.myButtons, self.colors)
        for b, c in button_colors:
            b.configure(bg=c)
        self.y += 1
        self.root.after(200, self.highlight_sequence)

    def start(self):
        self.add_to_pattern()
        self.root.mainloop()


if __name__ == '__main__':
    simon = SimonGame()
    simon.start()
