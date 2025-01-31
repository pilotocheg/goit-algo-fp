import turtle
import math


def draw_pythagoras_tree(t, length, level):
    if level == 0:
        return

    # Малюємо основний стовбур
    t.forward(length)
    t.left(45)

    # Ліва гілка
    draw_pythagoras_tree(t, length / math.sqrt(2), level - 1)

    t.right(90)

    # Права гілка
    draw_pythagoras_tree(t, length / math.sqrt(2), level - 1)

    t.left(45)
    t.backward(length)


def main():
    try:
        level = int(input("Введіть рівень рекурсії: "))

        if level <= 0:
            raise ValueError("Рівень рекурсії має бути більше 0")
    except:
        print("Рівень рекурсії має бути цілим числом")
        return

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)  # Повертаємо черепаху вгору
    t.up()
    t.goto(0, -200)
    t.down()

    draw_pythagoras_tree(t, 100, level)

    screen.mainloop()


if __name__ == "__main__":
    main()
