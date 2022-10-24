import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import numpy_financial as npfStr
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import streamlit as st
from PIL import Image
import plotly.graph_objects as go
from plotly.subplots import make_subplots


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
    btn = Image.open('src/Milenial.png')
    st.image(btn, caption='Survei BTN Ungkap Alasan Milenial Belum Beli Rumah')

upah1, upah2 = st.columns([2.5,1.5])
with upah1:
    upah = Image.open('src//Upah.png')
    st.image(upah)
    st.write("""
             [Persentase kenaikan Upah Minimum Kota Bandung](https://www.linovhr.com/umr-bandung-terbaru/)
             """)
with upah2:
    st.write("""
            Jawaban yang diberikan hampir semuanya berkaitan tentang keadaan ekonomi kaum milenial. Keadaan ekonomi dari kaum milenial bisa dihitung dengan menggunakan data upah minimum di Indonesia. Dilansir dari
            [KEPUTUSAN GUBERNUR JAWA BARAT NOMOR: 561/Kep.732-Kesra/2021 TENTANG UPAH MINIMUM KABUPATEN/KOTA DI DAERAH PROVINSI JAWA BARAT TAHUN 2022](https://disnakertrans.jabarprov.go.id/produk_hukum/id/378).
            """)
st.write("""Upah Minimum 2022 di Jawa barat khusunya di Bandung sebesar Rp. 3.774.860.
            Terdapat kenaikan dari tahun tahun sebelumnya, akan tetapi kenaikannya tidak terlalu signifikan. Sedangkan besar biaya hidup di Bandung berkisar Rp. 1.448.049 - Rp.5.571.254, dilansir dari Survei Biaya Hidup yang di paparkan oleh [rumah.com](https://www.rumah.com/areainsider/bandung/article/perkiraan-biaya-hidup-di-bandung-12546)""")

#Load Data
df = pd.read_csv('src/Rumah123.csv', usecols=['Harga', 'KT', 'KM', 'Garasi', 'LT', 'LB'])
#Cleansing set limit KT, KM, Garasi <= 5
df.isnull().sum()
df = df.dropna(subset=['Harga', 'KT', 'KM'])
df = df[df.KT <= 5.0]
df = df[df.KM <= 5.0]
df = df[df.Garasi <= 5.0]
#min,mean,max
minim = df['Harga'].min().round(2)
rata = df['Harga'].mean().round(2)
maksi = df['Harga'].max().round(2)

rumah1 = st.container()
with rumah1:
    st.subheader("Data Harga Jual Rumah di Bandung Yang bersumber dari [rumah123.com](https://www.rumah123.com/jual/bandung/rumah/?page=1#qid~dac46e90-0fc8-4df5-9936-af1ebefcb4a2)")
    st.write("""
             Untuk memperkuat jawaban yang sudah diberikan dari kaum milenial pada survei BTN. Berikut data harga rumah di Bandung, dengan menggunakan batasan jumlah kamar tidur, kamar mandi, dan garasi berjumlah <= 5
             """)

    rum1, rum2 = st.columns([2.5,2.5])
    with rum1:
        st.dataframe(df.style.format("{:.2f}"))
        st.caption("""
                   Keterangan: Harga menggunakan satuan $ dengan exchange rate = 15498.50:1.
                               LT dan LB menggunakan satuan m^2
                   """)
    
    with rum2:  
        option = st.selectbox(
            'How would you like to be contacted?',
            ('Harga Minimal', 'Rata rata', 'Harga Maksimal'))
        if option in 'Harga Minimal':
            st.write('Harga termurah : $', minim)
            minimrp = (minim*15498.50)
            st.caption('Dalam rupiah sebesar : Rp. ' + str(minimrp))
            rslt_df = df[df['Harga'] == minim]
            st.write('\nFitur lengkap rumah :\n', rslt_df.style.format("{:.2f}"))
        elif option in 'Rata rata':
            st.write('Harga rata rata : $', rata)
            ratarp = (rata*15498.50)
            st.caption('Dalam rupiah sebesar : Rp. ' + str(ratarp))
            rslt_df = df[df['Harga'] == rata]
            st.write('\nFitur lengkap rumah :\n', rslt_df.style.format("{:.2f}"))
        elif option in 'Harga Maksimal':
            st.write('Harga termahal : $', maksi)
            maksirp = (maksi*15498.50)
            st.caption('Dalam rupiah sebesar : Rp. ' + str(maksirp))
            rslt_df = df[df['Harga'] == maksi]
            st.write('\nFitur rumah :\n', rslt_df.style.format("{:.2f}"))
            
    corr = st.container()
    with corr:
        corr1, corr2 = st.columns([3,3])
        with corr1:
            st.write("""
                    Berdasar data yang sudah diambil dari [rumah123.com](https://www.rumah123.com/jual/bandung/rumah/?page=1#qid~dac46e90-0fc8-4df5-9936-af1ebefcb4a2) dengan data yang diambil adalah "Harga, KT, KM, Garasi, LT dan LB".
                    Diperoleh tabel korelasi matriks disamping, bisa ditarik kesimpulan bahwa luas tanah menjadi penentu utama dari penentuan harga suatu rumah.
                    Kesimpulan bahwa luas tanah memiliki hubungan sebab akibat dengan harga rumah didasari dari artikel yang dimuat oleh [money.kompas.com](https://money.kompas.com/read/2021/10/23/133000526/5-cara-menentukan-harga-jual-rumah-yang-tepat?page=all)
                    """)
        with corr2:
            st.dataframe(df.corr().style.format("{:.2f}"))
        

