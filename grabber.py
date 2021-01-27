# -*- coding: utf-8 -*-
def grabber(myfile,url,url_begin,url_last,new_file):
    from bs4 import BeautifulSoup
    import urllib3
    import pandas
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data)
    
    # IMAGES
    images = []
    for img in soup.findAll('img'):
        images.append(img.get('src'))

    table = soup.find_all("p", class_="desc")
    spec = []
    for x in table:
        spec = spec + [x.text]
        
    step = 0
    for i in images:
        step = step + 1
        if i == url_begin:
            debut = step
        if i == url_last:
            fin = step
    
    list_img = []  
    for j in range(debut-1,fin):
        list_img = list_img + [images[j]]

    df = pandas.read_csv(myfile)
    df = df.drop(['list','position'], axis=1)
    
    df['spec'] = spec
    df['img_url'] = list_img
    df.to_csv(new_file, sep=';',index=False,encoding='utf-8-sig')
    

# TABLETTE
grabber('tablette.txt',
        "https://www.ldlc.com/informatique/tablette/tablette/c4271/+fb-C000001041,C000001080,C000005309,C000033945.html?sort=4",
        "https://media.ldlc.com/r150/ld/products/00/05/73/37/LD0005733773_1.jpg",
        "https://media.ldlc.com/r150/ld/products/00/05/70/54/LD0005705448_1_0005705489_0005705499.jpg",
        "tablette.csv")

grabber('phone1.txt',
        "https://www.ldlc.com/telephonie/telephonie-portable/mobile-smartphone/c4416/+fb-C000000806,C000001080,C000005309,C000035190,C000035309,C000036353,C000036359.html?sort=4",
        "https://media.ldlc.com/r150/ld/products/00/05/70/09/LD0005700913_1.jpg",
        "https://media.ldlc.com/r150/ld/products/00/05/72/46/LD0005724615_1.jpg",
        "phone1.csv")

grabber('phone2.txt',
        "https://www.ldlc.com/telephonie/telephonie-portable/mobile-smartphone/c4416/page2/+fb-C000000806,C000001080,C000005309,C000035190,C000035309,C000036353,C000036359.html?sort=4",
        "https://media.ldlc.com/r150/ld/products/00/05/66/02/LD0005660289_2_0005660348.jpg",
        "https://media.ldlc.com/r150/ld/products/00/05/66/03/LD0005660304_2_0005660366.jpg",
        "phone2.csv")

grabber('pc.txt',
        "https://www.ldlc.com/informatique/ordinateur-portable/pc-portable/c4265/+fb-C000000220,C000000806,C000000920,C000000992,C000001041,C000004770,C000005597,C000033945,C000035190,C000035990,C000037334.html?sort=4",
        "https://media.ldlc.com/r150/ld/products/00/05/70/85/LD0005708533_1_0005708538_0005765903.jpg",
        "https://media.ldlc.com/r150/ld/products/00/05/71/26/LD0005712621_1_0005737536.jpg",
        "pc.csv")

grabber('macbook.txt',
        'https://www.ldlc.com/informatique/ordinateur-portable/portable-mac/c4266/?sort=4',
        'https://media.ldlc.com/r150/ld/products/00/05/74/91/LD0005749151_1.jpg',
        'https://media.ldlc.com/r150/ld/products/00/05/67/13/LD0005671385_1_0005758914_0005758932.jpg',
        'macbook.csv')

grabber('watch.txt',
        "https://www.ldlc.com/objets-connectes/loisirs/montre-connectee/c5962/?sort=4",
        "https://media.ldlc.com/r150/ld/products/00/05/72/09/LD0005720946_1.jpg",
        "https://media.ldlc.com/r150/ld/products/00/05/75/92/LD0005759286_1.jpg",
        'watch.csv')

grabber('pc2.txt',
        'https://www.ldlc.com/informatique/ordinateur-de-bureau/pc-de-marque/c4250/+fb-C000000192,C000000806,C000000992,C000001041,C000005597,C000033945,C000034247,C000034387.html?sort=4',
        'https://media.ldlc.com/r150/ld/products/00/05/76/88/LD0005768804_1.jpg',
        'https://media.ldlc.com/r150/ld/products/00/05/72/89/LD0005728995_1_0005735429_0005772542_0005772999.jpg',
        'pc2.csv')

grabber('tv.txt',
        'https://www.ldlc.com/image-son/television/tv-ecran-plat/c4402/?sort=4',
        'https://media.ldlc.com/r150/ld/products/00/05/73/79/LD0005737958_1.jpg',
        'https://media.ldlc.com/r150/ld/products/00/05/69/30/LD0005693074_1.jpg',
        'tv.csv')

# MERGE ALL DATAFRAMES
import pandas
myfiles = ['tablette.csv',
           'phone1.csv',
           'phone2.csv',
           'pc.csv',
           'macbook.csv',
           'watch.csv',
           'pc2.csv',
           'tv.csv']

df1 = pandas.read_csv(myfiles[0],sep=';')
for k in myfiles[1:]: 
    df2 = pandas.read_csv(k,sep=';')
    df1 = pandas.concat([df1, df2])
df1.to_csv("database.csv", sep=';',index=False,encoding='utf-8-sig')