import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import random
import math
from sklearn.cluster import KMeans
import collections


# points = []
# for line in file:
#     n1, n2 = line.split()
#     points.append((int(n1), int(n2)))
#
# plt.scatter(*zip(*points))
# plt.show()
# X = np.array(points)
#
# K = 3
# kmeans = KMeans(n_clusters = K)
# kmeans.fit(X)
# y_kmeans = kmeans.predict(X)
#
# plt.scatter(X[:, 0], X[:, 1], c = y_kmeans, s = 20, cmap = 'summer')
# #plt.scatter(X[:, 0], X[:, 1], c = y_kmeans)
# centers = kmeans.cluster_centers_
# plt.scatter(centers[:, 0], centers[:, 1], c = 'blue', s = 100, alpha = 0.9);
# plt.show()

def euclidian_range(x, y, centroid):
    sum_eu = (x - centroid[0]) ** 2 + (y - centroid[1]) ** 2
    return math.sqrt(sum_eu)


print("Выбери dataset\n1.birch1\n2.birch2\n3.birch3\n4.s1")
s = input()
if s == "1":
    file = open("points/birch1.txt", "r")
elif s == "2":
    file = open("points/birch2.txt", "r")
elif s == "3":
    file = open("points/birch3.txt", "r")
else:
    file = open("points/s1.txt", "r")

points = []
X = []
Y = []
for line in file:
    n1, n2 = line.split()
    X.append(int(n1))
    Y.append(int(n2))
    points.append((int(n1), int(n2)))

print("K = ?")
K = int(input())
centroids = []
clusters = []
all_colors = matplotlib.cm.rainbow(np.linspace(0, 1, K))

for i in range(K):
    centroids.append(((random.randint(np.min(X), np.max(X))), (random.randint(np.min(Y), np.max(Y)))))

plt.scatter(*zip(*points))
plt.scatter(*zip(*centroids), c='deeppink', s=50)
plt.show()

previous_clusters = []

print("computing ...")
for i in range(len(points)):
    min_distance = euclidian_range(X[i], Y[i], centroids[0])
    min_index = 0
    for j in range(len(centroids)):
        if euclidian_range(X[i], Y[i], centroids[j]) < min_distance:
            min_distance = euclidian_range(X[i], Y[i], centroids[j])
            min_index = j
    previous_clusters.append((min_index, points[i]))

for i in range(len(centroids)):
    x_sum = 0
    y_sum = 0
    x_count = 0
    y_count = 0
    for key, value in previous_clusters:
        if key == i:
            x_sum += value[0]
            y_sum += value[1]
            x_count += 1
            y_count += 1
    centroids[i] = (x_sum / x_count, y_sum / y_count)

while True:
    for i in range(len(points)):
        min_distance = euclidian_range(X[i], Y[i], centroids[0])
        min_index = 0
        for j in range(len(centroids)):
            if euclidian_range(X[i], Y[i], centroids[j]) < min_distance:
                min_distance = euclidian_range(X[i], Y[i], centroids[j])
                min_index = j
        clusters.append((min_index, points[i]))

    if previous_clusters == clusters:
        break

    previous_clusters = list(clusters)

    # keys = []
    # sumX = {}
    # sumY = {}
    # for i in range(len(clusters)):
    #     keys.append(clusters[i][0])
    # c = collections.Counter(keys)
    #
    # for key, value in clusters:
    #     if key not in sumX:
    #         sumX[key] = value[0]
    #         sumY[key] = value[1]
    #     else:
    #         sumX[key] += value[0]
    #         sumY[key] += value[1]
    #
    # for i in range(len(centroids)):
    #     centroids[i] = (sumX[i] / c[i], sumY[i] / c[i])

    for i in range(len(centroids)):
        x_sum = 0
        y_sum = 0
        count = 0
        for key, value in clusters:
            if key == i:
                x_sum += value[0]
                y_sum += value[1]
                count += 1
        centroids[i] = (x_sum / count, y_sum / count)

    clusters.clear()

color_values = []
for i in range(len(clusters)):
    color_values.append(all_colors[clusters[i][0]])
plt.scatter(*zip(*points), c=color_values)
plt.scatter(*zip(*centroids), c='deeppink', s=50)
plt.show()
# -----------------------------------
