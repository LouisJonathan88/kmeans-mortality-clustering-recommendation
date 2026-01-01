def get_recommendation(jenis_kematian, cluster_label):
    data_rekomendasi = {
        "KEMATIAN BALITA": {
            "Risiko Tinggi": "⚠️ PERINGATAN: Peningkatan imunisasi, pemantauan gizi balita, serta perbaikan sanitasi lingkungan.",
            "Risiko Sedang": "ℹ️ INFO: Edukasi orang tua dan pencegahan penyakit menular.",
            "Risiko Rendah": "✅ AMAN: Monitoring kesehatan balita secara berkala."
        },
        "KEMATIAN IBU": {
            "Risiko Tinggi": "⚠️ PERINGATAN: Peningkatan layanan ANC (Antenatal Care/Pemeriksaan Kehamilan), persalinan oleh tenaga medis, dan rujukan cepat.",
            "Risiko Sedang": "ℹ️ INFO: Pemeriksaan kehamilan rutin dan edukasi kesehatan ibu.",
            "Risiko Rendah": "✅ AMAN: Pemantauan dan edukasi lanjutan."
        },
        "KEMATIAN POST-NEO": {
            "Risiko Tinggi": "⚠️ PERINGATAN: Perawatan neonatal intensif dan deteksi dini komplikasi.",
            "Risiko Sedang": "ℹ️ INFO: Peningkatan pemantauan bayi baru lahir.",
            "Risiko Rendah": "✅ AMAN: Monitoring rutin layanan neonatal."
        },
        "LAHIR MATI": {
            "Risiko Tinggi": "⚠️ PERINGATAN: Peningkatan kualitas layanan antenatal dan persalinan.",
            "Risiko Sedang": "ℹ️ INFO: Deteksi dini risiko kehamilan.",
            "Risiko Rendah": "✅ AMAN: Pemantauan kehamilan rutin."
        }
    }

    # Ambil berdasarkan jenis kematian, jika tidak ada pakai kategori default
    kategori = data_rekomendasi.get(jenis_kematian, {})
    return kategori.get(cluster_label, "Rekomendasi umum: Tingkatkan koordinasi antar fasilitas kesehatan dan edukasi pola hidup sehat kepada masyarakat.")