def list_relationship(A, B):
    if A == B:
        return "A and B are equal"

    if is_sublist(B, A):
        return "A is a superlist of B"

    if is_sublist(A, B):
        return "A is a sublist of B"

    return "A and B are unequal"


def is_sublist(sub, main):
    for i in range(len(main) - len(sub) + 1):
        if main[i:i + len(sub)] == sub:
            return True
    return False


print(list_relationship([], []))
print(list_relationship([1, 2, 3], []))
print(list_relationship([], [1, 2, 3]))
print(list_relationship([1, 2, 3], [1, 2, 3, 4, 5]))
print(list_relationship([3, 4, 5], [1, 2, 3, 4, 5]))
print(list_relationship([3, 4], [1, 2, 3, 4, 5]))
print(list_relationship([1, 2, 3], [1, 2, 3]))
print(list_relationship([1, 2, 3, 4, 5], [2, 3, 4]))
print(list_relationship([1, 2, 4], [1, 2, 3, 4, 5]))
print(list_relationship([1, 2, 3], [1, 3, 2]))
