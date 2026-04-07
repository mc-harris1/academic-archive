#!/usr/bin/env python3

"""rmq.py: solve range minimum query utilizing the sparse table method"""

import math
import time
from random import randint

import matplotlib.pyplot as plt


class RMQ:
    def __init__(self, A):
        self.A = A
        self.N = len(self.A)
        log_size = self.get_log_val(self.N) + 1
        self.ST = [[0] * log_size for _ in range(self.N)]

    def get_log_val(self, x):
        return int(math.floor(math.log2(x)))

    def shift_bitwise_left(self, num):
        return 1 << num

    def preprocess(self):  # generate sparse table value
        for col in range(self.N):
            self.ST[col][0] = self.A[col]

        col = 1
        while self.shift_bitwise_left(col) <= self.N:
            row = 0
            while (row + self.shift_bitwise_left(col) - 1) < self.N:
                if self.ST[row][col - 1] < self.ST[row + self.shift_bitwise_left(col - 1)][col - 1]:
                    self.ST[row][col] = self.ST[row][col - 1]
                else:
                    self.ST[row][col] = self.ST[row + self.shift_bitwise_left(col - 1)][col - 1]
                row += 1
            col += 1

    def query(self, left_idx, right_idx):
        i = left_idx
        j = self.get_log_val(right_idx - left_idx + 1)

        if self.ST[i][j] <= self.ST[right_idx - self.shift_bitwise_left(j) + 1][j]:
            return self.ST[i][j]
        else:
            return self.ST[right_idx - self.shift_bitwise_left(j) + 1][j]


if __name__ == "__main__":
    # create arrays of size up to 1,000,000
    sizes = [10, 100, 1000, 10000, 100000, 1000000]

    options = [0, 1]  # 0 - sorted, 1 - random

    results = []

    for opt in options:  # run rmq on both sorted an unsorted arrays of sizes up to 1000000
        for i in sizes:
            arr = []
            for j in range(i):
                if opt == 0:
                    arr.append(j)
                else:
                    arr.append(randint(0, i))

            first = randint(0, i)
            second = randint(0, i)

            if first == second:  # make sure that left index is less than or equal to right index
                left = first
                right = first
            elif first < second:
                left = first
                right = second
            else:
                left = second
                right = first

            start = time.time()  # start timer

            find = RMQ(arr)  # create instance of RMQ class

            find.preprocess()

            min_val = find.query(left, right)

            finish = time.time()  # stop timer

            duration = finish - start  # calculate runtime of RMQ

            print(f"The minimum value of the range [{left}, {right}] is {min_val}.")
            if opt == 0:
                print(
                    f"The duration of the RMQ for the sorted array of "
                    f"size {i} is {duration} seconds.\n"
                )
            else:
                print(
                    f"The duration of the RMQ for the unsorted array of "
                    f"size {i} is {duration} seconds.\n"
                )

            results.append((opt, i, duration))

    # graph results
    for opt in options:
        sizes = [result[1] for result in results if result[0] == opt]
        durations = [result[2] for result in results if result[0] == opt]
        label = "Sorted" if opt == 0 else "Unsorted"
        plt.plot(sizes, durations, label=label)

    plt.xlabel("Array Size")
    plt.ylabel("Duration (seconds)")
    plt.title("RMQ Performance")
    plt.legend()
    plt.xscale("log")
    plt.yscale("log")
    plt.show()
