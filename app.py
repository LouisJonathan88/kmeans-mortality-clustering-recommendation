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
            ["Risiko Tinggi", "Risiko Rendah"]
        )

        hasil = pivot[pivot['cluster_label'] == cluster_pilihan]

        # ================= OUTPUT =================
        col1, col2 = st.columns([1.2, 0.8])

        with col1:
            st.subheader(f"Visualisasi Wilayah: {cluster_pilihan}")

            kab_sum = hasil.drop(columns=['cluster', 'cluster_label']).sum()
            top_kab = kab_sum.sort_values(ascending=False).head(5)

            tabel_kabupaten = top_kab.reset_index()
            tabel_kabupaten.columns = ['Nama Kabupaten/Kota', 'Jumlah Kematian']

            color_scale = "Reds" if cluster_pilihan == "Risiko Tinggi" else "Greens"

            fig = px.bar(
                tabel_kabupaten,
                x='Nama Kabupaten/Kota',
                y='Jumlah Kematian',
                color='Jumlah Kematian',
                color_continuous_scale=color_scale
            )
            fig.update_layout(coloraxis_showscale=False)

            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("Detail Cluster")

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
            st.write("**5 Wilayah Teratas:**")
            st.table(tabel_kabupaten)

        # ================= REKOMENDASI =================
        st.markdown("---")
        rekomendasi = get_recommendation(jenis_kematian, cluster_pilihan)

        st.write("### 💡 Rekomendasi Pencegahan")

        if cluster_pilihan == "Risiko Tinggi":
            st.error(rekomendasi)
        else:
            st.success(rekomendasi)

    else:
        st.warning("Data tidak tersedia untuk filter tersebut.")
