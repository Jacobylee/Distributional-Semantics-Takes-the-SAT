# Distributional-Semantics-Takes-the-SAT
Distributional semantics is one of the modern methods in natural language processing in solving tasks that require semantic knowledge of a word or relations between words. In this homework, we will learn how to create semantic representations of words from a corpus and how to use them in computational lexical semantic tasks.

Create distributional semantic word vectors

Code README
generate_co_matrix(filename):
		Given the txt file, return three parameters: co-occurrence matrix, PPMI matrix, and 			term index dictionary
euclidean(word1, word2):
		Given two vectors, calculate the Euclidean distance of the two vectors. (Print 				"Vectors have different dimension” if the vector dimensions are not equal)

Does PPMI do the right thing to the count matrix? Why?
		Yes. Because the PPMI matrix can see the relationship of the co-occurrence 				matrix, the higher the word’s frequency, the higher the PPMI value.
	
		Count matrix “dogs”:   [ 1. 11. 91.  1.  1. 31.  1.]
		PPMI  matrix “dogs”:   [0.   0.   0.60490439   0.   0.   1.1434224    0.   ]

Explain in a few sentences how PPMI helps.
		PMI measures the correlation between two variables. In probability theory, if x and 			y are unrelated, p(x, y)=p(x)p(y); if x and y are more related, p(x, y) ) And p(x)p(y) the 			greater the ratio. The PPMI value of high-frequency words is very high. Very 				common words such as “the”, its PPMI will be relatively low. And the effect of 				function word on semantics is smaller than content word

Do the distances you compute above confirm our intuition from distributional semantics (i.e. similar words appear in similar contexts)?	
		yes.The more relevant the word, the smaller the distance

Does the compact/reduced matrix still keep the information we need for each word vector?
		yes. Similar words are still close

SVD
---------SVD---------
U:
[[ 0.37230673  0.43322343 -0.18820229 -0.2427912   0.226526    0.50812791 -0.51945115]
 [ 0.26045118 -0.22721904  0.18344464 -0.18788652  0.22720271  0.56148711 0.66685423]
 [ 0.49355508 -0.33903632 -0.11985691  0.04830149 -0.77069021  0.13466881 -0.11251649]
 [ 0.36740391  0.35374508  0.6310224   0.58203466  0.00743366 -0.05275392 0.00932336]
 [ 0.40553839 -0.46531006  0.32579941 -0.36347644  0.36153672 -0.40888504 -0.28786979]
 [ 0.30604504 -0.23843033 -0.58724666  0.57451398  0.4048431  -0.08602128 0.05713899]
 [ 0.39603748  0.49723767 -0.25955562 -0.32011289 -0.0918668  -0.48065888 0.43196663]]
E:
[[1.76506662 0.         0.         0.         0.         0.	0.        ]
 [0.         1.35043894 0.         0.         0.         0.	0.        ]
 [0.         0.         1.1789961  0.         0.         0.	0.        ]
 [0.         0.         0.         1.17884721 0.         0.	0.        ]
 [0.         0.         0.         0.         0.44220794 0.	0.        ]
 [0.         0.         0.         0.         0.         0.3202968	0.        ]
 [0.         0.         0.         0.         0.         0.	  0.29256765]]
V:
[[ 0.37230673 -0.43322343  0.18820229 -0.2427912  -0.226526    0.50812791 0.51945115]
 [ 0.26045118  0.22721904 -0.18344464 -0.18788652 -0.22720271  0.56148711 -0.66685423]
 [ 0.49355508  0.33903632  0.11985691  0.04830149  0.77069021  0.13466881 0.11251649]
 [ 0.36740391 -0.35374508 -0.6310224   0.58203466 -0.00743366 -0.05275392 -0.00932336]
 [ 0.40553839  0.46531006 -0.32579941 -0.36347644 -0.36153672 -0.40888504 0.28786979]
 [ 0.30604504  0.23843033  0.58724666  0.57451398 -0.4048431  -0.08602128 -0.05713899]
 [ 0.39603748 -0.49723767  0.25955562 -0.32011289  0.0918668  -0.48065888 -0.43196663]]

U·E·V
[[ 0.	             0.56853597	0.56428788   0.                0.56853597   0.	            0.                ]
 [ 0.56853597 -0.                    0.26168976 -0.                 0.                 -0.	            0.30018777]
 [ 0.56428788  0.26168976     0.                 0.60490439  0.26168976  0.24332039	0.47994332]
 [ 0.                  0.                    0.60490439  0.                  0.                   1.1434224	 -0.              ]
 [ 0.56853597  0.                    0.26168976 -0.                  0.                  -0.		  0.94681494]
 [-0.                  0.                    0.24332039  1.1434224   0.                   0.                  -0.               ]
 [ 0.                  0.30018777   0.47994332   -0.                0.94681494    0.                  0.               ]]

Vector distances

Compute the Euclidean distance between the following pairs

		women and men:   0.4714018839533297
		women and dogs:  1.5197372396529087
		men and dogs:       1.3984029401866462
		feed and like:          0.6466271649250526
		feed and bite:         1.5897936639308878
		like and bite:          1.3119062712596168

Compute the Euclidean distances again but on the reduced PPMI-weighted count matrix.

		women and men:   0.12768975197385385
		women and dogs:  1.0689148903003787
		men and dogs:       0.9718464574250326
		feed and like:         0.44399330011666205
		feed and bite:        1.1329241779001433
		like and bite:          0.9123245004499333

Once normally and once using the reduced PPMI-weighted count matrix.
Index: {'men': 0, 'like': 1, 'the': 2, 'dogs': 3, 'feed': 4, 'bite': 5, 'women': 6}

