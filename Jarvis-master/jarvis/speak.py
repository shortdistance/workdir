import pyttsx

voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0'
def speak_out(words):
    engine = pyttsx.init()
    engine.setProperty('voice', voice_id)
    engine.say(words)
    engine.runAndWait()
    engine.endLoop()


engine = pyttsx.init()
voices = engine.getProperty('voices')
for voice in voices:
    print voice.id
    engine.setProperty('voice', voice.id)
    engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()