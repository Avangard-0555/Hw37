from flask import Flask, render_template, request, send_file
from gtts import gTTS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # HTML-шаблон интерфейса

@app.route('/synthesize', methods=['POST'])
def synthesize():
    # Получение текста и языка из формы
    text = request.form['text']
    lang = request.form['language']
    
    if not text.strip():
        return "Ошибка: текст не может быть пустым!"

    # Генерация речи
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    
    # Возврат файла пользователю
    return send_file("output.mp3", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)


