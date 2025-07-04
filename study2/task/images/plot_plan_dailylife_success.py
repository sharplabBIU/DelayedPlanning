import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Initialize the graph
G = nx.DiGraph()
fs = 30  # font size

# Add nodes with positions
positions = {
    "start": (0, 3),
    "baby": (-1, 2),
    "toothbrush": (1, 2),
    "bowtie": (-1.5, 1),
    "backpack": (0, 1),
    "car": (1.5, 1),
    "lamp": (-1.5, 0),
    "zebra": (-0.5, 0),
    "cat": (0.5, 0),
    "knight": (1.5, 0)
}

labels = {
    "lamp": "Depth=1",
    "zebra": "Depth=2",
    "knight": "Depth=3",
    "cat": "Depth=3"
}

# Add edges with colors
# edges = [
#     ("start", "toothbrush", "red"),
#     ("start", "baby", "blue"),
#     ("baby", "bowtie", "red"),
#     ("baby", "backpack", "blue"),
#     ("toothbrush", "backpack", "red"),
#     ("toothbrush", "car", "blue"),
#     ("backpack", "lamp", "red"),
#     ("bowtie", "lamp", "blue"),
#     ("bowtie", "knight", "red"),
#     ("car", "cat", "blue"),
#     ("car", "lamp", "red")
# ]

edges = [
    ("start", "toothbrush", "red"),
    ("start", "baby", "blue"),
    ("baby", "bowtie", "red"),
    ("baby", "backpack", "blue"),
    ("toothbrush", "backpack", "red"),
    ("toothbrush", "car", "blue"),
    ("backpack", "lamp", "red"),
    ("bowtie", "lamp", "blue"),
    ("car", "cat", "blue"),
    ("car", "lamp", "red")
]
# Add nodes and edges to the graph
for node in positions:
    G.add_node(node)

# for edge in edges:
#     G.add_edge(edge[0], edge[1], color=edge[2])

# Draw the graph without arrows first
fig, ax = plt.subplots(figsize=(10, 10))
nx.draw(G, pos=positions, with_labels=False, arrows=False, node_size=200, node_color='white', ax=ax)

# Load images and add them to the nodes
def add_image(node, img_path, ax):
    img = mpimg.imread(img_path)
    if "dot" in img_path:
        imagebox = OffsetImage(img, zoom=0.20)
    else:
        imagebox = OffsetImage(img, zoom=0.05)
    ab = AnnotationBbox(imagebox, positions[node], frameon=False)
    ax.add_artist(ab)

images = {
    "start": "dot.png",
    "baby": "dot.png",
    "toothbrush": "dot.png",
    "bowtie": "dot.png",
    "backpack": "greenv.png",
    "car": "dot.png",
    "lamp": "greenv.png",
    "zebra": "dot.png",
    "knight": "dot.png",
    "cat": "redx.png",
    }

for node, img_path in images.items():
    add_image(node, img_path, ax)

# Function to calculate arrow positions
def get_arrow_positions(start_pos, end_pos):
    if start_pos[1] > 2:
        offset = 0.1
        offset2 = 0.35
        start = (start_pos[0], start_pos[1] - offset)
        end = (end_pos[0], end_pos[1] + offset2)
    else:
        offset = 0.35  # Adjust this value to move arrow start and end points to the bottom and top of images
        start = (start_pos[0], start_pos[1] - offset)
        end = (end_pos[0], end_pos[1] + offset)
    return start, end

# Function to highlight the path to a specific end-node
def highlight_path_to_end_node(G, end_node):
    edges_to_highlight = []
    current_node = end_node
    while current_node in G:
        predecessors = list(G.predecessors(current_node))
        if not predecessors:
            break
        predecessor = predecessors[0]
        edge_color = G[predecessor][current_node]['color']
        edges_to_highlight.append((predecessor, current_node, edge_color))
        current_node = predecessor
    return edges_to_highlight

# Specify the end-node to highlight
end_node = "lamp"
highlighted_edges = highlight_path_to_end_node(G, end_node)

# Draw highlighted edges with colors and thicker width
for edge in edges:
    start_pos, end_pos = get_arrow_positions(positions[edge[0]], positions[edge[1]])
    color = edge[2]
    ax.annotate("",
                xy=end_pos, xycoords='data',
                xytext=start_pos, textcoords='data',
                arrowprops=dict(arrowstyle="->", color=color, lw=8, mutation_scale=20), zorder=5)



# Show plot
# plt.title("Decision Tree", fontsize=14, fontweight='bold')
plt.axis('off')
plt.savefig('decision_tree_success.png', dpi=300)
plt.show()
