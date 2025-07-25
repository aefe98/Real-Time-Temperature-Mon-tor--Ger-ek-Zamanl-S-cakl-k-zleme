import matplotlib
matplotlib.use('TkAgg')  # Windows'ta grafik açılmıyorsa ekle

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time

zaman = []
sicaklik_listesi = []

fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-o', label='Vücut Sıcaklığı')
ax.set_ylim(35, 42)
ax.set_xlim(0, 20)
ax.set_xlabel('Zaman (saniye)')
ax.set_ylabel('Sıcaklık (°C)')
ax.set_title('Gerçek Zamanlı Vücut Sıcaklığı Grafiği')
ax.legend()
ax.grid(True)

start_time = time.time()

def oku_sicaklik():
    return round(random.uniform(36.0, 41.0), 1)

def guncelle(frame):
    su_an = round(time.time() - start_time)
    yeni_sicaklik = oku_sicaklik()

    zaman.append(su_an)
    sicaklik_listesi.append(yeni_sicaklik)

    if len(zaman) > 20:
        zaman.pop(0)
        sicaklik_listesi.pop(0)
        ax.set_xlim(zaman[0], zaman[-1])

    line.set_data(zaman, sicaklik_listesi)

    # Konsola mesaj yazdır
    if yeni_sicaklik > 39.5:
        print(f"{su_an}s: {yeni_sicaklik}°C - Ciddi ateş, Yüksek ateş tespit edildi!")
    elif yeni_sicaklik > 38.0:
        print(f"{su_an}s: {yeni_sicaklik}°C - Yüksek ateş, müdahale gerektirir")
    elif 37.5 <= yeni_sicaklik <= 38.0:
        print(f"{su_an}s: {yeni_sicaklik}°C - Subferil, Hafif ateş başlangıcı")
    elif yeni_sicaklik < 36.0:
        print(f"{su_an}s: {yeni_sicaklik}°C - Hipotermi riski, Düşük vücut ısısı")
    else:
        print(f"{su_an}s: {yeni_sicaklik}°C - Vücut ısısı normal")

    return line,

ani = animation.FuncAnimation(fig, guncelle, interval=1000)  # 1 saniyede bir güncelle
plt.show()

