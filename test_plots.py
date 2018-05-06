import matplotlib.pyplot as plt
import numpy

d1 = [1, 2, 3]
d2 = [2, 3, 4]
d3 = [1, 2, 3]
labels = ['Negative', 'Neutral', 'Positive']

fig = plt.figure()
ax = fig.add_subplot(111)

# this is how we will get multiple plots per graph
# 3
plt.bar(numpy.arange(3) * 3, d1, color='red')
plt.bar(numpy.arange(3) * 3 + .8, d2, color='blue')
plt.bar(numpy.arange(3) * 3 + 1.6, d3, color='green')
ax.set_xticks(numpy.arange(3)*3+.8)

# 2
# plt.bar(numpy.arange(3) * 2, d1, color='red')
# plt.bar(numpy.arange(3) * 2 + .8, d2, color='blue')
# ax.set_xticks(numpy.arange(3)*2+.4)

ax.set_xticklabels(labels)
plt.show()

