import numpy as np
from nltk import bigrams
import scipy.linalg as scipy_linalg


def generate_co_matrix(filename):
    # read
    data = open(filename).readlines()
    # terms and bi grams
    bi_grams = []
    voca = []
    for line in data:
        voca += line.split()
        bi_grams += list(bigrams(line.split()))
    vocas = list(set(voca))
    # term index
    term_index = {word: i for i, word in enumerate(vocas)}
    # co_matrix
    co_matrix = np.zeros((len(vocas), len(vocas)), np.float64)
    for bi in bi_grams:
        co_matrix[term_index[bi[0]]][term_index[bi[1]]] += 1
        co_matrix[term_index[bi[1]]][term_index[bi[0]]] += 1
    # smooth
    co_matrix = (co_matrix * 10) + 1
    # PPMI
    ppmi = np.zeros((len(vocas), len(vocas)), np.float64)
    all_count = np.sum(co_matrix)
    for word in range(len(co_matrix)):
        for context in range(len(co_matrix[word])):
            pw = sum(co_matrix[word]) / all_count
            pc = sum(co_matrix[:, context]) / all_count
            pwc = co_matrix[word][context] / all_count
            ppmi[word][context] = max(np.log(pwc/(pw*pc)), 0)

    return co_matrix, ppmi, term_index


def euclidean(word1, word2):
    if len(word1) == len(word2):
        return scipy_linalg.norm(word1-word2)
    else:
        print("Vectors have different dimension")


co = generate_co_matrix("dist_sim_data.txt")[0]
PPMI = generate_co_matrix("dist_sim_data.txt")[1]
index = generate_co_matrix("dist_sim_data.txt")[2]
print("Index:", index)
print("co-occurrence matrix")
print(co)
print("PPMI matrix:")
print(PPMI)
print("dogs co-occurrence: ", co[index["dogs"]])
print("dogs PPMI: ", PPMI[index["dogs"]])
print("-------distance------")
print("women and men: ", euclidean(PPMI[index["women"]], PPMI[index["men"]]))
print("women and dogs: ", euclidean(PPMI[index["women"]], PPMI[index["dogs"]]))
print("men and dogs: ", euclidean(PPMI[index["men"]], PPMI[index["dogs"]]))
print("feed and like: ", euclidean(PPMI[index["feed"]], PPMI[index["like"]]))
print("feed and bite: ", euclidean(PPMI[index["feed"]], PPMI[index["bite"]]))
print("like and bite: ", euclidean(PPMI[index["like"]], PPMI[index["bite"]]))
print("---------SVD---------")
U, E, Vt = scipy_linalg.svd(PPMI, full_matrices=False)
U = np.matrix(U)  # compute U
E = np.matrix(np.diag(E))  # compute E
Vt = np.matrix(Vt)  # compute Vt = conjugage transpose of V
V = Vt.T  # compute V = conjugate transpose of Vt
print("U:")
print(U)
print("E:")
print(E)
print("V:")
print(V)
print("U·E·V")
print(np.around(np.dot(np.dot(U, E), Vt), decimals=8))
print("---------3D---------")
reduced_PPMI = np.around(PPMI * V[:, 0:3], decimals=8)
print("reduced_PPMI:")
print(reduced_PPMI)
print("women and men: ", euclidean(reduced_PPMI[index["women"]], reduced_PPMI[index["men"]]))
print("women and dogs: ", euclidean(reduced_PPMI[index["women"]], reduced_PPMI[index["dogs"]]))
print("men and dogs: ", euclidean(reduced_PPMI[index["men"]], reduced_PPMI[index["dogs"]]))
print("feed and like: ", euclidean(reduced_PPMI[index["feed"]], reduced_PPMI[index["like"]]))
print("feed and bite: ", euclidean(reduced_PPMI[index["feed"]], reduced_PPMI[index["bite"]]))
print("like and bite: ", euclidean(reduced_PPMI[index["like"]], reduced_PPMI[index["bite"]]))
