import tensorflow as tf
import os
import datetime
import attr
import tensorflow_datasets as tfds

#tf.logging.set_verbosity(tf.logging.ERROR)
print(tf.__version__)

print(tf.config.experimental.list_physical_devices())

dataset, info = tfds.load('amazon_us_reviews/Mobile_Electronics_v1_00',with_info=True)
train_dataset=dataset['train']

print(f"train_dataset :- {train_dataset}")

print(f"info :- {info}")

#print(f"length of the dataset {len(list(train_dataset))}")

BUFFER_SIZE = 300
BATCH_SIZE = 10

#shuffle
print("shuffle the data to make sure training data set is a good mix, small batch size can skew the training data")
train_dataset = train_dataset.shuffle(BUFFER_SIZE, reshuffle_each_iteration=False)

#print 5 records, iterate through the loop take 5 rows
for reviews in train_dataset.take(5):
    print(reviews)

