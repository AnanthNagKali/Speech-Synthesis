from gtts import gTTS
from playsound import playsound
audio="speech.mp3"
language='en'
sp=gTTS(text="we are getting a bike soon because we lost our old one we are planning to buy continental gt650",lang=language,slow=False)
sp.save(audio)
playsound(audio)
print("Use headphones for better sound ")

