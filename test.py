import tensorflow as tf
import numpy as np

image_label_list = open("file_paths.txt","r")

def read_my_file_format(filename_queue):
    reader = tf.WholeFileReader()
    key, value = reader.read(filename_queue)
    example = tf.image.decode_jpeg(value)
    return example

image_list = [line for line in image_label_list.readline()]

input_queue = tf.train.string_input_producer(image_list)
input_images = read_my_file_format(input_queue)
