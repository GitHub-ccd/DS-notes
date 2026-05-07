# Section 14 — Graph Theory

Graph algorithms, NetworkX, node centrality, clustering, community detection, and graph-based recommendation.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `01_graph_theory_introduction.ipynb` | Section introduction |
| `02_intro_graph_theory.ipynb` | Graphs — vertices, edges, directed vs undirected, weighted graphs |
| `03_networkX_intro.ipynb` | NetworkX — building and analysing graphs in Python |
| `04_networkX_intro_lab.ipynb` | NetworkX lab |
| `05_node_centrality.ipynb` | Degree, betweenness, closeness, and eigenvector centrality |
| `06_node_centrality_lab.ipynb` | Node centrality lab |
| `07_graph_theory_shortest_path.ipynb` | Dijkstra's algorithm and BFS/DFS shortest path |
| `08_graph_theory_shortest_path_lab.ipynb` | Shortest path lab |
| `09_network_clustering.ipynb` | Network clustering and graph cliques |
| `10_network_clustering_lab.ipynb` | Network clustering lab |
| `11_community_detection_lab.ipynb` | Community detection lab |
| `12_recommendation_systems.ipynb` | Graph-based recommendation via bipartite graphs |
| `13_recommendation_systems_lab.ipynb` | Graph recommendation lab |
| `14_graph_theory_recap.ipynb` | Section recap |

## 2026 Context

NetworkX-based graph analysis remains relevant for network science and classical graph algorithms. For **machine learning on graphs**, the field has moved to **Graph Neural Networks (GNNs)**:

- **PyTorch Geometric** (`torch_geometric`) — the dominant GNN library; implements GCN, GAT, GraphSAGE, and hundreds of variants
- **DGL** (Deep Graph Library) — alternative to PyG, supports PyTorch and MXNet backends

GNNs are used for molecular property prediction (drug discovery), fraud detection in transaction graphs, social network analysis, knowledge graphs, and recommendation systems. NetworkX is still used for graph construction and classical algorithms; PyG/DGL are used when you want to learn representations from graph structure.