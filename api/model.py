import numpy as np
import pickle
import pandas as pd
import networkx as nx

# global variables
embeddings = None
G = None
df = None

def load_assets():
    global embeddings, G, df

    embeddings = np.load("embeddings.npy")
    G = pickle.load(open("graph.pkl", "rb"))
    df = pd.read_csv("profiles.csv")

def find_path(source_idx, target_idx):
    try:
        path = nx.shortest_path(G, source=int(source_idx), target=int(target_idx))

        result = []
        for node in path:
            result.append({
                "index": int(node),
                "company": str(df.iloc[node]["company_name"]),
                "title": str(df.iloc[node]["title"])
            })

        return result

    except Exception as e:
        return {"error": str(e)}