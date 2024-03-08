def are_orthogonal(vector_one, vector_two):
    return vector_one[0] * vector_two[0] + vector_one[1] * vector_two[1] == 0


print(are_orthogonal((1, 2), (2, 1)))
print(are_orthogonal((2, 1), (-1, 2)))