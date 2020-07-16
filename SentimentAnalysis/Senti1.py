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

#print(f"train_dataset :- {train_dataset}")

#print(f"info :- {info}")

#print(f"length of the dataset {len(list(train_dataset))}")

BUFFER_SIZE = 100
BATCH_SIZE = 128

#shuffle
print("shuffle the data to make sure training data set is a good mix, small batch size can skew the training data")
train_dataset = train_dataset.shuffle(BUFFER_SIZE, reshuffle_each_iteration=False)

#print 5 records, iterate through the loop take 5 rows
#for reviews in train_dataset.take(5):
#    print(reviews)

for reviews in train_dataset.take(20):
    review_text = reviews['data']
#    print(review_text.get('review_body').numpy())
#    print(review_text.get('star_rating'))
#    print(tf.where(review_text.get('star_rating')>3,1,0).numpy())

tokenizer = tfds.features.text.Tokenizer()

vocabulary_set = set()

# for all data just .enumerate():
for _, reviews in train_dataset.take(600).enumerate():
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
    #print(review_text.get('review_body').numpy())
    encoded_example = encoder.encode(review_text.get('review_body').numpy())
    #print(encoded_example)

#for index in encoded_example:
    #print('{} ----> {}'.format(index,encoder.decode([index])))

def encode(text_tensor, label_tensor):
    encoded_text = encoder.encode(text_tensor.numpy())
    label = tf.where(label_tensor>3,1,0)
    return encoded_text, label

def encode_map_fn(tensor):
    text = tensor['data'].get('review_body')
    label = tensor['data'].get('star_rating')

    encoded_text, label = tf.py_function(encode,
                                         inp=[text,label],
                                         Tout=(tf.int64,tf.int32))
    encoded_text.set_shape([None])
    label.set_shape([])

    return encoded_text, label

ar_encoded_data = train_dataset.map(encode_map_fn)

#for f0,f1 in ar_encoded_data.take(5):
#    print(f"f0 encoded review body:- {f0}")
#    print(f"f1 encoded star rating:- {f1}")

TAKE_SIZE = 100

# skip the number of records specified in TAKE_SIZE and assign remaining to train data
# text data will be variable length, pad

train_data = ar_encoded_data.skip(TAKE_SIZE).shuffle(BUFFER_SIZE)
train_data = train_data.padded_batch(BATCH_SIZE)

test_data = ar_encoded_data.take(TAKE_SIZE)
test_data = test_data.padded_batch(BATCH_SIZE)

vocab_size += 1
print(f"vocab_size increased {vocab_size}")
sample_text, sample_labels = next(iter(test_data))

#print(sample_text[0])
#print(sample_labels[0])

#print(sample_text[1])
#print(sample_labels[1])

#for f0,f1 in test_data.take(10):
#    print(tf.unique_with_counts(f1)[2].numpy())

print("model define started")
model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(vocab_size + 1000,128))  # was getting an arrayoutbound kind of exception, so increased vocab size by 1000 randomly
#model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(128,return_sequences=True)))
#model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)))
for units in [64]: #,64]:
    model.add(tf.keras.layers.Dense(units,activation='relu'))
model.add(tf.keras.layers.Dense(1))

print(f"model summary :- {model.summary()}")

print("set tensorboar callback and checkpoints")
logdir = os.path.join("/home/pk/pycharm/logs",datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
tensorboard_callback = tf.keras.callbacks.TensorBoard(logdir,histogram_freq=1)
checkpointer = tf.keras.callbacks.ModelCheckpoint(filepath='/home/pk/pycharm/sentiment_analysis.hdf5',verbose=1,save_best_only=True)

print("model compile started")
model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])

print("model fit started")
history=model.fit(train_data,epochs=2,validation_data=test_data,callbacks=[tensorboard_callback,checkpointer])

model.save('/home/pk/pycharm/final_sentiment_analysis.hdf5')

# we didn't use a sigmoid function, we used a linear function so we won't predict 0 and 1
# model will predict -ve and +ve numbers and we have to interpret with a threshold

print(model.layers)