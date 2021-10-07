from google_trans_new import google_translator  
translator = google_translator()  
translate_text = translator.translate('how are you',lang_tgt='hi')  
print(translate_text)