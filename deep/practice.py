import tensorflow as tf
sess = tf.Session()
hello = tf.constant("Hello, TensorFlow!")
print(sess.run(hello))
a = tf.constant(111)
b = tf.constant(222)
add_op = a + b
sess.run(add_op)