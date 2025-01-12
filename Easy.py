from gtts import gTTS
import os

# Ввод текста
text = "Привет! Это пример перевода текста в речь."

# Создание аудиофайла
tts = gTTS(text, lang="ru")
tts.save("output.mp3")

# Воспроизведение аудио (опционально)
os.system("start output.mp3")  # Для Windows
# os.system("open output.mp3")  # Для macOS



