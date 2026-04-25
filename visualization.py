import matplotlib.pyplot as plt


def plot_bar(data):
    values = list(data.values())

    if not values or sum(values) == 0:
        print("No occupancy data to plot")
        return

    plt.figure()
    plt.bar(list(data.keys()), values)
    plt.title("Ward Occupancy")
    plt.xlabel("Ward")
    plt.ylabel("Occupancy %")
    plt.savefig("bar.png")
    plt.close()


def plot_pie(data):
    values = list(data.values())

    print("NEW PIE FUNCTION RUNNING")   # DEBUG LINE

    if not values or sum(values) == 0:
        print("No data to display in pie chart")
        return

    plt.figure()
    plt.pie(values, labels=list(data.keys()), autopct='%1.1f%%')
    plt.title("Ward Distribution")
    plt.savefig("pie.png")
    plt.close()


def plot_line(series):
    if series is None or len(series) == 0:
        print("No admission data to plot")
        return

    plt.figure()
    series.sort_index().plot()
    plt.title("Peak Admissions by Month")
    plt.savefig("line.png")
    plt.close()
