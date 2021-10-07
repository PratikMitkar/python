from google_trans_new import google_translator  
import gtts
import os

translator = google_translator()  

translate_text = translator.translate('how are you',lang_tgt='mr')  


t1 = gtts.gTTS(text= translate_text, lang= 'hi', slow=False)  

t1.save("welcome.mp3")   

os.system("start welcome.mp3")
