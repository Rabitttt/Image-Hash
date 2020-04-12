#SELMAN BURAK KARAGÖL

#REQUIREMENTS
# -pip install opencv-python
#Resim eklerken resmin "jpg" uzantılı olduguna dikkat ediniz. Resmi Proje Adına Surukle Bırak Yaparak Ekleyebilirsiniz.

import cv2  #OpenCV kütüphanesi eklendi.

resim = cv2.imread("resim.jpg")  #Resim Dosyasinin Pixellerini Listede RGB formatinda tutar.

cv2.imshow("resim",resim)  #Resmin ekranda çıkmasını saglayan kod

list = [[],[],[],[],[],[],[],[],[],[]] #Listelerin Listesi.

sayi = 0
toplam = 0

for satir in resim: #3 boyutlu listenin 2. boyutunda Satirlarda Gezer
    for pixel in satir:  #Her Satirdaki Her bir Pixele Erişebilmemizi Saglar.
        sayi = pixel[0] + pixel[1] + pixel[2] #Hash Yontemi İcin her Pixelin R G B (0-255 , 0-255 , 0-255) degerlerinin Toplamini Bulurken Kullanilir.
        Mod_Indis = sayi % 10 #Bulunan R G B toplamlarinin 10 a Gore Modunu Alir
        list[Mod_Indis].append(sayi) #Dizinin ,Mod Degerindeki indisine R G B toplamlarini Koyar.

list_mod2 = [000,000,000,000,000,000,000,000,000,000]  #

indis = 0

for i in list:  #Pixellerin Toplamlarini Moda Gore Gruplamiş olan 2 Boyutlu Dizinin Ilk Boyutuna Ulaşır.
    for Pixel_Deger in i:  #Pixel Toplamlarini Tutan dizinin 2. Boyutuna Ulaşır
        toplam += Pixel_Deger  #Mod Degerine Gore Aynı Yere Gruplanmis Pixel Toplamlarını Toplar
    toplam = toplam % 256  #Toplamin 256 ya Gore Modunu Alir
    list_mod2[indis] = toplam   #10 Haneli Diziye Modu Alinmis Toplam Degerlerini Ekler
    indis += 1  #Toplamın Eklenecegi Indisi 1 Arttırır.


#Hash Degeri List_mod2 Dizisinin Her Indis Degerinin Ard Ada Eklenmesiyle Edilir.
HASH =  "{}{}{}{}{}{}{}{}{}".format(list_mod2[0],list_mod2[1],list_mod2[2],list_mod2[3],list_mod2[4],list_mod2[5],list_mod2[6],list_mod2[7],list_mod2[8],list_mod2[9])
print("Resmin Hash Kodu : " + HASH)

cv2.waitKey(0)  #Resmin Ekranda Kalmasini Saglar


#ANALİZE YARDIMCI SATIRLAR ASAGIDADIR . Kullanmak İçin Yorum Satiri İfadesini '#' Kaldiriniz.(Resim Kapatildiginda Calisir)
#print(resim.shape) #(Satir Pixel , Sutun pixel , 3 (RGB yi temsilen) )
#print(type(resim)) #Resim Degiskeninin Tipini verir. sonuc = <class 'numpy.ndarray'>
#print(resim) #3 Boyutlu Pixel Tutan Listeyi Yazdirir
