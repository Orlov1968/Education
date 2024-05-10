import os
from datetime import time
import time

directory = "C:\\Users\\ASUS\\Downloads"
for dirpath, dirnames, filenames in os.walk(directory):
    for file in filenames:
        file_path = os.path.join(dirpath, file)
        file_time = os.path.getmtime(file_path)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
        file_size = os.path.getsize(file_path)
        parent_dir = os.path.dirname(file_path)
        print(f"Обнаружен файл: {file} , Путь: {file_path}, Размер: {file_size} байт," 
              f"Время изменения {formatted_time}, Родительская директория {parent_dir} ")
