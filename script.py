from bs4 import BeautifulSoup as bs
import requests, re

def get_lyrics():
    doc = requests.get("https://genius.com/The-champs-tequila-lyrics").text
    res = bs(doc, "html.parser")
    parse = res.find_all(class_="Lyrics__Container-sc-78fb6627-1 hiRbsH")
    s=""
    for tag in parse:
        s += tag.get_text(separator=" ")
    #print(s)
    l = re.split(r'[-[;,\s]+', s)
    for i in range(0, len(l)):
        l[i]=l[i].strip("()[]''-!:;,“”")
        l[i]=l[i].strip('""')
    #print(l)
    return l

def get_wc():
    dict = {}
    lyrics = get_lyrics()
    for lyric in lyrics:
        lyric=lyric.lower()
        #
        if lyric == 'mf' or lyric == 'doom': lyric=lyric.upper()
        #
        if lyric in dict:
            dict[lyric]+=1
        else:
            dict[lyric]=1
    return sort_dict(dict)


def sort_dict(dict):
    lyrics = []
    for d in dict:
        pair = (d, dict[d])
        lyrics.append(pair)
    for i in range(0, len(lyrics)):
        for j in range(i+1, len(lyrics)):
            if(lyrics[i][1] > lyrics[j][1]):
                temp = lyrics[j]
                lyrics[j]=lyrics[i]
                lyrics[i]=temp
    return lyrics

def word_report():
    dict = get_wc()
    print(f'Most common word: {dict[len(dict)-1][0]}: {dict[len(dict)-1][1]} times')



if __name__ == '__main__':
    word_report()