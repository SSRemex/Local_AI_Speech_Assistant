import soundfile as sf
import os
from paddlespeech.t2s.exps.syn_utils import get_am_output
from paddlespeech.t2s.exps.syn_utils import get_frontend
from paddlespeech.t2s.exps.syn_utils import get_predictor
from paddlespeech.t2s.exps.syn_utils import get_voc_output

from config import am_inference_dir, voc_inference_dir, wav_output_dir, voc_device, source_wav_filename


def sound_create(sentence):
    # frontend
    frontend = get_frontend(
        lang="mix",
        phones_dict=os.path.join(am_inference_dir, "phone_id_map.txt"),
        tones_dict=None
    )

    # am_predictor
    am_predictor = get_predictor(
        model_dir=am_inference_dir,
        model_file="fastspeech2_mix" + ".pdmodel",
        params_file="fastspeech2_mix" + ".pdiparams",
        device=voc_device)

    # voc_predictor 生编码器
    voc_predictor = get_predictor(
        model_dir=voc_inference_dir,
        model_file="hifigan_aishell3" + ".pdmodel",
        params_file="hifigan_aishell3" + ".pdiparams",
        device=voc_device)

    merge_sentences = True
    fs = 24000

    am_output_data = get_am_output(
        input=sentence,
        am_predictor=am_predictor,
        am="fastspeech2_mix",
        frontend=frontend,
        lang="mix",
        merge_sentences=merge_sentences,
        speaker_dict=os.path.join(am_inference_dir, "phone_id_map.txt"),
        spk_id=0, )
    wav = get_voc_output(
            voc_predictor=voc_predictor, input=am_output_data)
    # 保存文件
    file_name = wav_output_dir + source_wav_filename
    sf.write(file_name, wav, samplerate=fs)


if __name__ == '__main__':
    sound_create("你好")

