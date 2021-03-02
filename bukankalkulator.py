'''
Buatlah program untuk menghitung penghasilan kotor dan bersih serta sisa dari penjualan saham (kuantitas per lot) (1 lot = 100)
Harga adalah per lembar
Gunakan fungsi def dan return
'''

#proses

def hitung_kotor(harga_beli,harga_jual,kuantitas_beli,kuantitas_jual) :
    penghasilan_kotor = (harga_jual * kuantitas_jual*100)
    return penghasilan_kotor
    
def hitung_bersih(harga_beli,harga_jual,kuantitas_beli,kuantitas_jual) :
    penghasian_bersih = (harga_jual * kuantitas_jual*100) - (harga_beli*kuantitas_beli*100)
    return penghasian_bersih 
    
def hitung_sisa(harga_beli,harga_jual,kuantitas_beli,kuantitas_jual) :
    sisa = kuantitas_jual - kuantitas_beli
    return sisa

kotor = hitung_kotor(2000,3000,20,50) #input
print("Keuntungan kotor anda adalah :",kotor) #output

bersih = hitung_bersih(2000,3000,20,50) #input
print("Keuntungan bersih anda adalah :",bersih) #output

sisa = hitung_sisa(2000,20,20,50) #input
print("Sisa saham anda adalah :",sisa,"lot") #output
