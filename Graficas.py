import numpy as np
import matplotlib.pyplot as plt
def graph(v):
    N = len(v)

    ind = np.arange(N)    # the x locations for the groups
    width = 0.2       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, v, width)


    plt.ylabel('Percentages')
    plt.title('Probabilities for a state vector')
    plt.xticks(ind, ('0', '1', '2', '3', '4','5'))
    plt.yticks(np.arange(0, 1.1,0.1 ))

    plt.show()