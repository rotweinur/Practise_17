import sys

def get_object_shape(shape_map: dict[str, str], target_object: str) -> str:
    """
    Determines the shape of a specific object.
    Args:
        shape_map (dict[str, str]): Dictionary mapping objects to their shapes.
        target_object (str): The object name.
    Returns:
        str: The shape of the object or original string if unknown.
    """
    return shape_map.get(target_object, target_object)

def solve_task_4() -> None:
    """
    Reads input and prints the result for Task 4.
    """
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
        objects_shapes = {}
        for _ in range(n):
            line = sys.stdin.readline().strip()
            if line:
                parts = line.split()
                shape = parts[0]
                objects = parts[1:]
                for obj in objects:
                    objects_shapes[obj] = shape
        target = sys.stdin.readline().strip()
        print(get_object_shape(objects_shapes, target))
    except ValueError:
        pass

if __name__ == "__main__":
    solve_task_4()