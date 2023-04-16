import wave
import pyaudio
import subprocess


def play(file_name):
    # 打开WAV文件
    with wave.open(file_name, 'rb') as wav_file:
        # 创建PyAudio对象
        py_audio = pyaudio.PyAudio()
        # 打开PyAudio输出流
        stream = py_audio.open(format=py_audio.get_format_from_width(wav_file.getsampwidth()),
                                channels=wav_file.getnchannels(),
                                rate=wav_file.getframerate(),
                                output=True)
        # 播放数据
        data = wav_file.readframes(1024)
        while data:
            stream.write(data)
            data = wav_file.readframes(1024)
        # 关闭流
        stream.close()
        py_audio.terminate()


# 调整音频播放速率
def a_speed(input_file, speed, out_file):
    try:
        cmd = "ffmpeg -loglevel quiet -y -i %s -filter_complex \"atempo=tempo=%s\" %s" % (input_file, speed, out_file)
        res = subprocess.call(cmd, shell=True)

        if res != 0:
            return False
        return True
    except Exception:
        return False


# 调整音频channel和HZ为16k 1channel
def a_hz(input_file, out_file):
    try:
        cmd = "ffmpeg -y -i %s -ac 1 -ar 16000 -vn %s" % (input_file, out_file)
        res = subprocess.call(cmd, shell=True)
        if res != 0:
            return False
        return True
    except Exception:
        return False