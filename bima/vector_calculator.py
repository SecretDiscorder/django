import pandas as pd
import plotly.graph_objects as go

import matplotlib.pyplot as plt
def hitung_besar_vektor(x, y, z=0):  # Add default value 0 for z to handle both 2D and 3D vectors
    besar_vektor = math.sqrt(x**2 + y**2 + z**2)
    return besar_vektor

def hitung_arah_vektor(x, y, z=None, sudut_radian=None):
    if z is not None and sudut_radian is not None:
        print("Peringatan: Berikan nilai hanya untuk z atau sudut_radian, tidak keduanya.")
        return None, None
    elif z is not None:
        arah_radian = math.atan2(y, x)
        arah_derajat = math.degrees(arah_radian)
    elif sudut_radian is not None:
        arah_radian = sudut_radian
        arah_derajat = math.degrees(arah_radian)
    else:
        print("Peringatan: Mohon berikan nilai untuk z atau sudut_radian.")
        return None, None

    return arah_radian, arah_derajat
    
def penjumlahan_paralel_dua_dimensi():
    x1 = float(input("Masukkan komponen x vektor pertama: "))
    y1 = float(input("Masukkan komponen y vektor pertama: "))
    x2 = float(input("Masukkan komponen x vektor kedua: "))
    y2 = float(input("Masukkan komponen y vektor kedua: "))

    x_jumlah = x1 + x2
    y_jumlah = y1 + y2

    besar_vektor = hitung_besar_vektor(x_jumlah, y_jumlah)  # No need to pass z argument here
    arah_radian, arah_derajat = hitung_arah_vektor(x_jumlah, y_jumlah)  # No need to pass z argument here

    df = pd.DataFrame({
        'Komponen X Vektor Pertama': [x1],
        'Komponen Y Vektor Pertama': [y1],
        'Komponen X Vektor Kedua': [x2],
        'Komponen Y Vektor Kedua': [y2],
        'Hasil Penjumlahan X': [x_jumlah],
        'Hasil Penjumlahan Y': [y_jumlah],
        'Besar Vektor Hasil Penjumlahan': [besar_vektor],
        'Arah Vektor (Radian)': [arah_radian],
        'Arah Vektor (Derajat)': [arah_derajat]
    })

    print("Hasil penjumlahan vektor:")
    print(df)

    # Membuat grafik vektor hasil penjumlahan
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=[0, x1], y=[0, y1], mode='lines+markers', name='Vektor Pertama'))
    fig.add_trace(go.Scatter(x=[0, x2], y=[0, y2], mode='lines+markers', name='Vektor Kedua'))
    fig.add_trace(go.Scatter(x=[0, x_jumlah], y=[0, y_jumlah], mode='lines+markers', name='Hasil Penjumlahan'))

    fig.update_layout(
        xaxis=dict(title='Komponen X'),
        yaxis=dict(title='Komponen Y'),
        title='Grafik Vektor Hasil Penjumlahan',
        showlegend=True
    )

    fig.show()

def penjumlahan_paralel_tiga_dimensi():
    x1 = float(input("Masukkan komponen x vektor pertama: "))
    y1 = float(input("Masukkan komponen y vektor pertama: "))
    z1 = float(input("Masukkan komponen z vektor pertama: "))
    x2 = float(input("Masukkan komponen x vektor kedua: "))
    y2 = float(input("Masukkan komponen y vektor kedua: "))
    z2 = float(input("Masukkan komponen z vektor kedua: "))

    x_jumlah = x1 + x2
    y_jumlah = y1 + y2
    z_jumlah = z1 + z2

    besar_vektor = hitung_besar_vektor(x_jumlah, y_jumlah, z_jumlah)
    arah_radian, arah_derajat = hitung_arah_vektor(x_jumlah, y_jumlah, z_jumlah)

    df = pd.DataFrame({
        'Komponen X Vektor Pertama': [x1],
        'Komponen Y Vektor Pertama': [y1],
        'Komponen Z Vektor Pertama': [z1],
        'Komponen X Vektor Kedua': [x2],
        'Komponen Y Vektor Kedua': [y2],
        'Komponen Z Vektor Kedua': [z2],
        'Hasil Penjumlahan X': [x_jumlah],
        'Hasil Penjumlahan Y': [y_jumlah],
        'Hasil Penjumlahan Z': [z_jumlah],
        'Besar Vektor Hasil Penjumlahan': [besar_vektor],
        'Arah Vektor (Radian)': [arah_radian],
        'Arah Vektor (Derajat)': [arah_derajat]
    })

    print("Hasil penjumlahan vektor:")
    print(df)

    # Membuat grafik vektor hasil penjumlahan
    fig = go.Figure()

    fig.add_trace(go.Scatter3d(x=[0, x1], y=[0, y1], z=[0, z1], mode='lines+markers', name='Vektor Pertama'))
    fig.add_trace(go.Scatter3d(x=[0, x2], y=[0, y2], z=[0, z2], mode='lines+markers', name='Vektor Kedua'))
    fig.add_trace(go.Scatter3d(x=[0, x_jumlah], y=[0, y_jumlah], z=[0, z_jumlah], mode='lines+markers', name='Hasil Penjumlahan'))

    fig.update_layout(
        scene=dict(xaxis_title='Komponen X', yaxis_title='Komponen Y', zaxis_title='Komponen Z'),
        title='Grafik Vektor Hasil Penjumlahan',
        showlegend=True
    )

    fig.show()

