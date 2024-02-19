class meaning:
    count = 1

    def __init__(self, position, value):
        self.value = value
        self.range = value
        self.position = position

def add_atm_distances(seg_lis: list[meaning]):
    new_distance = []

    for i in seg_lis:
        for j in range(0, i.count):
            new_distance.append(i.value)

    return  new_distance


def optimal_distances(seg_list: list[meaning], bank: int):
    seg_dict: dict[int, list[meaning]]
    seg_dict = {0: seg_list}

    for iterator in range(1, bank+1):
        seg_dict[iterator] = (seg_dict[iterator-1])

        max= 0
        count_max_value = 1
        iter = 0
        index = 0

        for segment in seg_dict[iterator]:
            if segment.value > max:
                max = segment.value
                count_max_value = segment.count
                index = iter
            elif (segment.value == max) and (segment.count > count_max_value):
                index = iter
                count_max_value = segment.count

            iter += 1

        seg_dict[iterator][index].count += 1
        seg_dict[iterator][index].value = seg_dict[iterator][index].range / seg_dict[iterator][index].count

    return seg_dict[bank]

if __name__ == '__main__':
        segment_list = []
        distances = [100, 20, 30, 80]
        for i, distance in enumerate(distances):
            segment_list.append(meaning(i, abs(distance)))
            segment_list.sort(key=lambda x: x.value, reverse=True)

        n = 5
        k = 2
        segment_list = optimal_distances(segment_list, k)
        segment_list.sort(key=lambda x: x.position, reverse=False)
        print("Новые расстояния: " + str(add_atm_distances(segment_list)))
