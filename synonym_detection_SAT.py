from collections import defaultdict
from random import choice, sample
from word_vector_model import WordVectorModel


#   transfer txt to dictionary
def multiple_choice_database(filename):
    data = open(filename).readlines()
    data_base = defaultdict(list)
    for line in data[1:]:
        if line.split()[1] != '0' and line.split()[1] not in data_base[line.split()[0]]:
            data_base[line.split()[0]].append(line.split()[1])
    return data_base


#   yield question from dictionary(synonym)
def question_generator(database, k):
    verbs = list(database.keys())
    all_words = set(verbs+sum(list(database.values()), []))
    for i in range(k):
        question = defaultdict(set)
        verb = choice(verbs)
        question[verb].add(choice(database[verb]))
        question[verb].update(sample(set(filter(lambda x: x not in database[verb], all_words)), 4))
        yield question
        i += 1


#    yield question from txt file(analogy)
def sat_analogy(filename):
    data_base = []
    start_token = ['#', '190', 'ML:', 'KS']
    char_index = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
    with open(filename) as f:
        for line in f:
            line_list = line.split()
            if len(line_list) != 0:
                if line_list[0] in start_token:
                    continue
                else:
                    data_base.append(line_list)
    sat_questions = {}
    sat_selections = {}
    sat_answers = {}
    for lst in range(len(data_base)//7):
        sat_questions[lst] = data_base[lst*7]
        sat_answers[lst] = data_base[lst*7+6]
        sat_choice = []
        for choices in data_base[lst*7+1:lst*7+6]:
            sat_choice.append((choices[0], choices[1]))
        sat_selections[lst] = sat_choice

    for sat in sat_questions:
        question = (sat_questions[sat][0], sat_questions[sat][1], sat, char_index[sat_answers[sat][0]])
        yield {question: sat_selections[sat]}


#   given database and result to calculus the accuracy(synonym)
def accuracy(result, db):
    tp = 0
    fp = 0
    for pair in result:
        if pair[1] in db[pair[0]]:
            tp += 1
        else:
            fp += 1
    return round(tp / (tp + fp), 2)


if __name__ == "__main__":
    # Q1
    # build database
    synonym_db = multiple_choice_database("EN_syn_verb.txt")
    # build multiple choice questions
    synonym_sets = [q for q in question_generator(synonym_db, 1000)]

    composes_with_cosine = WordVectorModel("EN-wform.w.2.ppmi.svd.500.rcv_vocab.txt", synonym_sets, flag=True)  # cosine
    composes_with_cosine.synonym()
    cc_result = accuracy(composes_with_cosine.results, synonym_db)

    composes_with_euclidean = WordVectorModel("EN-wform.w.2.ppmi.svd.500.rcv_vocab.txt", synonym_sets, flag=False)  # Eucli
    composes_with_euclidean.synonym()
    ce_result = accuracy(composes_with_euclidean.results, synonym_db)

    word2vec_with_cosine = WordVectorModel("GoogleNews-vectors-rcv_vocab.txt", synonym_sets, flag=True)  # cosine
    word2vec_with_cosine.synonym()
    wc_result = accuracy(word2vec_with_cosine.results, synonym_db)

    word2vec_with_euclidean = WordVectorModel("GoogleNews-vectors-rcv_vocab.txt", synonym_sets, flag=False)  # eu
    word2vec_with_euclidean.synonym()
    we_result = accuracy(word2vec_with_euclidean.results, synonym_db)

    print("accuracy  cos     euclidean")
    print("COMPOSES", cc_result, "   ", ce_result)
    print("word2vec", wc_result, "   ", we_result)

    # Q2
    # build analogy questions
    analogy_sets = [i for i in sat_analogy("SAT-package-V3.txt")]

    analogy_composes_cosine = WordVectorModel("EN-wform.w.2.ppmi.svd.500.rcv_vocab.txt", analogy_sets, flag=True)  # cosine
    print("SAT analogy (COMPOSES cosine) Accuracy: %.2f " % analogy_composes_cosine.analogy())

    analogy_composes_euclidean = WordVectorModel("EN-wform.w.2.ppmi.svd.500.rcv_vocab.txt", analogy_sets, flag=False)  # eu
    print("SAT analogy (COMPOSES euclidean) Accuracy: %.2f " % analogy_composes_euclidean.analogy())

    analogy_word2vec_cosine = WordVectorModel("GoogleNews-vectors-rcv_vocab.txt", analogy_sets, flag=True)  # cosine
    print("SAT analogy (word2vector cosine) Accuracy: %.2f " % analogy_word2vec_cosine.analogy())

    analogy_word2vec_euclidean = WordVectorModel("GoogleNews-vectors-rcv_vocab.txt", analogy_sets, flag=False)  # eu
    print("SAT analogy (word2vector euclidean) Accuracy: %.2f " % analogy_word2vec_euclidean.analogy())

