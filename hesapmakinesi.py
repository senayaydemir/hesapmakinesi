def topla(a,b):
 return a+b 
def cikar(a,b):
 return a-b
def carp(a,b):
 return a*b
def bol(a,b):
 return a/b

print("""
Hesap Makinesi
      1. Toplama 
      2. Çıkarm 
      3. Çarpma
      4. Bölme
      5.Üs Alma

      
""")
sec=input("Seçiminiz:")
say_a=input("1.Sayı:")
say_b=input("2.Sayı:")
if (sec=="1"):
 print( topla(int(say_a),int(say_b)))
elif(sec=="2"):
  print( cikar(int(say_a),int(say_b)))
 