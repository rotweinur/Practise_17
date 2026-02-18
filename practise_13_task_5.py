import sys
from collections import defaultdict

def count_descendants_recursive(tree: dict[str, list[str]], name: str) -> int:
    """
    Recursively counts the total number of descendants for a given person.
    Args:
        tree (dict[str, list[str]]): Adjacency list representing the family tree.
        name (str): The name of the ancestor.
    Returns:
        int: Total count of descendants.
    """
    if name not in tree:
        return 0
    children = tree[name]
    count = len(children)
    for child in children:
        count += count_descendants_recursive(tree, child)
    return count

def solve_task_5() -> None:
    """
    Reads input and prints the result for Task 5.
    """
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
        genealogy_tree = defaultdict(list)
        for _ in range(n):
            line = sys.stdin.readline().strip()
            if line:
                parent, child = line.split()
                genealogy_tree[parent].append(child)
        target_name = sys.stdin.readline().strip()
        print(count_descendants_recursive(genealogy_tree, target_name))
    except ValueError:
        pass

if __name__ == "__main__":
    solve_task_5()