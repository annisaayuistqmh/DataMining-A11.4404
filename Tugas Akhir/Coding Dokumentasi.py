import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Tahapan Eksperimen:
# 1. Eksplorasi Data
url = "www.kaggle.com/datasets/vijayuv/onlineretail"
df = pd.read_csv(url, encoding="unicode_escape")

# Menampilkan beberapa baris pertama dataset
print(df.head())

# Informasi tentang tipe data dan nilai-nilai yang hilang
print(df.info())

# 2. Pembersihan Data
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Preprocessing Data
data = df[['StockCode', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID']]
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

# 3. Analisis Pola Pembelian
top_products = data['StockCode'].value_counts().head(10)
print("Produk yang paling sering dibeli:")
print(top_products)

# Analisis asosiasi (jika ditambahkan) untuk mencari keterkaitan antara produk berdasarkan pola pembelian

# Tren Belanja Berdasarkan Waktu
data['YearMonth'] = data['InvoiceDate'].dt.to_period('M')
shopping_trends = data.groupby('YearMonth')['Quantity'].sum()

# Visualisasi tren belanja berdasarkan waktu
plt.figure(figsize=(10, 6))
plt.plot(shopping_trends.index, shopping_trends, marker='o', linestyle='-')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Barang Terbeli')
plt.title('Tren Belanja Pelanggan Berdasarkan Waktu')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 4. Segmentasi Pelanggan
# Preprocessing untuk K-means Clustering
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data[['Quantity', 'UnitPrice']])

# Menentukan jumlah kluster yang optimal dengan Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
    kmeans.fit(data_scaled)
    wcss.append(kmeans.inertia_)

# Plot Elbow Method
plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), wcss, marker='o')
plt.xlabel('Jumlah Kluster')
plt.ylabel('Within-Cluster Sum of Squares (WCSS)')
plt.title('Elbow Method untuk Menentukan Jumlah Kluster Optimal')
plt.grid(True)
plt.show()

# Berdasarkan Elbow Method, pilih jumlah kluster yang optimal
n_clusters = 4
kmeans = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=300, n_init=10, random_state=42)
data['Cluster'] = kmeans.fit_predict(data_scaled)

# 5. Evaluasi dan Interpretasi
silhouette_avg = silhouette_score(data_scaled, data['Cluster'])
print(f"Silhouette Score untuk jumlah kluster {n_clusters}: {silhouette_avg}")

# Visualisasi hasil clustering
plt.figure(figsize=(10, 6))
for i in range(n_clusters):
    cluster_data = data[data['Cluster'] == i]
    plt.scatter(cluster_data['Quantity'], cluster_data['UnitPrice'], label=f'Cluster {i+1}')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='*', label='Centroids')
plt.xlabel('Quantity (Standarized)')
plt.ylabel('UnitPrice (Standarized)')
plt.title('Hasil Clustering dengan K-means')
plt.legend()
plt.grid(True)
plt.show()

# 6. Kesimpulan
# Merangkum hasil eksperimen dan memberikan rekomendasi bisnis berdasarkan analisis pola pembelian yang telah dilakukan