co-occurrence matrix
[[ 1. 21. 81.  1. 21.  1.  1.]
 [21.  1. 41. 11.  1.  1. 11.]
 [81. 41.  1. 91. 41. 31. 51.]
 [ 1. 11. 91.  1.  1. 31.  1.]
 [21.  1. 41.  1.  1.  1. 21.]
 [ 1.  1. 31. 31.  1.  1.  1.]
 [ 1. 11. 51.  1. 21.  1.  1.]]

PPMI matrix:

[[0.                  0.56853597  0.56428788  0.                   0.56853597  0.		   0.                ]
 [0.56853597  0.                  0.26168976  0.                   0.                  0.		   0.30018777]
 [0.56428788  0.26168976  0.                  0.60490439   0.26168976  0.24332039     0.47994332]
 [0.                  0.                  0.60490439  0.                   0.                  1.1434224       0.                ]
 [0.56853597  0.                  0.26168976  0.                   0.                  0.		   0.94681494]
 [0.                  0.                  0.24332039  1.1434224     0.                  0.		   0.                ]
 [0.                  0.30018777  0.47994332  0.                   0.94681494  0.		   0.                ]]

reduced_PPMI:

[[ 0.65714617  0.58504179 -0.22188976]
 [ 0.45971368 -0.30684544  0.21628052]
 [ 0.8711576  -0.45784785 -0.14131083]
 [ 0.64849239  0.47771113  0.74397295]
 [ 0.71580227 -0.62837282  0.38411623]
 [ 0.54018988 -0.3219856  -0.69236152]
 [ 0.69903253  0.67148911 -0.30601506]]
Computing with distributional semantic word vectors

Code README
Class WordVectorModel
__init__(self, db_filename, questions, flag=True)
			db_filename: Vector Model file, input model file and convert to matrix
			questions: questions need to be run
			flag: Use cosine when True, euclidean when False
euclidean(v1, v2)
			Static function, input two vectors with equal dimensions to return euclidean 				distance
cosine(v1, v2)
			Static function, input two vectors with equal dimensions to return cosine 					similarity
synonym(self)
			Used to deal with the synonym problem set. 
			self.q_sets :  [{word: set(choice1, choice2, choice3, choice4, choice5)}, …]
			Save (question token, selected token) in self.results
			Save unknown token in self.unknown
analogy(self)
			Used to deal with the analogy problem set. 
			self.q_sets: [{(‘audacious’, 'boldness', Question number, answer): 						[('anonymous', 'identity'), ('remorseful', 'misdeed'), ('deleterious', 'result'), 				('impressionable', 'temptation'), ('sanctimonious', ‘hypocrisy’)]}, ….]
			return accuracy
synonym_detection_SAT.py
multiple_choice_database(filename):
			Read the txt file, store all the synonym pairs in a dictionary, the key is the 				word, and the value is the synonym of the word
question_generator(database, k):
			input a database which multiple_choice_database(filename) returned, use 				generator to yield k questions randomly. Format is {word: set(choice1, 					choice2, choice3, choice4, choice5)}.
sat_analogy(filename):
			Extract the question from the “filename” and use the generator to yield it, 				Format is {(‘audacious’, 'boldness', question number, answer): 						[('anonymous', 'identity'), ('remorseful', 'misdeed'), ('deleterious', 'result'), 				('impressionable', 'temptation'), ('sanctimonious', ‘hypocrisy')]}
accuracy(result, db):
			Given the result and the database, judge whether it is a synonym based on 				the word pair in the result and return the accuracy rate

Synonym detection
unknown words method

Save the score of the unknown word as -100 so that it will not be selected. (Because cosine chooses the largest score and euclidean chooses the smallest, so I save euclidean as the opposite, -100 is guaranteed not to be selected. If the question is unknown, ignore this question.)

A table comparing the synonym test results using Euclidean distance vs. cosine similarity and COMPOSES vs. word2vec.

SAT Analogy questions

unknown words method

		If one of the two words in the question is unknown, an answer is randomly 				selected. If any word in the option is unknown, set its score to -100 for making sure 		it’s cannot be selected.

what you have tried and your results(subtracting the two word vectors)

		I used the vector difference of the two tokens of the question as the target vector, 			calculated the vector difference of each pair in the options, and judged the gap 				with the target vector, and chose the smallest gap.
		
		The vector of the token indirectly expresses the meaning of the vocabulary, 				and the distance between two tokens vectors can indirectly indicate the 					association of them. If the meanings of the question’s word pairs are similar, then 			the target vector will be small, choose the minimum difference between the target 			vector and options’ vector difference. For example, "man"-"woman" is 					approximately equal to "king"-"queen". The hidden meaning of the gap is gender. 			Regarding how to define "similar", the most important thing is relationship. The 				vector difference can represent this relationship. Two words, "cat" and "dog", both 			appear together with "pet, cute, animal...", then "cat" and "dog" belong to a similar 		relationship. For (words, letters) this kind of subordination is also a kind of 				relationship. The words that appear with "cat" such as "pet, cute, animal" are "cat 			context". Cat is the "target word". At this time, the vectors of cats and dogs 				represent their contextual content.

		I tried four combinations of two matrices and two distances. Among them, 				word2vector and cosine similarity have the highest accuracy. Around 0.4

SAT analogy (COMPOSES cosine) Accuracy:      0.38 
SAT analogy (COMPOSES euclidean) Accuracy: 0.35 
SAT analogy (word2vector cosine) Accuracy:       0.41 
SAT analogy (word2vector euclidean) Accuracy:  0.31 
