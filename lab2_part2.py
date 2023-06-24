import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Инициализация Pygame
pygame.init()
width, height = 800, 600
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

# Настройка OpenGL
glViewport(0, 0, width, height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0, width, 0, height)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Параметры многоугольника
vertices = np.array([[100, 100], [200, 100], [200, 200], [100, 200]], dtype=np.float32)
center = np.mean(vertices, axis=0)
scale = 1.0
angle = 0.0
curve_scale = 0.005

clock = pygame.time.Clock()


# Функция для рисования многоугольника
def draw_polygon():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glTranslate(center[0], center[1], 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)
    glScalef(scale, scale, 1.0)
    glTranslate(-center[0], -center[1], 0.0)

    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex2fv(vertex)
    glEnd()

    pygame.display.flip()


# Главный цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Изменение масштаба
    scale += 0.01
    if scale > 2.0:
        scale = 1.0

    # Вращение вокруг заданной точки
    angle += 1.0
    if angle > 360.0:
        angle = 0.0

    # Анимированное движение по кривой
    t = pygame.time.get_ticks() * curve_scale
    x = 300 + np.cos(t) * 200
    y = 300 + np.sin(t) * 200
    center = np.array([x, y], dtype=np.float32)

    draw_polygon()
    clock.tick(60)
