import numpy
from numpy import array
from numpy import mean
from numpy import cov
from PIL import Image
from numpy.linalg import eigh, norm
from matplotlib.pyplot import *
import os



def get_images():
	# input: none
	# output: Array of all images read by PIL
	
	path = './dataset/'
	images = []
	count = 0
	for f in os.listdir(path):
		images.append(numpy.asarray(Image.open(path +'/'+f).convert('L').resize((64, 64))).flatten())

	# image [0] is the first image
	# image [0][0] is the first column
	# image [0][0][0] is the first pixel, with [R, G, B]
	return numpy.asarray(images)





def PCA(data, n_d):
	# input: One colour array (R, G or B) of one image
	# output: PCA of that colour array
	

	matrix = data
	avg = mean(matrix.T, axis=1)
	center = matrix - avg
	variance = cov(center.T)
	values, vectors = eigh(variance)
	# print(vectors.shape)
	feat_vec = numpy.flip(vectors)[:,:n_d]
	norm_line = vectors.T.dot(center.T)
	# values are the eigenvalues, vectors is a matrix of eigenvectors
	
	return feat_vec.T, norm_line

def reconstruct(images, vectors):
	# input: vectors of all images
	# output: reconstructed images
	vectors = vectors.T
	# recon_array = numpy.array((4096,1))
	im = ''
	recon_list = []
	for originalImage in images:
		recon_array = []
		recon = numpy.dot(originalImage,vectors)*vectors
		# print(recon.shape)
		for i, row in enumerate(recon):
			recon_array.append(sum(row))
		recon_list.append(numpy.array(recon_array))
		# recon_array = numpy.asarray(recon_array)
		# im = Image.fromarray(recon_array.reshape((64,64)).astype(numpy.uint8), 'L')
	# im.rotate(180).show()
	return numpy.array(recon_list)

def store_images(images):
	index = 0
	for im in images:
		im = Image.fromarray(im.reshape((64,64)).astype(numpy.uint8), 'L')
		im.rotate(180)
		im.save('./reconstructed_dataset/recon_' + str(index), 'JPEG')
		index += 1
	return


images = get_images()

# for all the testing, we define one test picture, which is images[0]

graph_x, graph_y = [], []
vectors, norm_line = PCA(images, 200)
reconstructed_images = reconstruct(images, vectors)
mse = 0
for i, im in enumerate(images):
	mse += norm(images[i] - reconstructed_images[i])/norm(images[i])
mse /= len(images)
print(mse)
store_images(reconstructed_images)

# plot(graph_x,graph_y)
# show()
# print(vectors.shape)

