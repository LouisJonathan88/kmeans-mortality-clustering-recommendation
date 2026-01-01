# K-Means Mortality Clustering Recommendation System

Sistem rekomendasi pencegahan penyebab kematian berbasis **clustering K-Means** menggunakan data **Open Data Jawa Barat**.  
Aplikasi ini mengelompokkan kabupaten/kota berdasarkan kemiripan pola penyebab kematian dan memberikan **rekomendasi pencegahan** sesuai tingkat risiko.

## 📊 Dataset
Dataset yang digunakan berasal dari **Open Data Jawa Barat**.

- Sumber: https://opendata.jabarprov.go.id/id/dataset/jumlah-kematian-berdasarkan-jenis-dan-penyebab-kematian-di-jawa-barat

## 🚀 Cara Menjalankan Aplikasi
1. Clone repository:
   ```bash
   git clone https://github.com/<username>/kmeans-mortality-clustering-recommendation.git

   cd kmeans-mortality-clustering-recommendation
    ```
2. Install dependencies:
   ```bash
    pip install -r requirements.txt
    ```
3. Jalankan aplikasi:
    ```bash
     streamlit run app.py
     ```
## 📋 Requirements
- Python 3.8+
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn