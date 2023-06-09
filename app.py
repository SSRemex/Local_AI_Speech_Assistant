from flask import Flask, request, jsonify, render_template
from sound_generic import sound_create
from audio_play import a_speed
from config import HISTORY, wav_output_dir, source_wav_filename, a_speed_wav_filename, speed
from chat import chat
from sound_recognition import sound_to_text
import time


app = Flask(__name__, static_folder="templates/static")

source_history = HISTORY


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/upload_wav", methods=["POST"])
def upload_wav():

    global source_history
    # 获取上传的文件对象
    file = request.files.get("audio")

    # 将文件保存到服务器
    file.save(wav_output_dir + 'record_upload.wav')
    try:
        source_message = sound_to_text()
    except AssertionError as e:
        return jsonify(error="未检测到内容")
    sentence, history = chat(source_message, history=source_history)
    source_history = history
    sentence_format = sentence.replace("\n", " ").replace(",", "，").replace(".", "。")
    sound_create(sentence_format)
    a_speed(wav_output_dir + source_wav_filename, speed, wav_output_dir + a_speed_wav_filename)

    return jsonify(source_message=source_message, response=sentence,
                   audio=a_speed_wav_filename, time_id=int(time.time()), error="")


@app.route('/chat', methods=['POST'])
def chat_api():
    global source_history
    data = request.json
    message = data.get("text")
    sentence, history = chat(message, history=source_history)
    source_history = history
    sentence = sentence.replace("\n", "").replace(",", "，").replace(".", "。")
    sound_create(sentence)
    a_speed(wav_output_dir + source_wav_filename, speed, wav_output_dir + a_speed_wav_filename)

    return jsonify(response=sentence, audio=a_speed_wav_filename, time_id=int(time.time()))


if __name__ == '__main__':
    app.run("127.0.0.1", port=9995, debug=True)


