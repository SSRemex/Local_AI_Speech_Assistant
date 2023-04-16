import paddle
from paddlespeech.cli.asr import ASRExecutor
from paddlespeech.cli.text import TextExecutor
from audio_play import a_hz
from config import wav_output_dir, record_16k_filename, record_upload_filename

asr_executor = ASRExecutor()
text_executor = TextExecutor()


def sound_to_text():
    input_file = wav_output_dir + record_upload_filename
    output_file = wav_output_dir + record_16k_filename

    a_hz(input_file, output_file)
    text = asr_executor(
        audio_file=output_file,
        device=paddle.get_device(),
        force_yes=True
    )
    result = text_executor(
        text=text,
        task='punc',
        model='ernie_linear_p3_wudao',
        device=paddle.get_device())
    return result


# 第一次运行语音转文字比较慢，所以这里初始化调用一下来加速
# 请确保output_wav文件夹下有16k_record_upload.wav文件
sound_to_text()
