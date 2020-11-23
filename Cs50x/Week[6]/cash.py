from cs50 import get_float

para=get_float("para miktarını giriniz:")

while para<0:
    para=get_float("para miktarını giriniz:")
    
kurus=round(para*100)
Gvpara=0
paralar=[25,10,5,1]

for i in range(len(paralar)):
#/ float değer // int değer döndürür
    Gvpara+=kurus//paralar[i]
    kurus%=paralar[i]
    
print("toplam verilen para sayısı:",Gvpara)    
