#sinav sonuc isminde bir sözlük tanımladim ve icine value tanımladim
sinav_sonuc={
    'isimler':['ayşe k','ahmet m','Nuri c','nawar t','suzan t','ala b'],
    'cinsiyet':['K','E','E','E','K','K'],
    'matematik':[80,60,77,25,36,75],
    'turkce':[90,50,53,100,98,66]
}
turkcenot=0  #degerleri toplayacagim icin degerleri 0 a esitledim
erktop=0
kiztop=0
for i in range(len(sinav_sonuc['cinsiyet'])):  #hangi cinsiyeti belirleyeecğimi belli etmek icin bir for döngüsü açtim
    if sinav_sonuc['cinsiyet'][i]=='K':            #cinsiyet icerisinde kizlarin degerinde dolastim
        kiztop=kiztop+sinav_sonuc['matematik'][i]  #matematik notlarini topladim
kiztop=kiztop/3                                    #ortalamayi bulmak icin kiztop degereini uce boldum
print(f'kizlarin matematik not ortalamasi :', kiztop) #ortalamayi yazdirdim

for i in range(len(sinav_sonuc['cinsiyet'])):     #cinsiyetler arasinda dolandim
    if sinav_sonuc['cinsiyet'][i]=='E':           #cinsiyetin erkek oldugunu belirledim
        erktop=erktop+sinav_sonuc['matematik'][i] #erkeklerin matematik notunu topladim
erktop=erktop/3                                   #erkeklerin matematik ortalamasini aldirdim
print(f'erkeklerin matematik not ortalamasi :', erktop) #erkeklerin mat ortalamasini yazdirdim

for i in range(len(sinav_sonuc['turkce'])):  #döngü ile turkce notlarini aldim
    turkcenot=turkcenot+sinav_sonuc['turkce'][i] #türkce notlarini topladim
print('turkce not ortalamasi :', turkcenot/len(sinav_sonuc['turkce'])) #turkce notlarini turkce karakter sayisina bölüp ortalamyi yazdirdim

kiznotlar=[]                                     #kizlarin notlarini tutmak icin dizi olusturudm
for i in range(len(sinav_sonuc['cinsiyet'])):    #sinav sonuclarının cinsiyetlerinin arasinda doalndim
     if sinav_sonuc['cinsiyet'][i]=='K':         #cinsiyetin kiz olup olmadigina baktım
        kiznotlar.append(sinav_sonuc['turkce'][i]) #kiz notlarını oluşturdugum diziye ekledim
print("en yuksek turke kiz notu :",max(kiznotlar)) #en yüksek kiz notunu dizi içerisinden max degerini aldim

erkeknotlar=[]                                    #erkeklerin notlarini tutmak icin dizi olusturdum
for i in range(len(sinav_sonuc['cinsiyet'])):     #sinav sonuclarinin cinsiyetleri arasinda dolandim
     if sinav_sonuc['cinsiyet'][i]=='E':          #cinsiyetin erkek oldugunu kontrol ettim
        erkeknotlar.append(sinav_sonuc['turkce'][i]) #olusturdugum diziye erkek notlarini attim
print("en yuksek erkek turkce notu :",max(erkeknotlar)) #erkek notlar dizinin en yuksek elemanını alip yazdirdim
   








