def topla(a,b):
 return a+b

print("""
Hesap Makinesi
      1. Toplama 
      2. Çıkarm 
      3. Çarpma
      4. Bölme
      5.Üs Alma

      
""")
sec=input("Seçiminiz:")
if (sec=="1"):
 say_a=input("1.Sayı:")
 say_b=input("2.Sayı:")
 print( topla(int(say_a),int(say_b)))