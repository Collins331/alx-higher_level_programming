#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    # Check  if n <= 0
    if n <= 0:
        return []

    # Initializing the first row of the Pascal's triangle.
    triangles = [[1]]

    while len(triangles) != n:
        # Assigning the last row of triangles to tri
        tri = triangles[-1]

        # Create a new list tri and append '1' as the first element
        tmp = [1]

        # Using a for-loop to create the Pascal's triangle
        for i in range(len(tri) - 1):
            # This is where the magic happens:
            # Add the current element to the next element and append it to tmp
            tmp.append(tri[i] + tri[i + 1])
        # Adding 1 to the end of tmp
        tmp.append(1)

        # Appending tmp to the end of triangles
        triangles.append(tmp)

    # Return our Pascal's triangle.
    return triangles
