from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_julia_fractal():
    # Устанавливаем размер окна
    width, height = 800, 800

    # Инициализация библиотеки GLUT и создание окна
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Julia Fractal")

    # Устанавливаем функцию отрисовки
    glutDisplayFunc(draw)

    # Устанавливаем начальное состояние OpenGL
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-2.0, 2.0, -2.0, 2.0)

    # Запускаем главный цикл GLUT
    glutMainLoop()


def draw():
    # Очищаем буфер цвета
    glClear(GL_COLOR_BUFFER_BIT)

    # Устанавливаем цвет
    glColor3f(1.0, 1.0, 1.0)

    # Задаем параметры фрактала Жюлиа
    c = complex(-0.8, 0.156)
    max_iterations = 100

    # Рисуем фрактал Жюлиа
    for x in range(-400, 400):
        for y in range(-400, 400):
            z = complex(x / 200.0, y / 200.0)
            iteration = 0
            while abs(z) < 2 and iteration < max_iterations:
                z = z * z + c
                iteration += 1

            # Определяем цвет пикселя в зависимости от числа итераций
            brightness = 1 - iteration / max_iterations
            glColor3f(brightness, brightness, brightness)

            # Рисуем пиксель
            glBegin(GL_POINTS)
            glVertex2f(x / 400.0, y / 400.0)
            glEnd()

    # Отображаем отрисованное содержимое
    glutSwapBuffers()


# Запускаем отрисовку фрактала Жюлиа
draw_julia_fractal()
