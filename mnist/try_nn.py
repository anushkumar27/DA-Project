import tensorflow as tf
import numpy as np
import math

STU_TRAINING = 'stu-por-train.csv'
STU_TEST = 'stu-por-test.csv'

#training_set = tf.contrib.learn.datasets.base.load_csv(filename=IRIS_TRAINING, target = np.int)
#test_set = tf.contrib.learn.datasets.base.load_csv(filename=IRIS_TEST, target = np.int)

training_set = tf.contrib.learn.datasets.base.load_csv_without_header(filename=STU_TRAINING, target_dtype = np.int, features_dtype=np.int)
test_set = tf.contrib.learn.datasets.base.load_csv_without_header(filename=STU_TEST, target_dtype = np.int, features_dtype=np.int)

feature_columns = [tf.contrib.layers.real_valued_column('', dimension = 9)]

classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                            hidden_units = [10,20,10],
					    n_classes = 21,
					    model_dir = 'por_model')

classifier.fit(x=training_set.data, y=training_set.target, steps=2000)

pred = list(classifier.predict(test_set.data, as_iterable=True))

#print(test_set.target[0], pred[0][0])

rmse = 0
n = len(test_set.target)

for i in range(n):
	rmse += math.sqrt(math.pow(test_set.target[i] - pred[i][0],2))

#rmse = math.sqrt(rmse)
rmse /= n

print('rmse:',rmse)

acc_score = classifier.evaluate(x=test_set.data, y=test_set.target)
print('acc_score:',acc_score)
