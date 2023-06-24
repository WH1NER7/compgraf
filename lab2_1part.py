from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

# Количество сторон для многоугольника и круга
num_sides = 50
num_sides_polygon = 6


def draw_square():
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()


def draw_polygon():
    radius = 0.5
    angle = (2 * math.pi) / num_sides_polygon

    glBegin(GL_POLYGON)
    for i in range(num_sides_polygon):
        x = radius * math.cos(i * angle)
        y = radius * math.sin(i * angle)
        glVertex2f(x, y)
    glEnd()


def draw_circle():
    radius = 0.5
    angle = (2 * math.pi) / num_sides

    glBegin(GL_POLYGON)
    for i in range(num_sides):
        x = radius * math.cos(i * angle)
        y = radius * math.sin(i * angle)
        glVertex2f(x, y)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Рисование квадрата
    glPushMatrix()
    glTranslatef(-0.5, 0.5, 0.0)
    glColor3f(1.0, 0.0, 0.0)  # Красный цвет
    draw_square()
    glPopMatrix()

    # Рисование многоугольника
    glPushMatrix()
    glTranslatef(0.5, 0.5, 0.0)
    glColor3f(0.0, 1.0, 0.0)  # Зеленый цвет
    draw_polygon()
    glPopMatrix()

    # Рисование круга
    glPushMatrix()
    glTranslatef(0.0, -0.5, 0.0)
    glColor3f(1.0, 1.0, 0.0)  # Желтый цвет
    draw_circle()
    glPopMatrix()

    glFlush()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"OpenGL Shapes")

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glutMainLoop()


if __name__ == "__main__":
    main()
