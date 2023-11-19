import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def update(frame):
    plt.cla()
    ax.bar(range(len(frame)), frame, color='blue')
    plt.title("Three-Way Partition Sort")

def three_way_partition_sort_visualized(lst):
    if len(lst) <= 2:
        return sorted(lst)

    l1 = lst[:len(lst)//3]
    ln_minus_m = lst[len(lst)//3:2len(lst)//3]
    ln = lst[2len(lst)//3:]

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
animation = FuncAnimation(fig, update, frames=sorting_steps, repeat=False)

plt.show()
