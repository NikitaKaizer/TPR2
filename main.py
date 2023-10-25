class Element:
    def __init__(self, w):
        self.weight = w


class Container:
    def __init__(self, max_weight=100):
        self.MAXWEIGHT = max_weight
        self.current_elems = []

    def is_enough_space_for(self, elem):
        return elem.weight < (self.MAXWEIGHT - self.get_full_weight())

    def get_weight_to_full_capacity(self):
        return self.MAXWEIGHT - self.get_full_weight()

    def get_full_weight(self):
        return sum(self.current_elems)

    def put(self, elem):
        self.current_elems.append(elem.weight)


class Line:
    def __init__(self):
        self.amount_of_comparison = 0
        self.container_arr = [Container()]

    def reset(self):
        self.amount_of_comparison = 0
        self.container_arr = [Container()]

    def nfa(self, elem_arr):
        self.reset()
        for elem in elem_arr:
            self.amount_of_comparison += 1
            if self.container_arr[-1].is_enough_space_for(elem):
                self.container_arr[-1].put(elem)
            else:
                self.container_arr.append(Container())
                self.container_arr[-1].put(elem)

    def ffa(self, elem_arr):
        self.reset()
        for elem in elem_arr:
            self.amount_of_comparison += 1
            if self.container_arr[-1].is_enough_space_for(elem):
                self.container_arr[-1].put(elem)
            else:
                not_found_place_for_elem = True
                for i in range(len(self.container_arr) - 1, -1, -1):
                    self.amount_of_comparison += 1
                    if self.container_arr[i].is_enough_space_for(elem):
                        self.container_arr[i].put(elem)
                        not_found_place_for_elem = False
                        break
                if not_found_place_for_elem:
                    self.container_arr.append(Container())
                    self.container_arr[-1].put(elem)

    def wfa(self, elem_arr):
        self.reset()
        for elem in elem_arr:
            if self.container_arr[-1].is_enough_space_for(elem):
                self.container_arr[-1].put(elem)
            else:
                not_found_place_for_elem = True
                position = 0
                weight = self.container_arr[0].get_full_weight()
                for i in range(len(self.container_arr)):
                    self.amount_of_comparison += 1
                    if (self.container_arr[i].is_enough_space_for(elem) and
                            self.container_arr[i].get_weight_to_full_capacity() < weight):
                        weight = self.container_arr[i].get_weight_to_full_capacity()
                        position = i
                        not_found_place_for_elem = False
                if not_found_place_for_elem:
                    self.container_arr.append(Container())
                    self.container_arr[-1].put(elem)
                else:
                    self.container_arr[position].put(elem)

    def bfa(self, elem_arr):
        self.reset()
        for elem in elem_arr:
            self.amount_of_comparison += 1
            if self.container_arr[-1].is_enough_space_for(elem):
                self.container_arr[-1].put(elem)
            else:
                not_found_place_for_elem = True
                position = 0
                weight = 0
                for i in range(len(self.container_arr)):
                    self.amount_of_comparison += 1
                    if (self.container_arr[i].is_enough_space_for(elem) and
                            self.container_arr[i].get_full_weight() > weight):
                        weight = self.container_arr[i].get_full_weight()
                        position = i
                        not_found_place_for_elem = False
                if not_found_place_for_elem:
                    self.container_arr.append(Container())
                    self.container_arr[-1].put(elem)
                else:
                    self.container_arr[position].put(elem)

    def get_number_of_containers(self, method_name):
        print(f"The number of used containers is {len(self.container_arr)} for {method_name}. Number of comparison: {self.amount_of_comparison}")

    def show_containers_arr(self):
        for container in self.container_arr:
            print(f"Container weight: {container.get_full_weight()}")

    def get_results(self, method_name):
        self.get_number_of_containers(method_name)


def generate_elems(args):
    elems_arr = [Element(elem) for elem in args]
    return elems_arr


def check_all_algorithms(elems_arr, additional_info=""):
    if additional_info:
        print("\n", additional_info)
    line = Line()
    line.nfa(elems_arr)
    line.get_results("NFA")
    line.ffa(elems_arr)
    line.get_results("FFA")
    line.wfa(elems_arr)
    line.get_results("WFA")
    line.bfa(elems_arr)
    line.get_results("BFA")


def main():
    elems_arr_60 = generate_elems([
        77, 51, 38, 71, 49, 89, 67, 88, 92, 95, 43, 44, 29, 90, 82, 40, 41, 69, 26, 32,
        61, 42, 60, 17, 23, 61, 81, 09, 90, 25, 96, 67, 77, 34, 90, 26, 24, 57, 14, 68,
        5, 58, 12, 86, 51, 46, 26, 94, 16, 52, 78, 29, 46, 90, 47, 70, 51, 80, 31, 93
    ])

    elems_arr_sorted_60 = sorted(elems_arr_60, key=lambda x: x.weight, reverse=True)

    elems_arr_1row = generate_elems([
        77, 51, 38, 71, 49, 89, 67, 88, 92, 95, 43, 44, 29, 90, 82, 40, 41, 69, 26, 32
    ])

    elems_arr_2row = generate_elems([
        61, 42, 60, 17, 23, 61, 81, 09, 90, 25, 96, 67, 77, 34, 90, 26, 24, 57, 14, 68
    ])

    elems_arr_3row = generate_elems([
        5, 58, 12, 86, 51, 46, 26, 94, 16, 52, 78, 29, 46, 90, 47, 70, 51, 80, 31, 93
    ])

    elems_arr_1row_sorted = sorted(elems_arr_1row, key=lambda x: x.weight, reverse=True)
    elems_arr_2row_sorted = sorted(elems_arr_2row, key=lambda x: x.weight, reverse=True)
    elems_arr_3row_sorted = sorted(elems_arr_3row, key=lambda x: x.weight, reverse=True)

    check_all_algorithms(elems_arr_1row, "20 elements. 1 row Non-Sorted")
    check_all_algorithms(elems_arr_2row, "20 elements. 2 row Non-Sorted")
    check_all_algorithms(elems_arr_3row, "20 elements. 3 row Non-Sorted")
    check_all_algorithms(elems_arr_60, "60 elements. Non-Sorted")

    check_all_algorithms(elems_arr_1row_sorted, "20 elements. 1 row Sorted")
    check_all_algorithms(elems_arr_2row_sorted, "20 elements. 2 row Sorted")
    check_all_algorithms(elems_arr_3row_sorted, "20 elements. 3 row Sorted")
    check_all_algorithms(elems_arr_sorted_60, "60 elements. Sorted")


if __name__ == "__main__":
    main()
