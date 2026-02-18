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


if __name__ == "__main__":
    n = int(input())
    genealogy_tree = defaultdict(list)
    for _ in range(n):
        line = input()
        parent, child = line.split()
        genealogy_tree[parent].append(child)
        
    target_name = input()
    print(count_descendants_recursive(genealogy_tree, target_name))
