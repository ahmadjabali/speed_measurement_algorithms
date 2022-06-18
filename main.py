from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
#import time
import timeit
#arr = []
root = Tk()
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
# For Time Complexity
def quickSort(arr, low, high):

    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


# For Space Complexity
# Function Insertion sort
def insertion_sort(arr, low, n):
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        while j > low and arr[j - 1] > val:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = val

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
def hybrid_quick_sort(arr, low, high):
    while low < high:

        # If the size of the array is less
        # than threshold apply insertion sort
        # and stop recursion
        if high - low + 1 < 10:
            insertion_sort(arr, low, high)
            break

        else:
            pivot = partition(arr, low, high)


            if pivot - low < high - pivot:
                hybrid_quick_sort(arr, low, pivot - 1)
                low = pivot + 1
            else:

                hybrid_quick_sort(arr, pivot + 1, high)
                high = pivot - 1


root.geometry("600x300")
root.title(" choosing the best sorting algorithm ")
bg = PhotoImage(file="52.png")
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

frame = Frame(root, bd=5,bg = "#009cea")
frame.pack()

my_logo =ImageTk.PhotoImage(Image.open("5778984.png"))
my_label8 = Label(image=my_logo,bg = "#009cea")
my_label8.pack()

mylabel2 = Label(frame, padx=100, text="Enter Array and put , between numbers:",bg = "#00aaff")
mylabel2.pack()


inp = Entry(frame, width=50)
inp.pack()
arr=[]
mylabel = Label(frame, padx=100, text="preferd complexity :",bg = "#00aaff")
mylabel.pack()

v1 = StringVar()

r1 = Radiobutton(frame, text="Time Complexity", variable=v1, value="Time Complexity",bg = "#009cea")
r2 = Radiobutton(frame, text="Space Complexity", variable=v1, value="Space Complexity",bg = "#009cea")
r3 = Radiobutton(frame, text="Time + Space", variable=v1, value="hybrid",bg = "#009cea")
r1.pack()
r2.pack()
r3.pack()

def srt():

    arrORG = str(inp.get())
    arr1 = arrORG.split(",")
    integer_map = map(int, arr1)
    integer_list = list(integer_map)
    arr=integer_list
    n = len(arr)

    #arr = [int(d) for d in str(arrORG)]

    if v1.get() == "Time Complexity":
        quickSort(arr, 0, n - 1)


    elif v1.get() == "Space Complexity":
        insertion_sort(arr, 0, n - 1)
    elif v1.get() == "hybrid":
        hybrid_quick_sort(arr, 0, n - 1)


    lin1 = "\n your array before sorting : " + arrORG
    lin2 = "\n your choice of sorting : " + v1.get()
    lin3 = "\n your array after sorting : " + str(arr)
    lin4 = "\n The Time complexity : "

    execution_time = timeit.timeit(quickSort,1)
    lin5 =execution_time
    mylabel3 = Label(frame, padx=100, text="Result :" + lin1 + lin2 + lin3 + lin4 + lin5)
    mylabel3.pack()


btn = Button(frame, text="SORT", command=srt)
btn.pack()

root.mainloop()


