# coding=utf-8
def between(beg, end, mid):
    # 判断mid位于beg和end之间
    return end > mid >= beg or end < mid <= beg


def slice(array, begin, end, delta):
    if delta == 0:
        return []

    if begin < 0:
        begin += len(array)
    if end < 0:
        end += len(array)
    # 如果转化完成之后依然不在合法范围内，则返回空列表
    if begin < 0 and end < 0 or begin >= len(array) and end >= len(array):
        return []

    # 如果方向不同，则返回空列表
    if (end - begin) * delta <= 0:
        return []

    # 将越界的部分进行裁剪,begin太小，或者end太长
    beg = max(0, min(begin, len(array) - 1))
    end = max(-1, min(end, len(array)))

    result = []
    mid = beg
    while between(beg, end, mid):
        result.append(array[mid])
        mid += delta

    return result


if __name__ == '__main__':
    array = [1, 2, 3]
    new_array = slice(array, -99, 200, 1)
    for i in new_array:
        print i