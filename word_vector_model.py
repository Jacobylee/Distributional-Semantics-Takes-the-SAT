import numpy as np
import scipy.linalg as scipy_linalg
from random import choice


class WordVectorModel:
    def __init__(self, db_filename, questions, flag=True):
        print("generating model...", end="")
        dsm = []
        index = {}
        line_point = 0
        with open(db_filename) as f:
            for line in f:
                index[line.split()[0]] = line_point
                vector = list(map(float, line.split()[1:]))
                dsm.append(np.array(vector))
                line_point += 1
        f.close()
        print("Done!")

        self.dsm = np.mat(dsm)
        self.index = index
        self.q_sets = questions
        self.unknown = []
        self.results = []
        self.flag = flag

    @staticmethod
    def euclidean(v1, v2):
        if len(v1) != len(v2):
            return ValueError
        else:
            return scipy_linalg.norm(v1-v2)

    @staticmethod
    def cosine(v1, v2):
        if len(v1) != len(v2):
            return ValueError
        else:
            return np.dot(v1, v2) / (scipy_linalg.norm(v1) * scipy_linalg.norm(v2))

    def synonym(self):
        # q.sets :  [{word: set(choice1, choice2, choice3, choice4, choice5)}, ....]
        with open("synonym.txt", "w") as f:
            for mc_question in self.q_sets:
                token = list(mc_question.keys())[0]
                target = token[3:]
                if target in self.index.keys():
                    f.write("---------------------\n")
                    f.write("Question: %s \n" % token)
                    target_vector = np.array(self.dsm[self.index[target]])[0]
                    option_scores = {}
                    for option in list(mc_question.values())[0]:
                        opt = option[3:]
                        f.write("Selection: %s \n" % option)
                        if opt in self.index.keys():
                            opt_vector = np.array(self.dsm[self.index[opt]])[0]
                            if self.flag:
                                option_scores[self.cosine(target_vector, opt_vector)] = option  # cosine
                            else:
                                option_scores[-self.euclidean(target_vector, opt_vector)] = option  # euclidean use negative
                        else:
                            option_scores[-100] = option
                    selected = option_scores[max(option_scores.keys())]
                    self.results.append((token, selected))
                else:
                    self.unknown.append(token)

    def analogy(self):
        tp = 0
        fp = 0
        for as_question in self.q_sets:
            word1 = list(as_question.keys())[0][0]
            word2 = list(as_question.keys())[0][1]
            question_num = list(as_question.keys())[0][2]
            answer = list(as_question.values())[0][list(as_question.keys())[0][3]]
            if word1 in self.index.keys() and word2 in self.index.keys():
                word1_vector = np.array(self.dsm[self.index[word1]])[0]
                word2_vector = np.array(self.dsm[self.index[word2]])[0]
                word_diff = word1_vector-word2_vector
                option_scores = {}
                for option in list(as_question.values())[0]:
                    option1 = option[0]
                    option2 = option[1]
                    if option1 in self.index.keys() and option2 in self.index.keys():
                        option1_vector = np.array(self.dsm[self.index[option1]])[0]
                        option2_vector = np.array(self.dsm[self.index[option2]])[0]
                        option_diff = option1_vector-option2_vector
                        if self.flag:
                            option_scores[self.cosine(word_diff, option_diff)] = option  # cosine
                        else:
                            option_scores[-self.euclidean(word_diff, option_diff)] = option  # euclidean use negative
                    else:
                        option_scores[-100] = (option[0], option[1])
                selected = option_scores[max(option_scores.keys())]
                self.results.append((question_num, selected))
            else:
                self.unknown.append((word1, word2))
                selected = choice(list(as_question.values())[0])
            if answer == selected:
                tp += 1
            else:
                fp += 1
        return tp/(fp+tp)
