import subprocess
import datetime

# Запускаем команду ps aux и сохраняем вывод в переменную output
output = subprocess.check_output(['ps', 'aux'])

# Преобразуем вывод в список строк
output_lines = output.decode().split('\n')

# Создаём словарь для хранения количества процессов по
users_processes = {}

# Инициализируем переменные для общего количества процессов, памяти и CPU
total_processes = 0
total_memory_percent = 0.0
total_cpu_percent = 0.0
max_memory_percent = 0.0
max_cpu_percent = 0.0
max_memory_process_name = ""
max_cpu_process_name = ""

# Итерируемся по строкам вывода ps aux
for line in output_lines[1:]:
    # Игнорируем пустые строки
    if not line:
        continue

    # Разбиваем строку по пробелам
    parts = line.split()

    # Получаем имя пользователя
    user = parts[0]

    # Получаем коkличество процессов для пользователя
    processes = users_processes.get(user, 0)
    users_processes[user] = processes + 1

    # Получаем процент использования памяти и CPU
    memory_percent = float(parts[3])
    cpu_percent = float(parts[2])

    # Добавляем процент использования памяти и CPU к общим значениям
    total_memory_percent += memory_percent
    total_cpu_percent += cpu_percent

    # Если текущий процесс использует больше памяти, сохраняем его данные
    if memory_percent > max_memory_percent:
        max_memory_percent = memory_percent
        max_memory_process_name = parts[10][:20]

    # Если текущий процесс использует больше CPU, сохраняем его данные
    if cpu_percent > max_cpu_percent:
        max_cpu_percent = cpu_percent
        max_cpu_process_name = parts[10][:20]

    # Увеличиваем общее количество процессов
    total_processes += 1

# Выводим результаты в консоль
print("Отчёт о состоянии системы:")
print("Пользователи системы:", list(users_processes.keys()))
print("Процессов запущено:", total_processes)
print("Пользовательских процессов:")
for user, processes in users_processes.items():
    print(user + ":", processes)
print("Всего памяти используется: %.1f%%" % total_memory_percent)
print("Всего CPU используется: %.1f%%" % total_cpu_percent)
print("Больше всего памяти использует:", "(%.1f%%, %s)" % (max_memory_percent, max_memory_process_name))
print("Больше всего CPU использует:", "(%.1f%%, %s)" % (max_cpu_percent, max_cpu_process_name))

# Создаём имя файла для сохранения отчёта
filename = datetime.datetime.now().strftime("%d-%m-%Y-%H:%M") + "-scan.txt"

# Открываем файл для записи
with open(filename, "w") as f:
    # Записываем результаты в файл
    f.write("Отчёт о состоянии системы:\n")
    f.write("Пользователи системы: " + str(list(users_processes.keys())) + "\n")
    f.write("Процессов запущено: " + str(total_processes) + "\n")
    f.write("Пользовательских процессов:\n")
    for user, processes in users_processes.items():
        f.write(user + ": " + str(processes) + "\n")
    f.write("Всего памяти используется: %.1f%%\n" % total_memory_percent)
    f.write("Всего CPU используется: %.1f%%\n" % total_cpu_percent)
    f.write("Больше всего памяти использует: (%.1f%%, %s)\n" % (max_memory_percent, max_memory_process_name))
    f.write("Больше всего CPU использует: (%.1f%%, %s)\n" % (max_cpu_percent, max_cpu_process_name))

# Выводим сообщение о завершении работы
print("Отчёт сохранён в файле:", filename)
