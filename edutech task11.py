import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Load dataset
df = pd.read_csv("C:/Users/hp/OneDrive/Desktop/datasets/Mall_Customers.csv")
print(df.head())
print(df.shape)

# 2. RFM Analysis ke liye columns select karo
# Yahan Age, Annual Income, Spending Score use karenge
rfm = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

# 3. Scaling karo
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

# 4. Elbow Method - best K find karo
inertia = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(rfm_scaled)
    inertia.append(km.inertia_)

plt.figure(figsize=(8, 4))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method - Best K')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.savefig('elbow_plot.png')
plt.show()

# 5. K-Means with K=5
km = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = km.fit_predict(rfm_scaled)

# 6. Cluster Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x=df['Annual Income (k$)'],
    y=df['Spending Score (1-100)'],
    hue=df['Cluster'],
    palette='Set1'
)
plt.title('Customer Segments')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score')
plt.savefig('cluster_plot.png')
plt.show()

# 7. Segment Profiles
segment_summary = df.groupby('Cluster')[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']].mean()
print(segment_summary)
segment_summary.to_csv('segment_report.csv', index=True)

print("Done! Plots and report saved.")