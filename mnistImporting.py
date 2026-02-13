import numpy as np
import matplotlib.pyplot as plt
import cv2


class mnist_binarization:
    def load_mnist():
        path = 'mnist.npz'
        # path = 'mnist_filtered.npz'
        with np.load(path) as data:
            x_train = data['x_train']
            y_train = data['y_train']
            x_test = data['x_test']
            y_test = data['y_test']
        return (x_train, y_train), (x_test, y_test)

    def prepare_mnist_data(images, labels, threshold=50, start_index=0, samples_count=1, type_labels=[1,2,3,4,5]):
        # Создаем маску для выбранных меток и индексов
        final_mask = np.zeros_like(labels, dtype=bool)
        
        for label in type_labels:
            # Находим все вхождения текущей метки
            label_mask = (labels == label)
            available_indices = np.where(label_mask)[0]
            
            # Выбираем диапазон индексов с учетом START_INDEX и SAMPLES_PER_CLASS
            selected_indices = available_indices[
                start_index : start_index + samples_count
            ]
            
            # Обновляем общую маску
            final_mask[selected_indices] = True

        # Применяем маску
        selected_images = images[final_mask]
        selected_labels = labels[final_mask]
        
        # Бинаризация и обработка
        binary_images = (selected_images < threshold).astype(np.uint8) * 255
        binary_images = 255 - binary_images
        
        # Морфологическая обработка
        kernel = np.ones((2,2), np.uint8)
        for i in range(binary_images.shape[0]):
            binary_images[i] = cv2.morphologyEx(
                binary_images[i], cv2.MORPH_OPEN, kernel
            )
        
        # Конвертация в формат 0/1
        binary_images = (binary_images > 0).astype(int)
        
        return binary_images, selected_labels