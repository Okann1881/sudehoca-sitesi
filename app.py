import streamlit as st
import pandas as pd
import numpy as np
import random
import streamlit as st

# --- GİRİŞ SİSTEMİ BAŞLANGIÇ ---
def giris_yap():
    if "giris_basarili" not in st.session_state:
        st.session_state["giris_basarili"] = False

    if not st.session_state["giris_basarili"]:
        st.title("🔐 Öğretmen Paneli Girişi")
        
        # Kullanıcı adı ve şifre kutuları
        kullanici = st.text_input("Kullanıcı Adı")
        sifre = st.text_input("Şifre", type="password")
        
        if st.button("Giriş Yap"):
            # Buraya istediğin kullanıcı adı ve şifreyi yazabilirsin
            if kullanici == "sudehoca" and sifre == "pi123":
                st.session_state["giris_basarili"] = True
                st.rerun() # Sayfayı yenileyip içeriği gösterir
            else:
                st.error("Hatalı kullanıcı adı veya şifre! ❌")
        return False
    return True

# Eğer giriş yapılmadıysa uygulamanın geri kalanını çalıştırma
if giris_yap():
    # --- SİTE İÇERİĞİ BURADAN İTİBAREN BAŞLAR ---
    st.sidebar.button("Çıkış Yap", on_click=lambda: st.session_state.update({"giris_basarili": False}))
    
    # Buraya daha önce yazdığın tüm kodları (st.title, grafikler, soru üretici vb.) ekle
    st.success("Başarıyla giriş yapıldı. Hoş geldin!")
    
    # Mevcut kodların...
    st.set_page_config(page_title="SUDE HOCANIN MEKANI", page_icon="📐")

    st.balloons() # Site her açıldığında ekranda balonlar uçar! ✨
    st.title("SUDE HOCANIN MEKANI ✨")
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>❤️ Matematiği Sevdiren Panel</h1>", unsafe_allow_html=True)    
    # Yan menü (Sidebar) ekleyelim
    st.sidebar.header("Ayarlar")
    isim = st.sidebar.text_input("Kullanıcı Adı", "Hocam")

    st.write(f"Hoş geldiniz, **{isim}**! Bugün hangi problemi çözüyoruz?")

    # 1. LaTeX ile şık bir formül gösterimi
    st.header("1. Günün Formülü")
    st.latex(r'''
    f(x) = a x^2 + b x + c
    ''')

    # 2. İnteraktif Grafik Çizici
    st.header("2. Grafik Çizici")
    col1, col2 = st.columns(2)

    with col1:
        a = st.slider("a katsayısı", -10, 10, 1)
    with col2:
        b = st.slider("b katsayısı", -10, 10, 0)

    x = np.linspace(-10, 10, 100)
    y = a * (x**2) + b

    chart_data = pd.DataFrame({'x': x, 'y': y})
    st.line_chart(chart_data, x='x', y='y')

    st.success("Grafik başarıyla oluşturuldu!")
    st.header("3. Otomatik Soru Hazırlayıcı 📝")

    # Konu seçimi ekleyebilirsin
    konu = st.selectbox("Bir konu seçin:", ["Toplama/Çıkarma", "Çarpım Tablosu", "Denklem Çözme"])

    if st.button("Yeni Soru Üret"):
        if konu == "Toplama/Çıkarma":
            s1 = random.randint(10, 100)
            s2 = random.randint(10, 100)
            islem = random.choice(["+", "-"])
            sonuc = s1 + s2 if islem == "+" else s1 - s2
        
        st.info(f"Soru: {s1} {islem} {s2} = ?")
        with st.expander("Cevabı Gör"):
            st.write(f"Sonuç: **{sonuc}**")

    elif konu == "Denklem Çözme":
        x_katsayi = random.randint(2, 5)
        cevap = random.randint(1, 10)
        sabit = x_katsayi * cevap
        
        
    # Örnek bir veri tablosu oluşturalım
    data = {
    "Öğrenci": ["Ali", "Ayşe", "Mehmet", "Fatma", "Can"],
    "Sınav 1": [85, 90, 70, 45, 100]
    }
    df = pd.DataFrame(data)

    # Tabloyu düzenleme moduyla göster
    edited_df = st.data_editor(df) 

    # Ortalamayı hesaplayıp göster
    ortalama = edited_df["Sınav 1"].mean()
    st.metric(label="Sınıf Ortalaması", value=f"{ortalama:.2f}")

    # Başarı grafiği
    st.bar_chart(edited_df, x="Öğrenci", y="Sınav 1")
    sozler = [
    "Matematik, evrenin dilidir. - Galileo",
    "Hayat sadece iki şey için güzel; matematiği keşfetme ve öğretme. - Siméon Poisson",
    "Sıfır bir sayıdır, ama hiçbir şeyi temsil etmez!"
    ]
    st.sidebar.divider()
    st.sidebar.write(f"*Günün Sözü:* \n\n {random.choice(sozler)}")