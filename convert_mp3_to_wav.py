from pydub import AudioSegment


def mp3_to_wav(mp3_file, wav_file):
    """
    将 MP3 文件转换为 WAV 文件。

    :param mp3_file: 输入的 MP3 文件路径
    :param wav_file: 输出的 WAV 文件路径
    """
    # 加载 MP3 文件
    audio = AudioSegment.from_mp3(mp3_file)

    # 导出为 WAV 文件
    audio.export(wav_file, format="wav")
    print(f"转换完成：{mp3_file} -> {wav_file}")


if __name__ == "__main__":
    # 示例文件路径
    input_mp3_file = "/Users/tal/Desktop/convert_mp3_to_wav/leiqian.mp3"
    output_wav_file = "/Users/tal/Desktop/convert_mp3_to_wav/test_audio.wav"

    # 调用转换函数
    mp3_to_wav(input_mp3_file, output_wav_file)
