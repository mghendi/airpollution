import numpy
from numpy import array
from numpy import mean
from numpy import cov, var
from PIL import Image
from numpy.linalg import eigh, norm
from matplotlib.pyplot import *
import math

# The probability of an image belonging to a class P(picture | class) = P(class, picture) / P(class)
# This means that the probability of the image being in class can be determined by P(x), using a normal distribution
# variance (sigma_sq), mean (avg)

def train_data():
    
    f = open('sample_train.txt', 'r')
    train_images = []

    for line in f:
        line = line.split(' ')
        train_images.append((
            (numpy.asarray(Image.open(line[0]).convert('L').resize((64, 64))).flatten()), line[1].split('\n')[0]))

    # print(train_images)
    return train_images

def test_data():

    f = open('sample_test.txt', 'r')
    test_images = []

    for line in f:
        test_images.append(numpy.asarray(Image.open(line.split()[0]).convert('L').resize((64, 64))).flatten())

    return test_images

def train_PCA(data):
    images = []

    for (image, name) in data:
        images.append(image)

    matrix = numpy.asarray(images)
    # print(matrix)

    avg = mean(matrix.T, axis=1)
    center = matrix - avg
    variance = cov(center.T)
    values, vectors = eigh(variance)

    feat_vec = numpy.flip(vectors)[:,:32]
    norm_line = feat_vec.T.dot(center.T)

    return feat_vec, norm_line.T, avg

def eigen_class(eigen, data):

    classed_eigen = dict()

    for index, arr in enumerate(eigen):
        if data[index][1] not in classed_eigen:
            classed_eigen[data[index][1]] = list()
        classed_eigen[data[index][1]].append(arr) 
    
    for key in classed_eigen:
        classed_eigen[key] = numpy.asarray(classed_eigen[key])

    return classed_eigen

def mean_and_var(classed_eigen):
    avg = {}
    vari = {}
    for name in classed_eigen:
        arr = classed_eigen[name]
        # mu = mean(arr.T, axis=1)
        mu = [mean(col) for col in arr.T]
        # cen = arr - mu
        sigma_sq = var(arr.T, axis=1)

        if name not in avg:
            avg[name] = 0
            vari[name] = 0
        avg[name] = mu
        vari[name] = sigma_sq
    return avg, vari


def test_PCA(test_data, training_vectors, avg):
    matrix = numpy.asarray(test_data)
    # print(matrix)

    center = matrix - avg

    test_norm_line = training_vectors.T.dot(center.T)
    
    return test_norm_line.T

def find_distributions(mu, sig_sq, test_line):
    prod = 1
    max_val = -9999
    max_class = list()
    for vec in test_line:
        temp_name = 'X'
        max_val = -9999
        # print(test_line.shape)
        for name in mu:
            prod = 1    
            for index in range(len(vec)): 
                p_x_1 = (2 * 3.14 * sig_sq[name][index]) ** 0.5
                ra = (-(vec[index] - mu[name][index]) ** 2) / (2*sig_sq[name][index])
                p_x_2 = math.exp(ra)
                p_x = p_x_2/p_x_1
                prod *= p_x 
                # print(p_x_1, p_x_2, ra, p_x)
                # print(vec[index])
            if prod > max_val:
                max_val = prod
                temp_name = name
        max_class.append(temp_name)
    return max_class

training_data = train_data()
testing_data = test_data()

# print(training_data)
# print(testing_data)

vec, line, avg = train_PCA(training_data)

classed_eigen = eigen_class(line, training_data)
mu, sig_sq = mean_and_var(classed_eigen)

test_line = test_PCA(testing_data, vec, avg)
names = find_distributions(mu, sig_sq, test_line)
#print(names)