rumah2 = st.container()

with rumah2:
    st.write("""
             Setelah mengetahui semua data diatas, kaum milenial setidaknya bisa memiliki gambaran mengenai harga rata rata suatu rumah di daerah Bandung.
             Dan untuk memudahkan mengetahui lebih rinci harga rumah yang diinginkan bisa melalui website jual beli rumah, atau bisa melakukan prediksi harga tersendiri berdasarkan data rumah diatas menggunakan 
             tools sederhana dibawah ini:
             """)
    
    pred1, pred2 = st.columns([2.5,2.5])
    
    with pred1:
        #prediction
        x = df.drop(columns='Harga')
        y = df['Harga']
        #train
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=5)
        print(x_train.shape)
        print(y_train.shape)
        print(x_test.shape)
        print(y_test.shape)
        #model
        model = LinearRegression()
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        model.score(x_test, y_test)
        #inputdata
        st.subheader("Prediksi harga rumah sesuai keinginan fitur yang diperlukan kaum milenial")
        kam_tid = st.slider('Kamar Tidur', 1, 5)
        kam_man = st.slider('Kamar Mandi', 1, 5)
        garasi = st.slider('Garasi', 0, 5)
        luas_tan = st.number_input('Luas Tanah')
        luas_bang = st.number_input('Luas Bangunan')
    with pred2:
        if st.button('Hitung'):
            st.write("""Dengan fitur rumah sebagai berikut: \n""")
            st.write('Jumlah kamar tidur : '+str(kam_tid))
            st.write('Jumlah kamar mandi : '+str(kam_man))
            st.write('Jumlah garasi : '+str(garasi))
            st.write('Luas tanah : '+str(luas_tan)+' m^2')
            st.write('Luas bangunan : '+str(luas_bang)+' m^2')
            prediksi = model.predict([[kam_tid,kam_man,garasi,luas_tan,luas_bang]])
            st.write('$ '+'%.2f' % prediksi)
            predikrp = prediksi*15498.50
            st.write('Rp. '+'%.2f' % predikrp)
            
rumah3 = st.container()

