import numpy as np
from skimage import io, util
import heapq
from PIL import Image


# function for random block placement
def randomPatch(texture, blockSize):
    height, width, _ = texture.shape
    i = np.random.randint(width - blockSize)
    j = np.random.randint(height - blockSize)

    return texture[j:j + blockSize, i:i + blockSize]


# function for selecting the patch that reduces the overlap error
def L2Norm(patch, blockSize, overlap, result, x, y):
    error = 0
    if x > 0:
        left = patch[:, :overlap] - result[y:y + blockSize, x:x + overlap]
        error += np.sum(left ** 2)

    if y > 0:
        up = patch[:overlap, :] - result[y:y + overlap, x:x + blockSize]
        error += np.sum(up ** 2)

    if x > 0 and y > 0:
        corner = patch[:overlap, :overlap] - result[y:y + overlap, x:x + overlap]
        error -= np.sum(corner ** 2)

    return error


# selecting next random patch and calculating the L2norm error
def randomBestPatch(texture, blockSize, overlap, result, x, y):
    height, width, _ = texture.shape
    errors = np.zeros((height - blockSize, width - blockSize))

    for i in range(height - blockSize):
        for j in range(width - blockSize):
            patch = texture[i:i + blockSize, j:j + blockSize]
            e = L2Norm(patch, blockSize, overlap, result, x, y)
            errors[i, j] = e

    i, j = np.unravel_index(np.argmin(errors), errors.shape)
    return texture[i:i + blockSize, j:j + blockSize]


def minCutPath(errors):
    pq = [(error, [i]) for i, error in enumerate(errors[0])]
    heapq.heapify(pq)

    height, width = errors.shape
    seen = set()

    while pq:
        error, path = heapq.heappop(pq)
        curr_depth = len(path)
        curr_index = path[-1]

        if curr_depth == height:
            return path

        for delta in -1, 0, 1:
            next_index = curr_index + delta

            if 0 <= next_index < width:
                if (curr_depth, next_index) not in seen:
                    cuml_error = error + errors[curr_depth, next_index]
                    heapq.heappush(pq, (cuml_error, path + [next_index]))
                    seen.add((curr_depth, next_index))


# finding the overlap between a given block and the neighbouring blocks and then finding the minimum cost path which is the boundarya
def minCutPatch(patch, blockSize, overlap, result, x, y):
    patch = patch.copy()
    minCut = np.zeros_like(patch, dtype=bool)
    dy, dx, _ = patch.shape

    if x > 0:
        left = patch[:, :overlap] - result[y:y + dy, x:x + overlap]
        leftL2 = np.sum(left ** 2, axis=2)
        for i, j in enumerate(minCutPath(leftL2)):
            minCut[i, :j] = True

    if y > 0:
        up = patch[:overlap, :] - result[y:y + overlap, x:x + dx]
        upL2 = np.sum(up ** 2, axis=2)
        for j, i in enumerate(minCutPath(upL2.T)):
            minCut[:i, j] = True

    np.copyto(patch, result[y:y + dy, x:x + dx], where=minCut)

    return patch


def quilt(img_path, no_of_blocks, blockSize, mode, sequence=False):
    # reading the image from the image path
    texture = Image.open(img_path)
    # formatting the image as floating point
    texture = util.img_as_float(texture)

    no_of_blocks_height, no_of_blocks_width = no_of_blocks
    overlap = blockSize // 6

    # Generating the size of the target image
    w = (no_of_blocks_width * blockSize) - (no_of_blocks_width - 1) * overlap
    h = (no_of_blocks_height * blockSize) - (no_of_blocks_height - 1) * overlap

    result = np.zeros((h, w, texture.shape[2]))

    for i in range(no_of_blocks_height):
        for j in range(no_of_blocks_width):
            x = j * (blockSize - overlap)
            y = i * (blockSize - overlap)

            # performing random block placement
            if i == 0 and j == 0 or mode == "random":
                patch = randomPatch(texture, blockSize)
            elif mode == "best":
                patch = randomBestPatch(texture, blockSize, overlap, result, x, y)
            elif mode == "cut":
                patch = randomBestPatch(texture, blockSize, overlap, result, x, y)
                patch = minCutPatch(patch, blockSize, overlap, result, x, y)

            result[y:y + blockSize, x:x + blockSize] = patch

    image = Image.fromarray((result * 255).astype(np.uint8))
    return image

#texture synthesis using random block placeement
#quilt_output1 = quilt(img_path='weave.jpg', blockSize=50, no_of_blocks=(50, 50), mode="random", sequence=False)
#img2 = quilt_output1.save("Texture_Synthesis_random.jpg")

#texture synthesis involving calculating L2Norm error
#quilt_output2 = quilt(img_path='weave.jpg', blockSize=50, no_of_blocks=(50, 50), mode="best", sequence=False)
#img3 = quilt_output2.save("Texture_Synthesis_best.jpg")

#texture synthesis involving using minimum cost path
quilt_output = quilt(img_path='weave.jpg', blockSize=50, no_of_blocks=(50, 50), mode="cut", sequence=False)
img1 = quilt_output.save("Texture_Synthesis_cut1.jpg")