def vektor_terhadap_sumbu():
    x = float(input("Masukkan komponen x: "))
    y = float(input("Masukkan komponen y: "))
    z = float(input("Masukkan komponen z: "))

    besar_vektor = hitung_besar_vektor(x, y, z)
    arah_radian, arah_derajat = hitung_arah_vektor(x, y, z=z)

    print("Besar vektor:", besar_vektor)
    print("Arah vektor (radian):", arah_radian)
    print("Arah vektor (derajat):", arah_derajat)

    sudut_user = float(input("Masukkan sudut vektor (derajat): "))
    sudut_radian = math.radians(sudut_user)  # Mengubah sudut derajat menjadi radian

    x_baru = besar_vektor * math.cos(sudut_radian)  # Komponen x baru
    y_baru = besar_vektor * math.sin(sudut_radian)  # Komponen y baru

    print("Besar vektor terhadap sumbu x:", x_baru)
    print("Besar vektor terhadap sumbu y:", y_baru)

    # Membuat grafik vektor hasil penjumlahan
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=[0, x], y=[0, y], mode='lines+markers', name='Vektor Awal'))
    fig.add_trace(go.Scatter(x=[0, x_baru], y=[0, y_baru], mode='lines+markers', name='Vektor Baru'))

    fig.update_layout(
        xaxis=dict(title='Komponen X'),
        yaxis=dict(title='Komponen Y'),
        title='Grafik Vektor Terhadap Sumbu X dan Y',
        showlegend=True
    )

    fig.show()

def main():
    print("Menu:")
    print("1. Hitung besar dan arah vektor")
    print("2. Penjumlahan paralel vektor (2 dimensi)")
    print("3. Penjumlahan paralel vektor (3 dimensi)")
    print("4. Hitung vektor terhadap sumbu")
    pilihan = int(input("Masukkan pilihan menu (1/2/3/4): "))

    if pilihan == 1:
        x = float(input("Masukkan komponen x: "))
        y = float(input("Masukkan komponen y: "))

        # If working with 2D vector, set z to 0
        z = 0  # Default value for 2D vector
        besar_vektor = hitung_besar_vektor(x, y, z)
        arah_radian, arah_derajat = hitung_arah_vektor(x, y, z=z)

        print("Besar vektor:", besar_vektor)
        print("Arah vektor (radian):", arah_radian)
        print("Arah vektor (derajat):", arah_derajat)

        # Menampilkan grafik kartesian
        plt.figure(figsize=(6, 6))
        plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='blue', label='Vektor')
        plt.xlim(-max(abs(x), abs(y)) - 1, max(abs(x), abs(y)) + 1)
        plt.ylim(-max(abs(x), abs(y)) - 1, max(abs(x), abs(y)) + 1)
        plt.xlabel('Komponen X')
        plt.ylabel('Komponen Y')
        plt.axhline(0, color='gray', linestyle='dashed')
        plt.axvline(0, color='gray', linestyle='dashed')
        plt.grid()
        plt.legend()
        plt.title('Grafik Vektor')
        plt.show()

    elif pilihan == 2:
        penjumlahan_paralel_dua_dimensi()

    elif pilihan == 3:
        penjumlahan_paralel_tiga_dimensi()

    elif pilihan == 4:
        vektor_terhadap_sumbu()

    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()