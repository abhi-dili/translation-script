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
   
    with open('english.json') as f:
        json_data = json.load(f)
        count = 0
        for key, value in json_data.items():
            # translated_data[key] = value

            # if '_#######' in value:
            if value:
                try:
                    # translated_re = translate(value.replace('_#######',''), traget_lag)
                    translated_re = translate(value, traget_lag)
                    translated_data[key] = translated_re[0]
                    print(translated_re[0])
                except:
                    translated_data[key] = value+'_#######'
                    print('error')


            
            count += 1
        print(count)
    with open(f'out/{traget_lag}.json', 'w') as file:
        file.write(json.dumps(translated_data))

traget_lag = str(sys.argv[1])
translate_english_words(traget_lag)

















# from google_trans_new import google_translator  
# import csv
# import sys 
# import json
# translator  = google_translator()  
# import time
# import pyautogui

# def translate(text_in:str, traget_lag:str):
#     """
#     trnslate words from source to destination..

#     """
#     return translator.translate(
#                 text_in, 
#                 lang_src='en', 
#                 lang_tgt=traget_lag, 
#                 pronounce=True
#             )

# def translate_english_words(traget_lag):
        
#     """
#     Output:- english text : translate langauge
#     """

#     translated_data = {}
#     with open('out/kotest_final.json') as f:
#         json_data_new = json.load(f)

#     with open('out/ko2.json') as f:
#         json_data = json.load(f)
#         count = 0
#         for key, value in json_data_new.items():
#             if value == '#######':
#                 try:
#                     data_d = json_data[key]
#                     json_data_new[key] = data_d
#                     # translated_re = translate(data_d, traget_lag)
#                     # translated_data[key] = translated_re[0]
#                     # print(translated_re[0])
#                 except:
#                     translated_data[key] = '#######'
#                     print('error')


            
#             count += 1
#         print(count)
#     with open(f'out/{traget_lag}test_final.json', 'w') as file:
#         file.write(json.dumps(json_data_new))

# traget_lag = str(sys.argv[1])
# translate_english_words(traget_lag)