from sklearn.cluster import KMeans

def run_kmeans(pivot, X, k=3):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)

    # Urutkan berdasarkan total kematian agar mapping risiko konsisten
    cluster_totals = {}
    for c in range(k):
        cluster_totals[c] = pivot.iloc[labels == c].sum().sum()

    sorted_clusters = sorted(cluster_totals.items(), key=lambda x: x[1], reverse=True)
    
    cluster_map = {}
    labels_name = ["Risiko Tinggi", "Risiko Sedang", "Risiko Rendah"]
    for i, (cluster_id, _) in enumerate(sorted_clusters):
        cluster_map[cluster_id] = labels_name[i]

    return labels, cluster_map