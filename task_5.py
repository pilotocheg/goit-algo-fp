import colorsys
from task_4 import draw_tree, Node


def generate_colors(n):
    """Генерує градацію кольорів у 16-річній системі від темного до світлого"""
    return [
        "#" + "".join(f"{int(c*255):02X}" for c in colorsys.hsv_to_rgb(0.6, 1, i / n))
        for i in range(n)
    ]


def build_heap_tree(heap_array: list[int]) -> Node:
    nodes = [Node(val) for val in heap_array]

    for i in range(len(heap_array)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(heap_array):
            nodes[i].left = nodes[left_index]
        if right_index < len(heap_array):
            nodes[i].right = nodes[right_index]

    return nodes[0]


def bfs_traversal(root: Node, n):
    queue = [root]
    visited = []
    colors = generate_colors(n)

    while queue:
        node = queue.pop(0)
        visited.append(node)
        node.color = colors[len(visited) - 1]

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    draw_tree(root)


def dfs_traversal(root: Node, n):
    stack = [root]
    visited = []
    colors = generate_colors(n)

    while stack:
        node = stack.pop()
        visited.append(node)
        node.color = colors[len(visited) - 1]

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    draw_tree(root)


if __name__ == "__main__":
    heap_array = [1, 3, 5, 7, 9, 11, 13]
    root = build_heap_tree(heap_array)

    bfs_traversal(root, len(heap_array))
    dfs_traversal(root, len(heap_array))