with rumah3:
    st.header("**Mortgage Details**")
    st.write("""
             Setelah mengetahui harga dari rumah sesuai dengan kriteria yang diinginkan. 
             Berikut ini cara untuk mengetahui hutang/hipotek/mortgage yang perlu dilunasi: 
             """)
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Harga rumah")
        home_value = st.number_input("Harga rumah(Rp.): ", min_value=0.0, format='%f')
        
        st.subheader("Suku bunga pinjaman kredit rumah (0 - 15)%")
        interest_rate = st.number_input("Suku bunga pinjaman kredit rumah(%): ", min_value=0.0, max_value=15.0, format='%f')

    with col2:
        st.subheader("Down Payment (%)")
        down_payment_percent = st.number_input("Down Payment(%): ", min_value=0.0, format='%f')
        
        st.subheader("Tenor (5-30 tahun)")
        payment_years = st.number_input("Tenor (tenor): ", min_value=5, max_value=30, format='%d')
        

    down_payment = home_value* (down_payment_percent / 100)
    loan_amount = home_value - down_payment
    payment_months = payment_years*12
    interest_rate = interest_rate / 100
    periodic_interest_rate = (1+interest_rate)**(1/12) - 1
    monthly_installment = -1*npfStr.pmt(periodic_interest_rate , payment_months, loan_amount)

    st.subheader("**Down Payment:** Rp." + str(round(down_payment,2)))
    st.subheader("**Jumlah hutang:** Rp." + str(round(loan_amount, 2)))
    st.subheader("**Angsuran bulanan:** Rp." + str(round(monthly_installment, 2)))

    st.markdown("---")

    st.header("**Mortgage loan Amortization**")
    principal_remaining = np.zeros(payment_months)
    interest_pay_arr = np.zeros(payment_months)
    principal_pay_arr = np.zeros(payment_months)

    for i in range(0, payment_months):
        
        if i == 0:
            previous_principal_remaining = loan_amount
        else:
            previous_principal_remaining = principal_remaining[i-1]
            
        interest_payment = round(previous_principal_remaining*periodic_interest_rate, 2)
        principal_payment = round(monthly_installment - interest_payment, 2)
        
        if previous_principal_remaining - principal_payment < 0:
            principal_payment = previous_principal_remaining
        
        interest_pay_arr[i] = interest_payment 
        principal_pay_arr[i] = principal_payment
        principal_remaining[i] = previous_principal_remaining - principal_payment
        

    month_num = np.arange(payment_months)
    month_num = month_num + 1

    principal_remaining = np.around(principal_remaining, decimals=2)

    fig = make_subplots(
        rows=2, cols=1,
        vertical_spacing=0.03,
        specs=[[{"type": "table"}],
            [{"type": "scatter"}]
            ]
    )

    fig.add_trace(
            go.Table(
                header=dict(
                        values=['Month', 'Pembayaran pokok(Rp)', 'Pembayaran bunga(Rp)', 'Total tagihan hutang(Rp)']
                    ),
                cells = dict(
                        values =[month_num, principal_pay_arr, interest_pay_arr, principal_remaining]
                    )
                ),
            row=1, col=1
        )

    fig.add_trace(
            go.Scatter(
                    x=month_num,
                    y=principal_pay_arr,
                    name= "Pembayaran pokok"
                ),
            row=2, col=1
        )

    fig.append_trace(
            go.Scatter(
                x=month_num, 
                y=interest_pay_arr,
                name="Pembayaran bunga"
            ),
            row=2, col=1
        )

    fig.update_layout(title='Pembayaran angsuran hutang dalam bulan',
                    xaxis_title='Month',
                    yaxis_title='Amount(Rp)',
                    height= 800,
                    width = 1200,
                    legend= dict(
                            orientation="h",
                            yanchor='top',
                            y=0.47,
                            xanchor= 'left',
                            x= 0.01
                        )
                    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.header("**Home Equity (With Constant Market Value)**")

    cumulative_home_equity = np.cumsum(principal_pay_arr)
    cumulative_interest_paid = np.cumsum(interest_pay_arr)


    fig = go.Figure()
    fig.add_trace(
            go.Scatter(
                x=month_num, 
                y=cumulative_home_equity,
                name="Cumulative Home Equity"
            )
        )

    fig.add_trace(
            go.Scatter(
                x=month_num, 
                y=cumulative_interest_paid,
                name="Cumulative Interest Paid"
            )
        )

    fig.update_layout(title='Cumulative Home Equity Over Time',
                    xaxis_title='Month',
                    yaxis_title='Amount(Rp)',
                    height= 500,
                    width = 1200,
                    legend= dict(
                            orientation="h",
                            yanchor='top',
                            y=0.98,
                            xanchor= 'left',
                            x= 0.01
                        )
                    )


    st.plotly_chart(fig, use_container_width=True)
    st.write("""
             Dengan adanya prediksi harga dan perhitungan sederhana mengenai angsuran rumah diatas, diharapkan bisa meningkatkan daya beli rumah kaum milenial.
             Dan setidaknya para kaum milenial memiliki gambaran yang jelas mengenai harga dan angsuran dari rumah yang ingin dimiliki.
             """)