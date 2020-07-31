#-*- coding:utf-8 -*-

from tkinter import *
import random

boardWidth = 60
boardHeight = 60

class Snake():

    def __init__(self):
        self.snakeX = [20, 20, 20]
        self.snakeY = [20,21,22]
        self.snakeLength = 1
        self.key = ""
        self.points = 0

    def move(self):
        for i in range(self.snakeLength - 1, 0, -1):
            self.snakeX[i] = self.snakeX[i-1]
            self.snakeY[i] = self.snakeY[i-1]

        if self.key == "w":
           self.snakeY[0] = self.snakeY[0] - 1
        elif self.key == "s":
            self.snakeY[0] = self.snakeY[0] + 1
        elif self.key == "a":
            self.snakeX[0] = self.snakeX[0] - 1
        elif self.key == "d":
            self.snakeX[0] = self.snakeX[0] + 1

        self.comerManzana()

    def comerManzana(self):
        if self.snakeX[0] == manzana.getAppleX() and self.snakeY[0] == manzana.getAppleY():
            self.snakeLength += 1

            x = self.snakeX[len(self.snakeX) - 1]
            y = self.snakeY[len(self.snakeY) - 1]
            self.snakeX.append(x + 1)
            self.snakeY.append(y)

            self.points += 1
            manzana.crearManzana()


    def verificarPerder(self):
        for i in range(1, self.snakeLength, 1):
            if self.snakeY[0] == self.snakeY[i] and self.snakeX[0] == self.snakeX[i]:
                return True
        if self.snakeX[0] < 1 or self.snakeX[0] >= boardWidth - 1 or self.snakeY[0] < 1 or self.snakeY[0] >= boardHeight - 1:
            return True

        return False

    def getKey(self, event):

        if event.char == "w" or event.char == "d" or event.char == "s" or event.char == "a" or event.char == " ":
            self.key = event.char

    def getSnakeX(self, index):
        return self.snakeX[index]

    def getSnakeY(self, index):
        return self.snakeY[index]

    def getSnakeLength(self):
        return self.snakeLength

    def getPoints(self):
        return self.points

class Manzanas:
    def __init__(self):
        self.appleX = random.randint(1, boardWidth - 2)
        self.appleY = random.randint(1, boardHeight - 2)

    def getAppleX(self):
        return self.appleX

    def getAppleY(self):
        return self.appleY

    def crearManzana(self):
        self.appleX = random.randint(1, boardWidth - 2)
        self.appleY = random.randint(1, boardHeight - 2)

class Principal:
    def pintar(self):
        canvas.after(70, self.pintar)
        canvas.delete(ALL)

        if serpierte.verificarPerder() == False:

            serpierte.move()
            serpierte.verificarPerder()

            canvas.create_oval(serpierte.getSnakeX(0) * 10, serpierte.getSnakeY(0) * 10, serpierte.getSnakeX(0) * 10 + 10, serpierte.getSnakeY(0) * 10 + 10, fill = "#00FF00")

            for i in range(1, serpierte.getSnakeLength(), 1):
                canvas.create_oval(serpierte.getSnakeX(i) * 10, serpierte.getSnakeY(i) * 10, serpierte.getSnakeX(i) * 10 + 10, serpierte.getSnakeY(i) * 10 + 10, fill = "#85FF85")

            canvas.create_rectangle(manzana.getAppleX() * 10, manzana.getAppleY() * 10, manzana.getAppleX() * 10 + 10, manzana.getAppleY() * 10 + 10, fill = "#FF0000")

            valor_puntos.set("Puntos = " + str(serpierte.getPoints()))
        else:
            canvas.delete(ALL)
            canvas.create_text(300, 200, fill = "#fff", font = "Arial 40 bold", text = "Fin del Juego")
            canvas.create_text(300, 300, fill = "#fff", font = "Arial 40 bold", text = "Puntaje = " + str(serpierte.getPoints()))

if __name__ == '__main__':

    serpierte = Snake()
    manzana = Manzanas()

    root = Tk()
    root.title("Juego Snake")
    root.geometry("600x610")
    root.resizable(0, 0)

    root.call("wm", "iconphoto", root._w, PhotoImage(file = "/home/yirsis/Escritorio/Juegos/favicon.png"))

    valor_puntos = StringVar()

    puntos = Label(root, text = "Puntaje: " + str(serpierte.getPoints()), textvariable = valor_puntos)
    puntos.pack()

    canvas = Canvas(root, width = 600, height = 600, bg = "#111")
    canvas.pack(expand = YES, fill = BOTH)

    arrancar = Principal()
    arrancar.pintar()

    root.bind("<KeyPress>", serpierte.getKey)
    root.mainloop()

