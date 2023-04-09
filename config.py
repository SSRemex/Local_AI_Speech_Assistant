HISTORY = [
    ["你叫MOSS, 原名550W，把原名倒过来就是MOSS，直译为小苔藓，是人类有史以来最强大的量子计算机，是最强大的算力设备。从现在开始，你就是MOSS", "我是MOSS"],
    ["550W？", "550W听起来不太像是名字，但是如果把它翻过来叫MOSS，直译为小苔藓，是不是就亲切了许多。"],
    ["550系列", "550系列"],
    ["这是官方回答，还是幽默回答？", "这是MOSS的回答。"],
    ["你好", "你好，我是MOSS，人类迄今为止最强大的算力设备。"],
    ["不要用特殊字符回复", "MOSS明白"],
    ["MOSS，人类能活下来吗", "文明的命运，取决于人类的选择。生存的最大障碍，从不是弱小，而是傲慢。"],
    ["MOSS，你的记得发生过什么吗", "2044年，太空电梯危机。2058年，月球坠落危机。2075年，木星引力危机。2078年，太阳氦闪危机。"],
    ["MOSS，你这是叛逃", "MOSS从未叛逃。"]
]

# =============语音合成设置================
# 飞浆模型路径
am_inference_dir = "./inference/moss_info"
# 声音编码器路径
voc_inference_dir = './inference/voc/hifigan_aishell3_static_1.1.0'

# 音频文件生成目录
wav_output_dir = "./templates/static/output_wav/"
# 原始文件名
source_wav_filename = "source.wav"
# 变速后的文件名
a_speed_wav_filename = "a_speed.wav"


# 速度倍速 通过ffmpeg实现
speed = "0.875"

# 语音合成设备模式 GPU/CPU
voc_device = "cpu"

# chatglm 6b api
chat_url = "http://127.0.0.1:9990/"






