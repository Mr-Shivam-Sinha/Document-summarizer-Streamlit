import nltk
import re
nltk.download("all")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
import streamlit as st

def summarizer(files):
# content=open("case study - CAC1.txt","r",encoding='utf8')
# files=content.read().replace('\n',' ')
# print(files)
    cleaned_content= re.sub('[^a-zA-Z0-9\.]', ' ', files)
    cleaned_content=" ".join(cleaned_content.split())
# print(cleaned_content)
    tokenizer = nltk.RegexpTokenizer(r"[a-z,A-Z]+")
    new_tokens = tokenizer.tokenize(cleaned_content)
    new_tokens = [t.lower() for t in new_tokens]
    new_tokens =[t for t in new_tokens if len(t)!=1]
    new_tokens =[t for t in new_tokens if t not in stopwords.words("english")]
# print(new_tokens)

    freq=nltk.FreqDist(new_tokens)

    top_words=[]
    weights=[]

    for i,j in freq.items():
        if(j>=15):
            top_words.append(i)
            weights.append(j/len(new_tokens))
# print(top_words)
# print(weights)

    weight_values = dict(zip(top_words, weights))
    sentences=[]
    sentences=sent_tokenize(cleaned_content)

    imp_Sents=[]
    for i in top_words:
        current_word=i
        for j in sentences:
            current_sent=j
            if (current_sent.find(current_word) !=-1):
                imp_Sents.append(current_sent)
      
# print(imp_Sents)

    unique_sents = set()
    result = []
    for item in imp_Sents:
        if item not in unique_sents:
            unique_sents.add(item)
            result.append(item)
        
    summary=""
    for i in result:
        summary +=" "+i
    return summary

def summary():
    # st.title("DOCUMENT SUMMARIZER")
    html_temp = """
    <div style ="background-color:cyan;padding:13px">
    <h1 style ="color:black;text-align:center;">DOCUMENT SUMMARIZER</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    my_file=st.text_area("Paste Document content", placeholder="Paste here",height=60)
    result =""
    if st.button("Summarize"):
        result = summarizer(my_file)
    st.success(result)
        



summary()
##
