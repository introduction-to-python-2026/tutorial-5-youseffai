# Q: Write an import statement that imports the function pyplot from the module matplotlib and renames it to plt.
import matplotlib as plt


def build_histogram(data):
  lst={}
  for i in data:
    for key in lst.keys():
      if i == key:
        lst[key] = lst[key]+ 1
      else:
        lst[i] = 1
  return lst
def plot_histogram(histogram):
    x_values = list(histogram.keys())
    y_values = list(histogram.values())

    plt.bar(x_values, y_values)
    plt.xlabel('Items')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()


