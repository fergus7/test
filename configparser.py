import os

for r,d,f in os.walk(r"C:"):
    for files in f:
         if files == "mplab_ide.conf":
              print (os.path.join(r,files))
              conf=os.path.join(r,files)
              
parent_dir = os.path.dirname(conf)
grandparent_dir = os.path.dirname(parent_dir)
engrandparent_dir=os.path.dirname(grandparent_dir)

print(engrandparent_dir)
devamı="sys\\java\\zulu8.64.0.19-ca-fx-jre8.0.345-win_x64\\"
son_adres= '"'+ engrandparent_dir + devamı + '"'
print(son_adres)






def degistir_conf_satiri(dosya_yolu, eski_satir, yeni_satir):
    with open(dosya_yolu, 'r') as dosya:
        icerik = dosya.read()
    
    icerik = icerik.replace(eski_satir, yeni_satir)
    
    with open(dosya_yolu, 'w') as dosya:
        dosya.write(icerik)


eski_satir = 'jdkhome="C:\\Program Files\\Microchip\\MPLABX\\v6.10\\sys\\java\\zulu8.64.0.19-ca-fx-jre8.0.345-win_x64\\"'
yeni_satir ='jdkhome='+son_adres

degistir_conf_satiri(conf, eski_satir,yeni_satir)

