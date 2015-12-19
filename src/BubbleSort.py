class BubbleSort:
    def bubbleSort(self, A, n):
        # write code here
        for i in range(n - 1, 1, -1):
            for j in range(0, i):
                if A[j] > A[j + 1]:
                    A[j],A[j + 1] = A[j + 1], A[j]
        print(A)

A = [54,35,48,36,27,12,44,44,8,14,26,17,28]
n = len(A)
bubbleSort = BubbleSort()
bubbleSort.bubbleSort(A, n)