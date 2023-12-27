from random import randint
from .bar import bar


class sortingAlgos:
    def __init__(self , reDraw , array, barsList, canvas, speed):
        self.array = array
        self.barsList = barsList
        self.canvas = canvas
        self.speed = speed
        self.reDraw = reDraw

    def bubbleSort(self):
        n = len(self.array)
        print(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.barsList[j] = bar(j, self.array[j], "red", n, self.canvas)
                    self.barsList[j + 1] = bar(j + 1, self.array[j + 1], "red", n, self.canvas)
                    self.reDraw()
                    self.canvas.after(int(200//self.speed[0]))
            self.barsList[n - i - 1] = bar(n - i - 1, self.array[n - i - 1], "blue", n, self.canvas)
        self.sorted = True
        print("bubble sort :", self.array)

    def insertionSort(self):
        print(self.array)
        n = len(self.array)
        for i in range(1, n):
            j = i - 1
            while j >= 0 and self.array[j+1] < self.array[j]:
                self.array[j + 1], self.array[j] = self.array[j], self.array[j+1]
                self.barsList[j + 1] = bar(j + 1, self.array[j + 1], "blue", n, self.canvas)
                self.barsList[j] = bar(j, self.array[j], "blue", n, self.canvas)
                self.reDraw()
                self.canvas.after(int(200//self.speed[0]))
                j -= 1
        print(self.array)

    def selectionSort(self):
        print(self.array)
        n = len(self.array)
        for i in range(n):
            for j in range(i+1,n):
                if self.array[i] > self.array[j]:
                    self.array[i], self.array[j] = self.array[j], self.array[i]
                    self.barsList[i] = bar(i, self.array[i], "blue", n, self.canvas)
                    self.barsList[j] = bar(j, self.array[j], "red", n, self.canvas)
                    self.reDraw()
                    self.canvas.after(int(200//self.speed[0]))
            self.barsList[i] = bar(i, self.array[i], "blue", n, self.canvas)
            self.reDraw()
        print("insertion sort: ", self.array)

    def mergeSort(self):
        print(self.array)
        n = len(self.array)
        def merge(low, mid, high):
            n1 = mid - low + 1
            n2 = high - mid
            L = [0] * (n1)
            R = [0] * (n2)
            for i in range(0, n1):
                L[i] = self.array[low + i]
            for j in range(0, n2):
                R[j] = self.array[mid + 1 + j]
            i = 0
            j = 0
            k = low
            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    self.array[k] = L[i]
                    i += 1
                else:
                    self.array[k] = R[j]
                    j += 1
                self.barsList[k] = bar(k, self.array[k], "blue", n, self.canvas)
                self.reDraw()
                self.canvas.after(int(200//self.speed[0]))
                k += 1
            while i < n1:
                self.array[k] = L[i]
                self.barsList[k] = bar(k, self.array[k], "blue", n, self.canvas)
                self.reDraw()
                self.canvas.after(int(200//self.speed[0]))
                i += 1
                k += 1
            while j < n2:
                self.array[k] = R[j]
                self.barsList[k] = bar(k, self.array[k], "blue", n, self.canvas)
                self.reDraw()
                self.canvas.after(int(200//self.speed[0]))
                j += 1
                k += 1
        def divide(low, high):
            if low < high:
                mid = (low + high) // 2
                divide(low, mid)
                divide(mid + 1, high)
                merge(low, mid, high)
        divide(0, n - 1)
        self.stopSorting = True
        self.sorted = True
        print("merge sort: ", self.array)

    def quickSort(self):
        print(self.array)
        n = len(self.array)
        def partition(low, high):
            i = low - 1
            pivot = self.array[high]
            for j in range(low, high):
                if self.array[j] < pivot:
                    i += 1
                    self.array[i], self.array[j] = self.array[j], self.array[i]
                    self.barsList[i] = bar(i, self.array[i], "red", n, self.canvas)
                    self.barsList[j] = bar(j, self.array[j], "red", n, self.canvas)
                    self.reDraw()
                    self.canvas.after(int(200//self.speed[0]))
            self.array[i+1], self.array[high] = self.array[high], self.array[i+1]
            self.barsList[i+1] = bar(i+1, self.array[i+1], "green", n, self.canvas)
            self.barsList[high] = bar(high, self.array[high], "red", n, self.canvas)
            self.reDraw()
            self.canvas.after(int(200//self.speed[0]))
            return i+1
        def quick(low, high):
            if low < high:
                pi = partition(low, high)
                quick(low, pi-1)
                for i in range(low, pi):
                    self.barsList[i] = bar(i, self.array[i], "blue", n, self.canvas)
                self.canvas.after(int(200//self.speed[0]))
                quick(pi+1, high)
                for i in range(pi, high+1):
                    self.barsList[i] = bar(i, self.array[i], "blue", n, self.canvas)
                self.canvas.after(int(200//self.speed[0]))
        quick(0, n-1)
        print("quick sort :", self.array)
