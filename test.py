from google_trans_new import google_translator  
import csv
import sys 
import json
translator  = google_translator()  
import time
import pyautogui

def translate(text_in:str, traget_lag:str):
    """
    trnslate words from source to destination..

    """
    return translator.translate(
                text_in, 
                lang_src='en', 
                lang_tgt=traget_lag, 
                pronounce=True
            )

def translate_english_words(traget_lag):
        
    """
    Output:- english text : translate langauge
    """

    translated_data = {}
    json_data = {"request":"Request"}
    for key, value in json_data.items():
   
        try:
            translated_re = translate(value, traget_lag)
            translated_data[key] = translated_re[0]
            print(translated_re[0])
        except:
            translated_data[key] = ''
    print(translated_data)
 
traget_lag = str(sys.argv[1])
translate_english_words(traget_lag)