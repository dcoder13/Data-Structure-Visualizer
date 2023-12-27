from .bar import bar

class sortingAlgos:
    # def __init__(self, array, barsList, canvas, speed):
    #     self.array = array
    #     self.barsList = barsList
    #     self.canvas = canvas
    #     self.speed = speed
    #     self.stopSorting = False

    def reDraw(self):
        self.canvas.delete("all")
        for i in range(len(self.array)):
            self.barsList[i].draw(self.canvas)
        self.canvas.update()

    def startSort(self, selection):
        self.stopSorting = True
        selected_option = selection.get()
        print(selected_option)
        switcher = {
            "Bubble Sort": self.bubbleSort,
            "Insertion Sort": self.insertionSort,
            'Selection Sort': self.selectionSort,
            'Merge Sort': self.mergeSort,
            'Quick Sort': self.quickSort
        }
        self.stopSorting = False
        if(self.sorted):
            print("already sorted")
        else:
            self.func = switcher.get(selected_option, lambda: "Invalid")
            self.func()


    def bubbleSort(self):
        n = len(self.array)
        print(self.array)
        for i in range(n):
            if self.stopSorting:
                return
            for j in range(0, n - i - 1):
                if self.stopSorting:
                    return
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.barsList[j] = bar(j, self.array[j], "red", n, self.canvas)
                    self.barsList[j + 1] = bar(j + 1, self.array[j + 1], "red", n, self.canvas)
                    self.reDraw()
                    self.canvas.after(int(200//self.speed))
            self.barsList[n - i - 1] = bar(n - i - 1, self.array[n - i - 1], "blue", n, self.canvas)
        self.stopSorting = True
        self.sorted = True
        print("bubble sort :", self.array)

    def insertionSort(self):
        print(self.array)
        n = len(self.array)
        for i in range(1, n):
            j = i - 1
            while j >= 0 and self.array[j+1] < self.array[j]:
                if self.stopSorting:
                    return
                self.array[j + 1], self.array[j] = self.array[j], self.array[j+1]
                self.barsList[j + 1] = bar(j + 1, self.array[j + 1], "blue", n, self.canvas)
                self.barsList[j] = bar(j, self.array[j], "blue", n, self.canvas)
                self.reDraw()
                self.canvas.after(int(200//self.speed))
                j -= 1
            if self.stopSorting:
                return
        self.stopSorting = True
        self.sorted = True
        print(self.array)

    def selectionSort(self):
        print(self.array)
        n = len(self.array)
        for i in range(n):
            for j in range(i+1,n):
                if self.stopSorting:
                    return
                if self.array[i] > self.array[j]:
                    self.array[i], self.array[j] = self.array[j], self.array[i]
                    self.barsList[i] = bar(i, self.array[i], "blue", n, self.canvas)
                    self.barsList[j] = bar(j, self.array[j], "red", n, self.canvas)
                    self.reDraw()
                    self.canvas.after(int(200//self.speed))
            if self.stopSorting:
                return
            self.barsList[i] = bar(i, self.array[i], "blue", n, self.canvas)
            self.reDraw()
        self.stopSorting = True
        self.sorted = True
        print("insertion sort: ", self.array)

    def mergeSort(self):
        print(self.array)
        n = len(self.array)
        def merge(low, mid, high):
            if self.stopSorting:
                    return
            n1 = mid - low + 1
            n2 = high - mid
            L = [0] * (n1)
            R = [0] * (n2)
            for i in range(0, n1):
                if self.stopSorting:
                    return
                L[i] = self.array[low + i]
            for j in range(0, n2):
                if self.stopSorting:
                    return
                R[j] = self.array[mid + 1 + j]
            i = 0
            j = 0
            k = low
            while i < n1 and j < n2:
                if self.stopSorting:
                    return
                if L[i] <= R[j]:
                    self.array[k] = L[i]
                    i += 1
                else:
                    self.array[k] = R[j]
                    j += 1
                self.barsList[k] = bar(k, self.array[k], "blue", n, self.canvas)
                self.reDraw()
                self.canvas.after(int(200//self.speed))
                k += 1
            while i < n1:
                if self.stopSorting:
                    return
                self.array[k] = L[i]
                self.barsList[k] = bar(k, self.array[k], "blue", n, self.canvas)
                self.reDraw()
                self.canvas.after(int(200//self.speed))
                i += 1
                k += 1
            while j < n2:
                if self.stopSorting:
                    return
                self.array[k] = R[j]
                self.barsList[k] = bar(k, self.array[k], "blue", n, self.canvas)
                self.reDraw()
                self.canvas.after(int(200//self.speed))
                j += 1
                k += 1
        def divide(low, high):
            if low < high:
                if self.stopSorting:
                    return
                mid = (low + high) // 2
                divide(low, mid)
                divide(mid + 1, high)
                merge(low, mid, high)
        divide(0, n - 1)
        if self.stopSorting:
            return
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
                if self.stopSorting:
                    return
                if self.array[j] < pivot:
                    i += 1
                    self.array[i], self.array[j] = self.array[j], self.array[i]
                    self.barsList[i] = bar(i, self.array[i], "red", n, self.canvas)
                    self.barsList[j] = bar(j, self.array[j], "red", n, self.canvas)
                    self.reDraw()
                    self.canvas.after(int(200//self.speed))
            self.array[i+1], self.array[high] = self.array[high], self.array[i+1]
            self.barsList[i+1] = bar(i+1, self.array[i+1], "green", n, self.canvas)
            self.barsList[high] = bar(high, self.array[high], "red", n, self.canvas)
            self.reDraw()
            self.canvas.after(int(200//self.speed))
            return i+1
        def quick(low, high):
            if low < high:
                if self.stopSorting:
                    return
                pi = partition(low, high)
                if self.stopSorting:
                    return
                quick(low, pi-1)
                for i in range(low, pi):
                    self.barsList[i] = bar(i, self.array[i], "blue", n, self.canvas)
                self.canvas.after(int(200//self.speed))
                quick(pi+1, high)
                for i in range(pi, high+1):
                    self.barsList[i] = bar(i, self.array[i], "blue", n, self.canvas)
                self.canvas.after(int(200//self.speed))
        quick(0, n-1)
        if self.stopSorting:
            return
        self.stopSorting = True
        self.sorted = True
        print("quick sort :", self.array)
