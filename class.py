class OtonomArac:
    def __init__(self, hiz_limiti=120, son_konum=None, guvenli_mesafe=10, 
                 hava_durumu=None, trafik_durumu=None):
        self.hiz_limiti = hiz_limiti
        self.son_konum = son_konum
        self.guvenli_mesafe = guvenli_mesafe
        self.hava_durumu = hava_durumu
        self.trafik_durumu = trafik_durumu
    
    def hiz_kontrolu(self, hiz):
        if hiz > self.hiz_limiti:
            print(f"Hiz sinirini astiniz. Hiz limiti: {self.hiz_limiti}")
            return False
        return True
    
    def mesafe_kontrolu(self, ondaki_arac_mesafe):
        if ondaki_arac_mesafe < self.guvenli_mesafe:
            print(f"Ondaki araca cok yakinsiniz. Mesafe: {ondaki_arac_mesafe} metre")
            return False
        return True
    
    def hava_durumu_kontrolu(self):
        if self.hava_durumu == "yagmurlu":
            print("Yagmurlu havada surus yapmak tehlikelidir.")
            return False
        return True
    
    def trafik_kontrolu(self):
        if self.trafik_durumu == "yoğun":
            print("Trafik yogunlugu nedeniyle ilerlemekte zorluk yasayabilirsiniz.")
            return False
        return True
    
    def seyahat_et(self, hedef_konum):
        if not self.hiz_kontrolu(80):
            return
        if not self.mesafe_kontrolu(20):
            return
        if not self.hava_durumu_kontrolu():
            return
        if not self.trafik_kontrolu():
            return
        
        self.son_konum = hedef_konum
        print(f"Hedef konuma ulasildi: {hedef_konum}")
