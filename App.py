import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center; color: black;'>Milenial, Generasi Tak Berumah?</h1>", unsafe_allow_html=True)
st.markdown("---")

st.write("Streamlit App by [Aldhi Prambudi](https://www.linkedin.com/in/aldhi-prambudi-9111501b7/)")

awal = st.container()

with awal:
    st.write("""
             Milenial adalah istilah yang digunakan untuk menyebut orang yang lahir antara tahun 1980 - 1996. orang termuda dari generasi ini baru lulus dari kuliah dan sedang meniti karir. Sedangkan beberapa orang yang tergolong sudah tua, sudah mapan dan sudah berkeluarga. 
             Dengan adanya keluarga, tentunya memerlukan tempat untuk tinggal yaitu memiliki rumah. Rumah atau suatu tempat untuk ditinggali sudah menjadi kebutuhan primer ynag perlu dipenuhi.
             Akan tetapi ada suatu permasalahan yang menyangkut dengan kemampuan generasi milenial untuk memiliki suatu rumah.
             """)

btn1, btn2 = st.columns([1.5,2.5])
with btn1:
    st.write("""
             Berdasarkan berita yang dimuat di laman [Bisnis.com](https://ekonomi.bisnis.com/read/20210929/47/1448530/survei-btn-ungkap-alasan-milenial-belum-beli-rumah), melaporkan hasil survei yang dilakukan oleh BTN yang mengangkat tema alasan milenial belum beli membeli rumah.
             Grafik disamping menunjukkan hasil dari survei.
             """)
with btn2:
    btn = Image.open('.\Milenial.png')
    st.image(btn, caption='Survei BTN Ungkap Alasan Milenial Belum Beli Rumah')

upah1, upah2 = st.columns([2.5,1.5])
with upah1:
    upah = Image.open('.\Upah.png')
    st.image(upah)
    st.write("""
             [Persentase kenaikan Upah Minimum Kota Bandung](https://www.linovhr.com/umr-bandung-terbaru/)
             """)
with upah2:
    st.write("""
            Jawaban yang diberikan hampir semuanya berkaitan tentang keadaan ekonomi kaum milenial. Keadaan ekonomi dari kaum milenial bisa dihitung dengan menggunakan data upah minimum di Indonesia. Dilansir dari
            [KEPUTUSAN GUBERNUR JAWA BARAT NOMOR: 561/Kep.732-Kesra/2021 TENTANG UPAH MINIMUM KABUPATEN/KOTA DI DAERAH PROVINSI JAWA BARAT TAHUN 2022](https://disnakertrans.jabarprov.go.id/produk_hukum/id/378), Upah Minimum 2022 di Jawa barat khusunya di Bandung sebesar Rp. 3.774.860.
            Terdapat kenaikan dari tahun tahun sebelumnya, akan tetapi kenaikannya tidak terlalu signifikan. Sedangkan besar biaya hidup di Bandung berkisar Rp. 1.448.049 - Rp.5.571.254, dilansir dari Survei Biaya Hidup yang di paparkan oleh [rumah.com](https://www.rumah.com/areainsider/bandung/article/perkiraan-biaya-hidup-di-bandung-12546)
            """)

rumah = st.container()

with rumah:
    