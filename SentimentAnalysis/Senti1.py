import tensorflow as tf
import os
import datetime
import attr
import tensorflow_datasets as tfds

#tf.logging.set_verbosity(tf.logging.ERROR)
print(tf.__version__)

print(tf.config.experimental.list_physical_devices())

dataset, info = tfds.load('amazon_us_reviews/Mobile_Electronics_v1_00',with_info=True)
train_dataset=data['train']