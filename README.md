# Distributional-Semantics-Takes-the-SAT
Distributional semantics is one of the modern methods in natural language processing in solving tasks that require semantic knowledge of a word or relations between words. In this homework, we will learn how to create semantic representations of words from a corpus and how to use them in computational lexical semantic tasks.

1. Create distributional semantic word vectors

# Code README
generate_co_matrix(filename):
		Given the txt file, return three parameters: co-occurrence matrix, PPMI matrix, and term index dictionary
euclidean(word1, word2):
		Given two vectors, calculate the Euclidean distance of the two vectors. (Print "Vectors have different dimension” if the vector dimensions are not equal)

Computing with distributional semantic word vectors

# Code README
# Class WordVectorModel
__init__(self, db_filename, questions, flag=True)
			db_filename: Vector Model file, input model file and convert to matrix
			questions: questions need to be run
			flag: Use cosine when True, euclidean when False
euclidean(v1, v2)
			Static function, input two vectors with equal dimensions to return euclidean distance
cosine(v1, v2)
			Static function, input two vectors with equal dimensions to return cosine similarity
synonym(self)
			Used to deal with the synonym problem set. 
			self.q_sets :  [{word: set(choice1, choice2, choice3, choice4, choice5)}, …]
			Save (question token, selected token) in self.results
			Save unknown token in self.unknown
analogy(self)
			Used to deal with the analogy problem set. 
			self.q_sets: [{(‘audacious’, 'boldness', Question number, answer): [('anonymous', 'identity'), ('remorseful', 'misdeed'), ('deleterious', 'result'),('impressionable', 'temptation'), ('sanctimonious', ‘hypocrisy’)]}, ….]
			return accuracy
# synonym_detection_SAT.py
multiple_choice_database(filename):
			Read the txt file, store all the synonym pairs in a dictionary, the key is the word, and the value is the synonym of the word
question_generator(database, k):
			input a database which multiple_choice_database(filename) returned, use generator to yield k questions randomly. Format is {word: set(choice1, choice2, choice3, choice4, choice5)}.
sat_analogy(filename):
			Extract the question from the “filename” and use the generator to yield it, Format is {(‘audacious’, 'boldness', question number, answer): [('anonymous', 'identity'), ('remorseful', 'misdeed'), ('deleterious', 'result'), ('impressionable', 'temptation'), ('sanctimonious', ‘hypocrisy')]}
accuracy(result, db):
			Given the result and the database, judge whether it is a synonym based on the word pair in the result and return the accuracy rate


Synonym detection

unknown words method

Save the score of the unknown word as -100 so that it will not be selected. (Because cosine chooses the largest score and euclidean chooses the smallest, so I save euclidean as the opposite, -100 is guaranteed not to be selected. If the question is unknown, ignore this question.)


SAT Analogy questions

unknown words method

		If one of the two words in the question is unknown, an answer is randomly selected. If any word in the option is unknown, set its score to -100 for making sure t’s cannot be selected.

what you have tried and your results(subtracting the two word vectors)

		I used the vector difference of the two tokens of the question as the target vector, calculated the vector difference of each pair in the options, and judged the gap with the target vector, and chose the smallest gap.
		
		The vector of the token indirectly expresses the meaning of the vocabulary, and the distance between two tokens vectors can indirectly indicate the association of them. If the meanings of the question’s word pairs are similar, then the target vector will be small, choose the minimum difference between the target vector and options’ vector difference. For example, "man"-"woman" is approximately equal to "king"-"queen". The hidden meaning of the gap is gender. Regarding how to define "similar", the most important thing is relationship. The vector difference can represent this relationship. Two words, "cat" and "dog", both appear together with "pet, cute, animal...", then "cat" and "dog" belong to a similar relationship. For (words, letters) this kind of subordination is also a kind of relationship. The words that appear with "cat" such as "pet, cute, animal" are "cat context". Cat is the "target word". At this time, the vectors of cats and dogs represent their contextual content.

		I tried four combinations of two matrices and two distances. Among them,word2vector and cosine similarity have the highest accuracy. Around 0.4

SAT analogy (COMPOSES cosine) Accuracy:      0.38 
SAT analogy (COMPOSES euclidean) Accuracy: 0.35 
SAT analogy (word2vector cosine) Accuracy:       0.41 
SAT analogy (word2vector euclidean) Accuracy:  0.31 
