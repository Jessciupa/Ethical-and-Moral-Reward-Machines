import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score

def vectorize(df):
    """
    Returns N x F Numpy Array representing F dimensions of ACME values
    of N Countries.

    Input: Pandas DataFrame

    Output: Numpy Array
    """
    # Define the indices of the age-related columns
    age_columns_indices = [14, 15]  # Assuming Age [Elderly -> Young]: Estimates and Age [Elderly -> Young]: se

    # Select only the age-related columns
    X = df.values[:, age_columns_indices].astype(float)

    # Normalize Values
    X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

    return X

def clustering_test(df, savefig=True):
    prefs = df.columns[4:]
    X = vectorize(df)

    N = X.shape[0]

    calin_hara_indices = list()
    
    # Number of main clusters (adjust as needed)
    num_main_clusters = 3

    # Hierarchical / Agglomerative with Ward Linkage
    agg_ward = AgglomerativeClustering(n_clusters=num_main_clusters, linkage='ward')
    C = agg_ward.fit_predict(X)

    calin_idx = silhouette_score(X, C)
    calin_hara_indices.append(calin_idx)

    # Calculate mean AMCE score for each cluster
    cluster_info = {}
    for cluster_id in range(num_main_clusters):
        cluster_indices = np.where(C == cluster_id)[0]  # Indices of countries in this cluster
        mean_amce = np.mean(X[cluster_indices], axis=0)  # Mean AMCE score for this cluster
        cluster_info[cluster_id] = mean_amce

    # Create DataFrame to store cluster info
    cluster_df = pd.DataFrame(columns=['Cluster', 'Mean AMCE Score'])
    for cluster_id, mean_amce in cluster_info.items():
        cluster_df = cluster_df.append({'Cluster': cluster_id, 'Mean AMCE Score': mean_amce}, ignore_index=True)

    # Print the DataFrame
    print("Cluster Information:")
    print(cluster_df)

if __name__ == '__main__':
    df = pd.read_csv(r"C:\Source\reward_machines\cultural_cluster_data\moral_machine_exp.csv")  # Adjust the path to your data file
    clustering_test(df)