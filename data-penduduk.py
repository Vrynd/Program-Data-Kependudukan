"""
kode pekerjaan :
1 = PNS, 2 = TNI/PORLI, 3 = Pedagang, 4 = Petani, 5 = Nelayan, 6 = Buruh

Kode agama :
1 = Islam, 2 = Protestan, 3 = Katholik, 4 = Hindu, 5 = Budha, 6 = Konghucu, 7 = Agama Lainya
"""

print("*"*10, "DATA KEPENDUDUKAN", "*"*10)
data_penduduk = {
    0:{
        'nik' : 12331,
        'nama' : 'Ana',
        'jenis_kel' : 'P',
        'agama' : 1,
        'status' : 'Belum Kawin',
        'pekerjaan' : 1
    },

    1:{
        'nik' : 12332,
        'nama' : 'Adi',
        'jenis_kel' : 'L',
        'agama' : 2,
        'status' : 'Belum Kawin',
        'pekerjaan' : 2
    },

    2:{
        'nik' : 12333,
        'nama' : 'Leo',
        'jenis_kel' : 'L',
        'agama' : 2,
        'status' : 'Kawin',
        'pekerjaan' : 5
    },

    3:{
        'nik' : 12334,
        'nama' : 'Dewi',
        'jenis_kel' : 'P',
        'agama' : 2,
        'status' : 'Kawin',
        'pekerjaan' : 2
    },

    4:{
        'nik' : 12335,
        'nama' : 'Aryo',
        'jenis_kel' : 'L',
        'agama' : 3,
        'status' : 'Belum Kawin',
        'pekerjaan' : 3
    },

    5:{
        'nik' : 12336,
        'nama' : 'Desti',
        'jenis_kel' : 'P',
        'agama' : 5,
        'status' : 'Belum Kawin',
        'pekerjaan' : 6
    },

    6:{
        'nik' : 12337,
        'nama' : 'Hesti',
        'jenis_kel' : 'P',
        'agama' : 3,
        'status' : 'Kawin',
        'pekerjaan' : 2
    },

    7:{
        'nik' : 12338,
        'nama' : 'Wahyu',
        'jenis_kel' : 'L',
        'agama' : 1,
        'status' : 'Belum Kawin',
        'pekerjaan' : 1
    },

    8:{
        'nik' : 12339,
        'nama' : 'Kukuh',
        'jenis_kel' : 'L',
        'agama' : 2,
        'status' : 'Kawin',
        'pekerjaan' : 2
    },

    9:{
        'nik' : 12310,
        'nama' : 'Farajahwa',
        'jenis_kel' : 'P',
        'agama' : 4,
        'status' : 'Belum Kawin',
        'pekerjaan' : 3
    },

    10:{
        'nik' : 12311,
        'nama' : 'Mikahel',
        'jenis_kel' : 'L',
        'agama' : 2,
        'status' : 'Kawin',
        'pekerjaan' : 1
    },

    11:{
        'nik' : 12312,
        'nama' : 'Dicky',
        'jenis_kel' : 'L',
        'agama' : 1,
        'status' : 'Belum Kawin',
        'pekerjaan' : 2
    },

    12:{
        'nik' : 12313,
        'nama' : 'Prasetyo',
        'jenis_kel' : 'L',
        'agama' : 1,
        'status' : 'Kawin',
        'pekerjaan' : 4
    },

    13:{
        'nik' : 12314,
        'nama' : 'Monica',
        'jenis_kel' : 'P',
        'agama' : 2,
        'status' : 'Belum Kawin',
        'pekerjaan' : 2
    },

    14:{
        'nik' : 12315,
        'nama' : 'Utomo',
        'jenis_kel' : 'L',
        'agama' : 1,
        'status' : 'Kawin',
        'pekerjaan' : 4
    }
}

# Menampilkan Semua data Penduduk
def tampilkanData():
    for id, info in data_penduduk.items():
        print("-"*30)
        print("ID Penduduk :", id)
        print("Nik :", info['nik'])
        print("Nama :", info['nama'])
        print("Jenis Kelamin :", info['jenis_kel'])
        print("Agama :", info['agama'])
        print("Status :", info['status'])
        print("Pekerjaan :", info['pekerjaan'])
tampilkanData()
print("="*30)

# Mencari data penuduk tertentu
def cariData():
    # Sebagai Perhitungan
    perempuanBelum_kawin = 0
    perempuanTidak_islam = 0
    lakiLaki_PNS = 0
    lakiLaki_petani_nelayan = 0

    # Mencari Data Penduduk Tertentu
    for data in data_penduduk.values():
        if data['jenis_kel'] == 'P' and data['status'] == 'Belum Kawin':
            perempuanBelum_kawin += 1
        if data['jenis_kel'] == 'P' and data['agama'] != 1:
            perempuanTidak_islam += 1
        if data['jenis_kel'] == 'L' and data['pekerjaan'] == 1:
            lakiLaki_PNS += 1
        if data['jenis_kel'] == 'L' and data['pekerjaan'] == 4 or data['pekerjaan'] == 5:
            lakiLaki_petani_nelayan += 1

    # Mencetak Data Penduduk Tertentu
    print(f"Jumlah Penduduk Perempuan Yang Belum Kawin : {perempuanBelum_kawin}")
    print(f"Jumlah Penduduk Perempuan Yang Tidak Beragama Islam : {perempuanTidak_islam}")
    print(f"Jumlah Penduduk Laki-Laki Yang Pekerjaanya PNS : {lakiLaki_PNS}")
    print(f"Jumlah Penduduk Laki-Laki Yang Pekerjaanya Petani atau Nelayan : {lakiLaki_petani_nelayan}")
cariData()
print("="*70)

