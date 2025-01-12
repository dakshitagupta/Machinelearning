# -*- coding: utf-8 -*-
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
import streamlit as st
import pickle
import nltk


def transform_text(text):
    text=nltk.word_tokenize(text)
    #tokenize=>
    txt=[]
    for i in text:
        if(i not in ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']):
            txt.append(i)
    text=txt[:]
    txt.clear()
    #stopwords=>
    stop_words=["मैं","मुझको","मेरा","अपने आप को","हमने","हमारा","अपना","हम","आप","आपका","तुम्हारा","अपने आप","स्वयं","वह","इसे","उसके","खुद को","कि वह","उसकी","उसका","खुद ही","यह","इसके","उन्होने","अपने","क्या","जो","किसे","किसको","कि","ये","हूँ","होता है","रहे","थी","थे","होना","गया","किया जा रहा है","किया है","है","पडा","होने","करना","करता है","किया","रही","एक","लेकिन","अगर","या","क्यूंकि","जैसा","जब तक","जबकि","की","पर","द्वारा","के लिए","साथ","के बारे में","खिलाफ","बीच","में","के माध्यम से","दौरान","से पहले","के बाद","ऊपर","नीचे","को","से","तक","से नीचे","करने में","निकल","बंद","से अधिक","तहत","दुबारा","आगे","फिर","एक बार","यहाँ","वहाँ","कब","कहाँ","क्यों","कैसे","सारे","किसी","दोनो","प्रत्येक","ज्यादा","अधिकांश","अन्य","में कुछ","ऐसा","में कोई","मात्र","खुद","समान","इसलिए","बहुत","सकता","जायेंगे","जरा","चाहिए","अभी","और","कर दिया","रखें","का","हैं","इस","होता","करने","ने","बनी","तो","ही","हो","इसका","था","हुआ","वाले","बाद","लिए","सकते","इसमें","दो","वे","करते","कहा","वर्ग","कई","करें","होती","अपनी","उनके","यदि","हुई","जा","कहते","जब","होते","कोई","हुए","व","जैसे","सभी","करता","उनकी","तरह","उस","आदि","इसकी","उनका","इसी","पे","तथा","भी","परंतु","इन","कम","दूर","पूरे","गये","तुम","मै","यहां","हुये","कभी","अथवा","गयी","प्रति","जाता","इन्हें","गई","अब","जिसमें","लिया","बड़ा","जाती","तब","उसे","जाते","लेकर","बड़े","दूसरे","जाने","बाहर","स्थान","उन्हें","गए","ऐसे","जिससे","समय","दोनों","किए","रहती","इनके","इनका","इनकी","सकती","आज","कल","जिन्हें","जिन्हों","तिन्हें","तिन्हों","किन्हों","किन्हें","इत्यादि","इन्हों","उन्हों","बिलकुल","निहायत","इन्हीं","उन्हीं","जितना","दूसरा","कितना","साबुत","वग़ैरह","कौनसा","लिये","दिया","जिसे","तिसे","काफ़ी","पहले","बाला","मानो","अंदर","भीतर","पूरा","सारा","उनको","वहीं","जहाँ","जीधर","के","एवं","कुछ","कुल","रहा","जिस","जिन","तिस","तिन","कौन","किस","संग","यही","बही","उसी","मगर","कर","मे","एस","उन","सो","अत"]

    #print(len(stop_words))
    for i in text:
        if i not in stop_words:
            txt.append(i)
    text=txt[:]
    
    ########go==>
    
    def generate_stem_words(word):
        suffixes = {1: [u"ो",u"े",u"ू",u"ु",u"ी",u"ि",u"ा"],2: [u"कर",u"ाओ",u"िए",u"ाई",u"ाए",u"ने",u"नी",u"ना",u"ते",u"ीं",u"ती",u"ता",u"ाँ",u"ां",u"ों",u"ें"],3: [u"ाकर",u"ाइए",u"ाईं",u"ाया",u"ेगी",u"ेगा",u"ोगी",u"ोगे",u"ाने",u"ाना",u"ाते",u"ाती",u"ाता",u"तीं",u"ाओं",u"ाएं",u"ुओं",u"ुएं",u"ुआं"],4: [u"ाएगी",u"ाएगा",u"ाओगी",u"ाओगे",u"एंगी",u"ेंगी",u"एंगे",u"ेंगे",u"ूंगी",u"ूंगा",u"ातीं",u"नाओं",u"नाएं",u"ताओं",u"ताएं",u"ियाँ",u"ियों",u"ियां"],5: [u"ाएंगी",u"ाएंगे",u"ाऊंगी",u"ाऊंगा",u"ाइयाँ",u"ाइयों",u"ाइयां"]}
        for L in 5, 4, 3, 2, 1:
            if len(word) > L + 1:
                for suf in suffixes[L]:
                    if word.endswith(suf):
                        return word[:-L]
        return word

    def generate_stem_dict():
        stem_word={}
        for each_token in text:
            #print type(each_token)
            temp=generate_stem_words(each_token)
            stem_word[each_token]=temp
            stemmed_word.append(temp)
        return stem_word
    
    stemmed_word=[]
    tt=generate_stem_dict()
    t1=list(tt.values())
    # print("check:",t1)    
    return(" ".join(t1))


tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model_lstm.pkl','rb'))

st.title("\U0001f4ac फेक न्यूज डिटेक्टर \U0001f4ac")
box_display = '<p style="font-family:sans-serif; color:#ffe456; font-size: 25px;-webkit-text-stroke-width:1px; -webkit-text-stroke-color:black ;">समाचार यहाँ लिखें \U0001F447</p>'
st.markdown(box_display, unsafe_allow_html = True)
input_sms = st.text_area("")

if st.button("खबर की जांच करें"):
    if input_sms is "":
        empty_display = '<p style="font-family:sans-serif; color:#ffe456; font-size: 40px; -webkit-text-stroke-width:1.4px; -webkit-text-stroke-color:black ;">\U0001F60A कृपया कुछ समाचार लिखें \U0001F60A</p>'
        st.markdown(empty_display, unsafe_allow_html = True)
    else:
        #1. preprocess
        transformed_sms = transform_text(input_sms)
        # print(transformed_sms)

        #2. Vectorize
        vector_input = tfidf.transform([transformed_sms])
        # print(vector_input)

        #3. Predict
        result = model.predict(vector_input)[0]

        #4.display
        if result  == 0:
            display_message = '<p style="font-family:sans-serif; color:RED; font-size: 40px;">\U000026A0 सावधान! यह समाचार गलत है \U000026A0</p>'
            st.markdown(display_message, unsafe_allow_html = True)
            
        else:
            display_message = '<p style="font-family:sans-serif; color:Green; font-size: 40px;">\U00002714 यह समाचार सही है \U00002714</p>'
            st.markdown(display_message, unsafe_allow_html = True)
