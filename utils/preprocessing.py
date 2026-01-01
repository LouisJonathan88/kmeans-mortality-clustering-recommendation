import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df, tahun, jenis_kematian):
    df_filt = df[(df['tahun'] == tahun) & (df['jenis_kematian'] == jenis_kematian)]
    
    if df_filt.empty:
        return pd.DataFrame(), None

    df_group = df_filt.groupby(['penyebab_kematian', 'nama_kabupaten_kota'])['jumlah_kematian'].sum().reset_index()
    
    pivot = df_group.pivot(
        index='penyebab_kematian',
        columns='nama_kabupaten_kota',
        values='jumlah_kematian'
    ).fillna(0)

    scaler = StandardScaler()
    X = scaler.fit_transform(pivot)

    return pivot, X