from collections import deque
#  Understand

# Plan
# # Graphs Problem solving
# ## Translate the problem


def earliest_ancestor(ancestors, starting_node):
    q = deque([[starting_node]])

    while len(q) > 0:
        generation = q.popleft()
        print('PRINT', generation)

        new_generation = []

        for node in generation:
            new_generation.extend(
                [p for p, child in ancestors if child == node])

        if new_generation:
            q.extend([new_generation])
        else:
            return min(generation) if min(generation) != starting_node else -1


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 1))
