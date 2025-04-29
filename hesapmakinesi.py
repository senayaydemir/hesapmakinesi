def topla(a,b):
 return a+b 
def cikar(a,b):
 return a-b
def carp(a,b):
 return a*b
def bol(a,b):
 if 0 == int(b):
  print("Sıfıra Bölünme Hatası")
  return 0
 else:
  return a/b
def usal(a,b):
  return a**b
while True:
 print("""
Hesap Makinesi
      1. Toplama 
      2. Çıkarma
      3. Çarpma
      4. Bölme
      5. Üs Alma

      
 """)
 sec=input("Seçiminiz:")
 say_a=input("1.Sayı:")
 say_b=input("2.Sayı:")
 if (sec=="1"):
  print( topla(int(say_a),int(say_b)))
 elif(sec=="2"):
  print( cikar(int(say_a),int(say_b)))
 elif(sec=="3"):
  print( carp(int(say_a),int(say_b)))
 elif(sec=="4"):
  print( bol(int(say_a),int(say_b)))
 elif(sec=="5"):
  print( usal(int(say_a),int(say_b)))
 else :
  print("Geçersiz İşlem")
  input("Devam etmek için ENTER")
 