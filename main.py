import pyautogui
import time
import random
from datetime import datetime

# Настройка: отключаем аварийное завершение при ударе об угол (опционально)
pyautogui.FAILSAFE = False

print("=== Anti-Sleep Запущен ===")
print("Нажми Ctrl+C в консоли, чтобы остановить скрипт.")

try:
    while True:
        # Генерируем случайное смещение (от -5 до 5 пикселей)
        x_move = random.randint(-5, 5)
        y_move = random.randint(-5, 5)

        # Двигаем мышь относительно текущего положения
        pyautogui.moveRel(x_move, y_move)

        # Выводим время последнего движения (чтобы видеть, что скрипт жив)
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"[{current_time}] Курсор сдвинут на {x_move}, {y_move}")

        # Ждем 60 секунд перед следующим движением
        time.sleep(60)

except KeyboardInterrupt:
    print("\nСкрипт остановлен пользователем.")