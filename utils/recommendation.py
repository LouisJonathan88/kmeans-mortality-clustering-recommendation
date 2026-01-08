def get_recommendation(jenis_kematian, cluster_label):
    data_rekomendasi = {
        "KEMATIAN BALITA": {
            "Risiko Tinggi": "⚠️ PERINGATAN: Diperlukan peningkatan upaya pencegahan secara komprehensif melalui penguatan program imunisasi dasar lengkap, pemantauan status gizi balita secara berkala, serta perbaikan sanitasi dan kebersihan lingkungan. Dominasi kategori lain-lain menunjukkan perlunya pendekatan preventif menyeluruh untuk menekan berbagai faktor risiko yang tidak terklasifikasi secara spesifik.",
            "Risiko Rendah": "✅ AMAN: Pemantauan kesehatan balita secara berkala tetap perlu dilakukan, khususnya melalui deteksi dini penyakit infeksi seperti pneumonia dan diare, pemantauan pertumbuhan, serta pemeliharaan cakupan imunisasi. Langkah ini bertujuan menjaga kondisi kesehatan balita agar tetap terkendali dan mencegah peningkatan risiko kematian."
        },
        "KEMATIAN IBU": {
            "Risiko Tinggi": "⚠️ PERINGATAN: Diperlukan penguatan layanan antenatal care (ANC) secara intensif, khususnya untuk deteksi dan pengelolaan hipertensi serta pencegahan komplikasi pendarahan. Selain itu, persalinan harus ditangani oleh tenaga kesehatan terlatih dengan sistem rujukan yang cepat dan efektif guna menekan risiko kematian ibu.",
            "Risiko Rendah": "✅ AMAN: Pemantauan kesehatan ibu secara berkelanjutan serta edukasi terkait kondisi medis seperti gangguan darah dan metabolik tetap diperlukan. Upaya ini mencakup skrining rutin, pengendalian penyakit penyerta, serta peningkatan kesadaran ibu terhadap tanda bahaya selama kehamilan."
        },
        "KEMATIAN POST-NEO": {
            "Risiko Tinggi": "⚠️ PERINGATAN: Diperlukan perawatan neonatal yang lebih intensif melalui pemantauan kondisi bayi baru lahir, peningkatan kualitas layanan kesehatan neonatal, serta deteksi dini terhadap komplikasi pasca-kelahiran. Dominasi penyebab lain-lain menunjukkan perlunya pendekatan komprehensif dalam perawatan neonatal.",
            "Risiko Rendah": "✅ AMAN: Monitoring rutin layanan neonatal tetap perlu dilakukan, terutama untuk mendeteksi dan menangani penyakit infeksi serta gangguan pencernaan sejak dini. Pemantauan ini bertujuan menjaga stabilitas kondisi kesehatan bayi pasca-neonatal."
        },
        "LAHIR MATI": {
            "Risiko Tinggi": "⚠️ PERINGATAN: Peningkatan kualitas layanan antenatal dan persalinan sangat diperlukan, khususnya dalam pemantauan pertumbuhan janin, pencegahan berat badan lahir rendah, serta penanganan asfiksia saat persalinan. Kesiapan fasilitas dan tenaga kesehatan menjadi faktor kunci dalam menurunkan risiko lahir mati.",
            "Risiko Rendah": "✅ AMAN: Pemantauan kehamilan rutin melalui layanan antenatal care tetap diperlukan, termasuk skrining kelainan janin, pencegahan infeksi maternal, serta pemenuhan imunisasi ibu hamil. Langkah ini bertujuan menjaga kondisi kehamilan tetap stabil dan mencegah komplikasi yang berpotensi menyebabkan lahir mati."
        }
    }

    # Ambil berdasarkan jenis kematian, jika tidak ada pakai kategori default
    kategori = data_rekomendasi.get(jenis_kematian, {})
    return kategori.get(cluster_label, "Rekomendasi umum: Tingkatkan koordinasi antar fasilitas kesehatan dan edukasi pola hidup sehat kepada masyarakat.")