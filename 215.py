#!/usr/bin/python
# -*- coding: utf-8 -*-

# Consider the problem of building a wall out of 2×1 and 3×1 bricks (horizontal×vertical dimensions) such that, for extra strength, the gaps between horizontally-adjacent bricks never line up in consecutive layers, i.e. never form a "running crack".

# For example, the following 9×3 wall is not acceptable due to the running crack shown in red:

# There are eight ways of forming a crack-free 9×3 wall, written W(9,3) = 8.

# Calculate W(32,10).

#Answer:
    #806844323190414

from mathplus import timer, memorize


@timer
def pe(M, N):
    @memorize
    def make_line(length):
        if length < 2:
            return []
        if length in (2, 3):
            return [(length, )]
        ret2 = [l + (length, ) for l in make_line(length - 2)]
        ret3 = [l + (length, ) for l in make_line(length - 3)]
        return ret2 + ret3

    lines = make_line(M - 2) + make_line(M - 3)
    line_cnt = len(lines)
    for i, l in enumerate(lines):
        lines[i] = set(l)
    joints = [0] * line_cnt

    for i1, l1 in enumerate(lines):
        joints[i1] = d = []
        for i2, l2 in enumerate(lines):
            for p in l2:
                if p in l1:
                    break
            else:
                d.append(i2)

    w_m_k = [1] * line_cnt

    for k in range(N - 1):
        new_w = [0] * line_cnt
        for i1 in range(line_cnt):
            for i2 in joints[i1]:
                new_w[i1] += w_m_k[i2]
        w_m_k = new_w

    return sum(w_m_k)


# print(pe(9, 3))
print(pe(32, 10))
