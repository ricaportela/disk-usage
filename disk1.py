from matplotlib import pyplot as plt


def plot_data():
    """ Draw Pie Chart with values from Json File """
    # Data to plot
    labels = 'Used', 'Available', 'Use%'
    sizes = [215, 210, 134]
    colors = ['gold', 'yellowgreen', 'lightcoral']
    explode = (0.1, 0, 0)  #  explode 1st slice
    plt.title('Filesystem'+'\n'+'Size of '+'Mounted on ')
    # Plot
    plt.pie(sizes, explode=explode, labels=labels, \
                   colors=colors, autopct='%1.1f%%', \
                   shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()

if __name__ == ("__main__"):
    plot_data()
    