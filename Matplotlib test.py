import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def update(frame):
    plt.cla()
    ax.bar(range(len(frame)), frame, color='blue')
    plt.title("Three-Way Partition Sort")

def quicksort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[0]
    less = [x for x in lst[1:] if x < pivot]
    equal = [x for x in lst if x == pivot]
    greater = [x for x in lst[1:] if x > pivot]

    return quicksort(less) + equal + quicksort(greater)

def three_way_partition_sort_visualized(lst):
    if len(lst) <= 2:
        return sorted(lst)

    l1 = lst[:len(lst)//3]
    ln_minus_m = lst[len(lst)//3:2*len(lst)//3]
    ln = lst[2*len(lst)//3:]

    if l1:
        l1_sorted = quicksort(l1)
    else:
        l1_sorted = []

    if ln_minus_m:
        ln_minus_m_sorted = quicksort(ln_minus_m)
    else:
        ln_minus_m_sorted = []

    if ln:
        ln_sorted = quicksort(ln)
    else:
        ln_sorted = []

    return l1_sorted + ln_minus_m_sorted + ln_sorted


data = [1, 5, 8, 4, 2]

sorting_steps = [three_way_partition_sort_visualized(data[:i+1]) for i in range(len(data))]

fig, ax = plt.subplots()

def init():
    ax.set_xlim(0, len(data))
    ax.set_ylim(0, max(data) + 1)
    return []

animation = FuncAnimation(fig, update, frames=sorting_steps, init_func=init, repeat=False)

plt.show()
