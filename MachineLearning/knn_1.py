#KNN tutorial

from sklearn.neighbors import KNeighborsClassifier

from math import sqrt
def Euclidean_distance(point1, point2,class_value):
    print(point1," ",point2," ",sqrt(pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2)),class_value)

def main():
    x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
    y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
    z = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
    classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

    data = list(zip(x, y,z))
    print(data)
    print(classes)

    for i in range(len(data)):
        Euclidean_distance(data[i], (8,21), classes[i])
    
    model = KNeighborsClassifier(n_neighbors=7)
    model.fit(data, classes)
    print(model.predict([[8, 21,11]]))
    
if __name__=="__main__":
    main()