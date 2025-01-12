import pyttsx3

# Инициализация движка
engine = pyttsx3.init()

# Настройка параметров
engine.setProperty('rate', 150)  # Скорость речи
engine.setProperty('volume', 0.9)  # Громкость (0.0 - 1.0)

# Установка голоса (если есть русские голоса)
voices = engine.getProperty('voices')
for voice in voices:
    if "Russian" in voice.name:
        engine.setProperty('voice', voice.id)
        break

# Текст для преобразования
text = "Привет! Это пример перевода текста в речь на русском языке."

# Генерация речи
engine.say(text)
engine.runAndWait()





