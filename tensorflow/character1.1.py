import tensorflow as tf
import numpy as np

matrix1=tf.constant([[3.1,3.]])
matrix2=tf.constant([[2.],[3.]])

product=tf.matmul(matrix1,matrix2)

with tf.Session() as sess:
    with tf.device("/gpu:1"):
        print sess.run(product)
