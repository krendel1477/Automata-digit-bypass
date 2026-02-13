from mnistImporting import mnist_binarization
# from maze import Maze
from algorithm import Algorithm

# ===================== НАСТРОЙКИ ВЫБОРКИ =====================
DESIRED_LABELS = [5]  # Какие цифры выбираем
SAMPLES_PER_CLASS = 1            # Примеров на каждый класс
START_INDEX = 0                  # Стартовый индекс выборки
# =============================================================

if __name__ == "__main__":
    (x_train, y_train), (x_test, y_test) = mnist_binarization.load_mnist()
    
    images, labels = x_train, y_train
    
    # Подготавливаем данные
    binary_images, prepared_labels = mnist_binarization.prepare_mnist_data(images, labels, 50, 
                                            START_INDEX, SAMPLES_PER_CLASS, DESIRED_LABELS)
    
    count_of_iterations = 50


    # print(len(y_train))
    # Обработка и визуализация
    counter = 0
    for i, (img, label) in enumerate(zip(binary_images, prepared_labels)):
        result = Algorithm.process_mnist_digit(img, label, DESIRED_LABELS, count_of_iterations)
        num = result["info"]
        if (num == label):
            counter += 1
        # print(f"Эта цифра является {num}-й: {'цифра определена' if result['exit_found'] else 'цифра не определена'}\n")
    print(f"Точность:{counter/(SAMPLES_PER_CLASS*5)}")
    counter = 0
    for i, (img, label) in enumerate(zip(binary_images, prepared_labels)):
        result = Algorithm.process_mnist_digit(img, label, DESIRED_LABELS, count_of_iterations)
        num = result
        if (num == True):
            counter += 1
        # print(f"Эта цифра является {num}-й: {'цифра определена' if result['exit_found'] else 'цифра не определена'}\n")
    print(f"Точность:{counter/(SAMPLES_PER_CLASS)}")