# Import libraries for graph operations and data handling
import numpy as np
import pickle
import pandas as pd
import networkx as nx

# Global variables to store loaded data
embeddings = None  # Profile embeddings for similarity matching
G = None  # Network graph for path finding
df = None  # Profile data DataFrame

# Load all required data files into memory
def load_assets():
    global embeddings, G, df

    # Load pre-computed embeddings from numpy file
    embeddings = np.load("embeddings.npy")
    # Load network graph from pickle file
    G = pickle.load(open("graph.pkl", "rb"))
    # Load profile data from CSV file
    df = pd.read_csv("profiles.csv")

# Find shortest path between two profiles using NetworkX graph algorithm
def find_path(source_idx, target_idx):
    try:
        # Calculate shortest path using Dijkstra's algorithm
        path = nx.shortest_path(G, source=int(source_idx), target=int(target_idx))

        # Build result with profile details for each node in path
        result = []
        for node in path:
            result.append({
                "index": int(node),
                "company": str(df.iloc[node]["company_name"]),
                "title": str(df.iloc[node]["title"])
            })

        return result

    except Exception as e:
        # Return error if path cannot be found
        return {"error": str(e)}