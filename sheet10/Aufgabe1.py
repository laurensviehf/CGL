import numpy as np
import itertools
import matplotlib.pyplot as plt

n = 10
np.random.seed(42) # Für reproduzierbare Ergebnisse
points = np.random.rand(n, 2)

def total_path_length(path_indices, points):
    """Berechnet die Gesamtlänge eines Pfades[cite: 21]."""
    dist = 0
    for i in range(len(path_indices) - 1):
        p1 = points[path_indices[i]]
        p2 = points[path_indices[i+1]]
        dist += np.sqrt(np.sum((p1 - p2)**2))
    return dist

# 2. Alle Permutationen berechnen 
def solve_tsp(points):
    n = len(points)
    indices = list(range(n))
    
    # Optimierung: Fixiere den ersten Punkt, um Permutationen auf (n-1)! zu reduzieren
    start_node = indices[0]
    rest_nodes = indices[1:]
    
    min_length = float('inf')
    best_path = None
    
    for p in itertools.permutations(rest_nodes):
        current_path = [start_node] + list(p)
        current_length = total_path_length(current_path, points)
        
        if current_length < min_length:
            min_length = current_length
            best_path = current_path
            
    return best_path, min_length

best_path, min_len = solve_tsp(points)

plt.figure(figsize=(8, 6))
path_points = points[best_path]
plt.plot(path_points[:, 0], path_points[:, 1], 'ro-', label=f'Kürzester Pfad (L={min_len:.2f})')
plt.scatter(points[:, 0], points[:, 1], color='blue', zorder=5)
for i, txt in enumerate(range(n)):
    plt.annotate(txt, (points[i, 0], points[i, 1]), size=12, fontweight='bold')

plt.title(f"TSP Lösung für n={n}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()