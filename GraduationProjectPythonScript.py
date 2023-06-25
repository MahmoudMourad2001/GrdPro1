from flask import Flask, jsonify
app = Flask(__name__)


 # -*- coding: utf-8 -*-
def model():    
    import speech_recognition as sr
    import wave
    r = sr.Recognizer()  
    acoustic_parameters_directory='model/acoustic'
    language_model_file = 'model/language-model.lm.bin'
    phoneme_dictionary_file ='model/pronounciation-dictionary.dict'
    language_model_file=(acoustic_parameters_directory,language_model_file,phoneme_dictionary_file) 
    # obtain audio from file
    with sr.AudioFile(r'C:\sphinx\model forqan\sound\moh.wav') as source:
  
        audio = r.record(source)
    try:  
        return("'"+r.recognize_sphinx(audio,language_model_file)+ "'")  
          
    except sr.UnknownValueError:  
        return("error")  
    except sr.RequestError :  
        return("error") 
"""



"""
corpus=["binasonaMina LBnaAAnahina rBndHonaManaAAnaNina rBndHonayynaMona",
        "aanaLonaHanaMonaduna LinaLBnaAAnahina randbIna LonaeanaAAnaLanaMinayynaNona",
        "aanarBndHonaManaAAnaNina rBndHonayynaMona",
        "ManaAAnaLinakina yanawonaMina dInayynaNona",
        "ainayBnaAAnakana Nanaeonabunaduna wanaainayBnaAAnakana NanasonatanaeinayynaNona",
        "aanahonadinaNana SInbrandAAndTand LonaMunasonatanaqinbyynaMona",
        "SinbrandAAnaTand LBnaZinayynaNana aanaNonaeanaMonatana eanaLanayonahinaMona gandyonarina LonaManagondDuncwUnabina eanaLanayonahinaMona wanaLana DBndACndLInayynaNona"
        ]
verses=["بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ",
        "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ",
        "الرَّحْمَنِ الرَّحِيمِ",
        "مَالِكِ يَوْمِ الدِّينِ",
        "إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ",
        "اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ"
        ,"صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ"]
numb=6
c=False
faultindex=[]
faultreport=[]
inputs=model()
word=""
if(inputs!="error"):
    word="SinbrandAAnatana LBnazinayynaNana aanaNonaeanaMonatana eanaLanayonahinaMona ganayonarina LonaManagonadunawUnabina eanaLanayonahinaMona wanaLana DBndACndLInayynaNona"
verse=corpus[numb].split()
verseara=verses[numb].split()
inputverse=word.split()
def chardic(x):
    dic = {
        "n": "النون",
        "k": "الكاف",
        "y": "الياء",
        "d": "الدال",
        "T": "الطاء",
        "t": "التاء",
        "s": "السين",
        "S": "الصاد",
        "q": "القاف",
        "Z": "الذال",
        "z": "الزاي",
        "g": "الغين",
        "D":"الضاد",
        "d":"الدال",
        "A":"ألف_مدية"
    }
    return dic.get(x)
def diacdic(x):
    dic = {
        "a": "مفتوح",
        "A": "ممدود_بالفتح_وجه_القصر",
        "C": "ممدود_بالفتح_وجه_الإشباع",
        "i": "مكسور",
        "o": "ساكن",
        "y": "مضموم",
        "B": "مشدد_بالفتح",
        
    }
    return dic.get(x)
    return x
def catdic(x):
    dic = {
        "a": "مرقق",
        "b": "مفخم_من_الدرجة_الثالثة",
        "c": "مفخم_من_الدرجة_الثانية",
        "d": "مفخم_من_الدرجة_الأولى", 
    }
    return dic.get(x)
    return x
    
def detection(realword,faultword):
    errorlist=[]
    i=0
    l=0
    for j in range(int(len(realword)/4)+1):
        if(j==0):
            continue
        if realword[l:j*4]!=faultword[l:j*4]:
            errorlist.append("،"+chardic(realword[j*4-4]))
            for ch in realword[i:j*4]:
        
                if(ch!=faultword[i]):
                    #  errorlist+=(i%4) error type
                    fch=""
                    nch=""
                    if i%4== 0:
                        nch=chardic(ch)
                        fch=chardic(faultword[i])
                    elif i%4 == 1:
                        nch=diacdic(ch)
                        fch=diacdic(faultword[i])
                    else:
                        nch=catdic(ch)
                        fch=catdic(faultword[i])
                        #   errorlist+=(int(i/4))letter index
                    errorlist.append(nch)
                    errorlist.append(fch)#(fault's type index,letter's index,'correct index','fault index')
                i+=1
        l+=4            
    return errorlist
if(len(verse)==len(inputverse)):
    i=0
    l=""
    for w in inputverse :
        if(verse[i]!=w):
            faultindex.append("."+verseara[i])
            faultreport.append(detection(verse[i],w))
        i+=1       
cou=int(1)       
for w in faultreport:
    for wo in w:
        faultindex.insert(cou,wo)
        cou=cou+1
    cou=cou+1




@app.route('/')    
def index ():
    return faultindex
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000)
print(faultindex)            





