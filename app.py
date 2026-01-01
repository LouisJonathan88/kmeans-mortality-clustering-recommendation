import streamlit as st
import pandas as pd
import plotly.express as px

from utils.preprocessing import preprocess_data
from utils.clustering import run_kmeans
from utils.recommendation import get_recommendation

st.set_page_config(page_title="Rekomendasi Pencegahan Kematian Jabar", layout="wide")

st.title("Sistem Rekomendasi Pencegahan Penyebab Kematian di Jawa Barat")
st.markdown("Analisis Clustering Menggunakan Algoritma K-Means")
st.markdown("---")

# ================= LOAD DATA =================
@st.cache_data
def load_data():
    try:
        # Ganti sesuai path file Anda
        return pd.read_csv("data/penyebab_kematian_jabar.csv")
    except Exception as e:
        st.error(f"Gagal memuat data: {e}")
        return None

df = load_data()

if df is not None:
    # ================= SIDEBAR =================
    st.sidebar.header("Filter Data")

    tahun = st.sidebar.selectbox(
        "Pilih Tahun",
        sorted(df['tahun'].unique(), reverse=True)
    )

    jenis_kematian = st.sidebar.selectbox(
        "Pilih Jenis Kematian",
        df['jenis_kematian'].unique()
    )

    # ================= PROCESS =================
    pivot, X = preprocess_data(df, tahun, jenis_kematian)

    if not pivot.empty:
        # ================= CLUSTERING =================
        labels, cluster_map = run_kmeans(pivot, X)

        pivot['cluster'] = labels
        pivot['cluster_label'] = pivot['cluster'].map(cluster_map)

        # ================= PILIH CLUSTER =================
        cluster_pilihan = st.sidebar.selectbox(
            "Pilih Cluster Risiko untuk Lihat Rekomendasi",
            ["Risiko Tinggi", "Risiko Sedang", "Risiko Rendah"]
        )

        hasil = pivot[pivot['cluster_label'] == cluster_pilihan]

        # ================= OUTPUT =================
        col1, col2 = st.columns([1.2, 0.8])

        with col1:
            st.subheader(f"Visualisasi Wilayah: {cluster_pilihan}")
            
            # Hitung Kabupaten Dominan
            kab_sum = hasil.drop(columns=['cluster', 'cluster_label']).sum()
            top_kab = kab_sum.sort_values(ascending=False).head(5)
            
            tabel_kabupaten = top_kab.reset_index()
            tabel_kabupaten.columns = ['Nama Kabupaten/Kota', 'Jumlah Kematian']

            # Logika Warna Grafik
            color_scale = "Reds" if cluster_pilihan == "Risiko Tinggi" else \
                          "Blues" if cluster_pilihan == "Risiko Sedang" else "Greens"

            # Grafik Bar Plotly
            fig = px.bar(
                tabel_kabupaten, 
                x='Jumlah Kematian', 
                y='Nama Kabupaten/Kota',
                orientation='h',
                color='Jumlah Kematian',
                color_continuous_scale=color_scale
            )
            fig.update_layout(
                yaxis={'categoryorder':'total ascending'},
                coloraxis_showscale=False
            )
            st.plotly_chart(
                fig,
                use_container_width=True,
                config={
                    "displayModeBar": False,   
                    "scrollZoom": False       
                }
            )

        with col2:
            st.subheader("Detail Cluster")
            st.write("**Penyebab Kematian dalam Cluster ini:**")

            # Hitung total kematian per penyebab
            penyebab_sum = hasil.drop(columns=['cluster', 'cluster_label']).sum(axis=1)

            tabel_penyebab = (
                penyebab_sum[penyebab_sum > 0]
                .sort_values(ascending=False)
                .reset_index()
                .rename(columns={
                    'penyebab_kematian': 'Penyebab Kematian',
                    0: 'Jumlah Kematian'
                })
            )

            st.dataframe(tabel_penyebab, use_container_width=True)


        # ================= REKOMENDASI =================
        st.markdown("---")
        rekomendasi = get_recommendation(jenis_kematian, cluster_pilihan)
        
        st.write("### 💡 Rekomendasi Pencegahan")
        
        # Logika Warna Box Rekomendasi
        if cluster_pilihan == "Risiko Tinggi":
            st.error(rekomendasi)   # Warna Merah
        elif cluster_pilihan == "Risiko Sedang":
            st.info(rekomendasi)    # Warna Biru
        else:
            st.success(rekomendasi) # Warna Hijau
            
    else:
        st.warning("Data tidak tersedia untuk filter tersebut.")