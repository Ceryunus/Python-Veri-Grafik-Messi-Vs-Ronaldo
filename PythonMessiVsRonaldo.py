import requests
# resimlendirmek için kullanılan modüller
from io import BytesIO  # bytlarla iş yapmak icin
from PIL import Image   # baytları resme dönüştürmek icin

class Futbolcu():

    def __init__(self, isim, hiz, sut, pas, top_surme, defans, fizik):
        self.isim = isim
        self.hiz = hiz
        self.sut = sut
        self.pas = pas
        self.top_sureme = top_surme
        self.defans = defans
        self.fizik = fizik

    def yetenek_hazirla(self):
        yetenekler = ",".join([
            str(self.hiz),
            str(self.sut),
            str(self.pas),
            str(self.top_sureme),
            str(self.defans),
            str(self.fizik),
            str(self.hiz)
        ])  # listenin içerisindeki her bir elemanın arasını yanda verdiğimiz şeyi koyuyuor !
        print(yetenekler)
        return yetenekler

    def yetenek_goresllestir(self):
        grafik_URL = "https://image-charts.com/chart"

        payload = {
            "chco": "3092de",  # renk
            "chd": "t:" + self.yetenek_hazirla(),  # yetenekler
            "chdl": self.isim,  # isim
            "chdlp": "b",  #
            "chs": "480x480",  # grafik boyutu
            "cht": "r",  # radar chart chart tipi yani
            "chtt": "Futbolcu Ozellikleri",  # baslık
            "chl": "hiz|sut|pas|top_surus|defans|fizik",  # lableear etiketler
            "chxl": "0:|0|20|40|60|80|100",  # lable alabileceği değerler
            "chxt": "x",  # x eksenine ataması
            "chxr": "0,0.0,100.0",  # max değeri
            "chm": "b,aaaaaabb,0,0,0"
        }

        response = requests.post(grafik_URL, data=payload)
        print(response.status_code)
        print(response.content)
        image = Image.open(BytesIO(response.content))
        image.show()

    def yetenek_kiyaslama_goster(self, hedef_ftbolcu):
        grafik_URL = "https://image-charts.com/chart"

        payload = {
            "chco": "3092de,027182",  # renk
            "chd": "t:" + self.yetenek_hazirla() + "|" + hedef_ftbolcu.yetenek_hazirla(),  # yetenekler
            "chdl": self.isim + "|" + hedef_ftbolcu.isim,  # isim
            "chdlp": "b",  #
            "chs": "480x480",  # grafik boyutu
            "cht": "r",  # radar chart chart tipi yani
            "chtt": "Futbolcu Ozellikleri",  # baslık
            "chl": "hiz|sut|pas|top_surus|defans|fizik",  # lableear etiketler
            "chxl": "0:|0|20|40|60|80|100",  # lable alabileceği değerler
            "chxt": "x",  # x eksenine ataması
            "chxr": "0,0.0,100.0",  # max değeri
            "chm": "b,aaaaaabb,0,0,0|b,0073cfbb,1,0,0"
        }
        response = requests.post(grafik_URL, data=payload)
        print(response.status_code)
        print(response.content)
        image = Image.open(BytesIO(response.content))
        image.show()


messi = Futbolcu("messi", 85, 92, 91, 95, 38, 68)
ronaldo = Futbolcu("ronaldo", 89, 93, 81, 89, 35, 77)
# ronaldo.yetenek_goresllestir()
messi.yetenek_kiyaslama_goster(ronaldo)
