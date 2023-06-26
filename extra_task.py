from OpenGL.GL import *
from OpenGL.GLUT import *
from PIL import Image


def load_image_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Удаляем символы перевода строки
    lines = [line.rstrip('\r\n') for line in lines]

    # Преобразование строк в список байтовых значений
    image_data = [int(char) for line in lines for char in line]
    # print(image_data)
    return image_data


def create_bitmap_image(image_data, width, height):
    # Создание пустого изображения
    image = Image.new('RGB', (width, height), 'white')
    pixels = image.load()

    # Установка цвета пикселей в соответствии с данными изображения
    for y in range(height):
        for x in range(width):
            pixel_value = image_data[y * width + x]
            color = (0, 0, 0) if pixel_value == 1 else (255, 255, 255)
            pixels[x, y] = color

    return image


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Отображение изображения с использованием glDrawPixels
    glRasterPos2f(-1, -1)
    glDrawPixels(image.width, image.height, GL_RGB, GL_UNSIGNED_BYTE, image.tobytes())

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(image.width, image.height)
    glutCreateWindow(b"PyOpenGL Example")

    glutDisplayFunc(display)

    glutMainLoop()


if __name__ == "__main__":
    # Загрузка данных из файла
    image_data = load_image_data("input.txt")

    # Вычисление ширины и высоты изображения
    width = 255
    height = len(image_data) // width

    # Создание битмап-изображения
    image = create_bitmap_image(image_data, width, height)

    main()
