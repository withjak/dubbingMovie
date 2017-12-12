from gtts import gTTS


def sub_to_audio(sub):
    print(sub.text)

    tts = gTTS(text=sub.text, lang='en')
    tts.save("op.mp3")
