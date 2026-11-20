#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahve İçince Neden Daha Yorgun Oluyorum Simulatoru
Gerçekten çalışır. Gerçekten hiçbir şey çözmez.
"""

import random
import time

def neden_daha_yorgun(kahve_sayisi):
    sebepler = [
        "Kahve molekülleri senin yorgunluğunu tanıdı ve ona aşık oldu. Artık ayrılmak istemiyorlar.",
        "Kahve içtikten sonra vücudun 'oh rahatladım' dedi ve tamamen kapatma moduna geçti.",
        "Bilimsel gerçek: Kahve aslında anti-kahvedir. İçtikçe ters etki yapar.",
        "Kahve senin yerine yoruldu, sen de onun yorgunluğunu hissettin. Empati bu.",
        "Kafein seni uyandırmak yerine 'bu iş bitmez' diye ikna etti.",
        "Kahve içmek için harcadığın enerji, kahvenin verdiği enerjiden fazla.",
        "Vücudun kahveyi görünce 'yine mi bu herif' dedi ve greve gitti.",
        f"Tam {kahve_sayisi} kahve içtin. Bu sayı kutsal. Kutsal sayılar yorar."
    ]
    
    print("\n🔬 Bilimsel Analiz Başlıyor...")
    time.sleep(1)
    print("🧊 Kahve molekülleri inceleniyor...")
    time.sleep(1)
    print("📊 Yorgunluk katsayısı hesaplanıyor...")
    time.sleep(1)
    
    print(f"\n✅ SONUÇ: {kahve_sayisi} kahve içtiğin için %{(kahve_sayisi * 23 + random.randint(10, 90)) % 100} daha yorgunsun.")
    print(f"📝 Sebep: {random.choice(sebepler)}")
    print("\n😎 Tavsiye: Bir kahve daha iç. Belki bu sefer işe yarar. (Yaramaz.)")

def main():
    print("=" * 50)
    print("KAHEVE İÇİNCE NEDEN DAHA YORGUN OLUYORUM?")
    print("Devrimsel Algoritma v1.0")
    print("=" * 50)
    
    try:
        sayi = int(input("\nBugün kaç kahve içtin? (sayı gir): "))
        if sayi < 0:
            print("Negatif kahve mi? Zaten uykudasın demek.")
            return
        neden_daha_yorgun(sayi)
    except ValueError:
        print("Sayı gir dedik kardeşim. Kahve sayısı string olamaz.")

if __name__ == "__main__":
    main()
