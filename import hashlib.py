import hashlib
import os

def parola_olustur(plain_password):
    salt = os.urandom(16)
    
    hash_obj = hashlib.sha256(salt + plain_password.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    
    return salt, password_hash

def parola_dogrula(girilen_parola, saklanan_salt, saklanan_hash):

    yeni_hash = hashlib.sha256(saklanan_salt + girilen_parola.encode('utf-8')).hexdigest()
    
    return yeni_hash == saklanan_hash

kullanici_parolasi = "belekuni"

db_salt, db_hash = parola_olustur(kullanici_parolasi)

print(f"Sisteme Kaydedilen Tuz: {db_salt.hex()}")
print(f"Sisteme Kaydedilen Hash: {db_hash}")

test_parola = "belekuni"
if parola_dogrula(test_parola, db_salt, db_hash):
    print("\n✅ Giriş Başarılı!")
else:
    print("\n❌ Hatalı Parola!")