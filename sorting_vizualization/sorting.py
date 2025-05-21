import random
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as anim


n = int(input("Enter the number of elements:"))
print("\n 1.Bubble \n 2.Insertion \n 3.Quick \n 4.Selection \n 5.Merge Sort \n 6.Heapify \n 7.Shell \n 8.Count sort \n")
al = int(input("Choose algorithm: "))
array = [i + 1 for i in range(n)]
random.shuffle(array)

if(al==1):
    title = "Bubble Sort"
    algo = sort_buble(array)
elif(al==2):
    title = "Insertion Sort"
    algo = insertion_sort(array)
elif(al==3):
    title = "Quick Sort"
    algo = quick_Sort(array,0,n-1)
elif(al==4):
    title="Selection Sort"
    algo = selection_sort(array)
elif (al == 5):
    title = "Merge Sort"
    algo=merge_sort(array,0,n-1)
elif (al == 6):
    title = "Heap Sort"
    algo = heap_sort(array)
elif (al == 7):
    title = "Shell Sort"
    algo = shell_sort(array)
elif (al == 8):
    title = "Count Sort"
    algo = count_sort(array)
else:
    print("Please enter a number from list")
# Initialize fig
fig, ax = plt.subplots()
ax.set_title(title)

bar_rec = ax.bar(range(len(array)), array, align='edge')

ax.set_xlim(0, n)
ax.set_ylim(0, int(n * 1.1))

text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

epochs = [0]


def update_plot(array, rec, epochs):
    for rec, val in zip(rec, array):
        rec.set_height(val)
    epochs[0]+= 1
    text.set_text("No.of operations :{}".format(epochs[0]))


anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, epochs), frames=algo, interval=1, repeat=False)
plt.show()
