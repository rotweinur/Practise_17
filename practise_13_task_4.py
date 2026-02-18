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


if __name__ == "__main__":
    n = int(input())
    objects_shapes = {}
    for _ in range(n):
        line = input()
        parts = line.split()
        shape = parts[0]
        objects = parts[1:]
        for obj in objects:
            objects_shapes[obj] = shape
            
    target = input()
    print(get_object_shape(objects_shapes, target))
