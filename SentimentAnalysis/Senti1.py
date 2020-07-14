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

for reviews in train_dataset.take(20):
    review_text = reviews['data']
    print(review_text.get('review_body').numpy())
    print(review_text.get('star_rating'))
    print(tf.where(review_text.get('star_rating')>3,1,0).numpy())

tokenizer = tfds.features.text.Tokenizer()

vocabulary_set = set()

# for all data just .enumerate():
for _, reviews in train_dataset.take(1000).enumerate():
    #print(reviews)
    review_text = reviews['data']
    reviews_tokens = tokenizer.tokenize(review_text.get('review_body').numpy())
    vocabulary_set.update(reviews_tokens)

#print(vocabulary_set)

vocab_size = len(vocabulary_set)
print(f"vocab size {vocab_size}")

encoder = tfds.features.text.TokenTextEncoder(vocabulary_set)

for reviews in train_dataset.take(5):
    review_text = reviews['data']
    print(review_text.get('review_body').numpy())
    encoded_example = encoder.encode(review_text.get('review_body').numpy())
    print(encoded_example)