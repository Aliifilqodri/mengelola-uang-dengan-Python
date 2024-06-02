import matplotlib.pyplot as plt

class Keuangan:
    def __init__(self, total_uang):
        self.total_uang = total_uang
        self.tabungan = 0
        self.makan = 0
        self.foya_foya = 0
        self.target = 0

    def alokasikan_uang(self, persen_tabungan, persen_makan, persen_foya_foya):
        self.tabungan = self.total_uang * persen_tabungan / 100
        self.makan = self.total_uang * persen_makan / 100
        self.foya_foya = self.total_uang * persen_foya_foya / 100

    def set_target_tabungan(self, target):
        self.target = target

    def cek_kemajuan(self):
        return (self.tabungan / self.target) * 100

    def tampilkan_grafik(self):
        labels = ['Nabung', 'Beli Makan', 'Foya-foya']
        values = [self.tabungan, self.makan, self.foya_foya]
        colors = ['#4CAF50', '#FFC107', '#FF5722']
        
        plt.figure(figsize=(10, 5))
        plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.title(f'Alokasi Uang (Total: Rp {self.total_uang})')
        plt.show()

        if self.target > 0:
            plt.figure(figsize=(10, 5))
            plt.bar(['Target Tabungan'], [self.target], color='#4CAF50')
            plt.bar(['Tabungan Sekarang'], [self.tabungan], color='#FFC107')
            plt.title('Kemajuan Menuju Target Tabungan')
            plt.ylim(0, max(self.target, self.tabungan) * 1.2)
            plt.show()

# Penggunaan
total_uang = 480147
persen_tabungan = 60
persen_makan = 20
persen_foya_foya = 20
target_tabungan = 1000000

keuangan = Keuangan(total_uang)
keuangan.alokasikan_uang(persen_tabungan, persen_makan, persen_foya_foya)
keuangan.set_target_tabungan(target_tabungan)

print(f"Tabungan: Rp {keuangan.tabungan}")
print(f"Beli Makan: Rp {keuangan.makan}")
print(f"Foya-foya: Rp {keuangan.foya_foya}")
print(f"Kemajuan Tabungan: {keuangan.cek_kemajuan()}%")

keuangan.tampilkan_grafik()
