#!/usr/bin/python3
"""Module defines a Pascal's Triangle function."""

def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tria = triangles[-1]
        tmp = [1]
        for i in range(len(tria) - 1):
            tmp.append(tria[i] + tria[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
