import random
import time 
import emoji


peserta = ["Yusuf", "Rafii", "Ahmad", "Dedi", "Eka"]
    
print("--- PENGUNDIAN HADIAH ---")
print(f"Peserta: {peserta}")
    
pemenang = random.choice(peserta)

if pemenang:
    pesan = emoji.emojize(f"Selamat :party_popper: Pemenangnya adalah: **{pemenang}** :trophy:")
    print("\n" + "="*30)
    print(pesan)
    print("="*30)