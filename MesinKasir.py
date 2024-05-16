import math
hargatotal=0
totallama=0
kursus=[]
stop=False
diskom=0
print("#"*40)
print("Selamat datang di bimbel kami")
print("kami menyediakan :")
print("- matematika")
print("- bahasaindonesia")
print("- bahasainggris")
print("- pendidikanagamaislam")
print("- bahasadaerah")
print("- biologi")
print("- fisika")
print("- geografi")
print("- sejarah")
print("- kimia")
print("#"*40)


while(not stop):
    mapel=input('Silahkan input mata pelajaran yang diinginkan :').lower()
    kursus.append(mapel)
    if mapel=="matematika":
        lama=int(input("mau ambil berapa lama (dalam bulan) :"))
        harga=(lama/12)*400000
    elif mapel=="bahasaindonesia":
        lama=int(input("mau ambil berapa lama (dalam bulan) :"))
        harga=(lama/12)*200000
    elif mapel=="bahasainggris":
        lama=int(input("mau ambil berapa lama (dalam bulan) :"))
        harga=(lama/12)*200000
    elif mapel=="pendidikanagamaislam":
        lama=int(input("mau ambil berapa lama (dalam bulan) :"))
        harga=(lama/12)*200000
    elif mapel=="bahasadaerah":
        lama=int(input("mau ambil berapa lama (dalam bulan) :"))
        harga=(lama/12)*200000
    elif mapel=="biologi":
        lama=int(input("mau ambil berapa lama (dalam bulan) :"))
        harga=(lama/12)*400000
    elif mapel=="fisika":
        lama=int(input("mau ambil berapa lama (dalam bulan) :"))
        harga=(lama/12)*400000
    elif mapel=="geografi":
        lama=int(input("mau ambil berapa lama (dalam bulan) :"))
        harga=(lama/12)*200000
    elif mapel=="sejarah":
        lama=int(input("mau ambil berapa lama (dalam bulan) :"))
        harga=(lama/12)*200000
    elif mapel=="kimia":
        lama=int(input("mau ambil berapa lama (dalam bulan) :"))
        harga=(lama/12)*400000
    else:
        print('Mohon maaf input salah')
    hargatotal=hargatotal+harga
    totallama=totallama+lama
    tanya = str(input("Mau ambil lagi?(y/t) :")).lower()
    if(tanya == "t"):
        stop = True

if totallama>=6 and totallama<=12:
    diskl=2/100
elif totallama>=12:
    diskl=4/100
else:
    diskl=0
    
jmlmatales=len(kursus)
if jmlmatales>=3 and jmlmatales<=6:
    diskj=2/100
elif jmlmatales>=6 and jmlmatales<=10:
    diskj=5/100
elif jmlmatales>=10:
    diskj=10/100
else:
    diskj=0
    
if "matematika" and "fisika" and "kimia" and "biologi" in kursus:
    disk=5/100
elif "bahasaindonesia" and "bahasainggris" and "bahasadaerah" in kursus:
    disk=5/100
elif "sejarah" and "geografi" in kursus:
    disk=5/100
else:
    disk=0
totaldiskon=diskl+diskj+disk

diskon=hargatotal*totaldiskon
tagihan=hargatotal-diskon
tagihan=math.ceil(tagihan)

print("#"*40)
print("Jumlah yang harus di bayarkan :", tagihan)
print("#"*40)
bayar=int(input("silahkan masukan jumlah yang dibayarkan :"))
kembalian=bayar-tagihan
totaldiskon=totaldiskon*100
totaldiskon=math.ceil(totaldiskon)
print("#"*40)
print("biaya keseluruhan        :",tagihan)
print("uang yang kamu bayarkan  :",bayar)
print("kembalian kamu           :",kembalian)