
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import tensorflow as tf


# In[33]:


#dataset = pd.read_csv('data-03-diabetes.csv').as_matrix()
dataset = pd.read_csv('test.csv').as_matrix()
train_data = np.array(dataset[:,0:-1])
train_label = np.array(dataset[:,[-1]])

for i in range(len(train_data)):
    for j in range(len(train_data[0])):
        train_data[i][j] = train_data[i][j]/10


feature = tf.placeholder(tf.float32, shape = [None,2])
PF = tf.placeholder(tf.float32, shape=[None,1])

# feature = tf.placeholder(tf.float32, shape = [None,8])
# PF = tf.placeholder(tf.float32, shape=[None,1])

W = tf.Variable(tf.random_normal([2,1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

# W = tf.Variable(tf.random_normal([8,1]), name = 'weight')
# b = tf.Variable(tf.random_normal([1]), name = 'bias')

hypothesis = tf.sigmoid(tf.matmul(feature, W) + b)

cost = -tf.reduce_mean(PF * tf.log(hypothesis) + (1-PF) * tf.log(1 - hypothesis))
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.01)
train = optimizer.minimize(cost)

predicted = tf.cast(hypothesis > 0.5, dtype = tf.float32)
acc = tf.reduce_mean(tf.cast(tf.equal(predicted, PF), dtype = tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    feed = {feature:train_data, PF:train_label}
        
    for step in range(1000):
        cost_val, _ = sess.run([cost, train], feed_dict = {feature:train_data, PF:train_label})
        if step % 100 == 0:
            print(step, cost_val)
        
    h, c, a = sess.run([hypothesis, predicted, acc], feed_dict=feed)
    print("\nhypothesis : ", h, "\ncorrect : ", c, "accuracy : ", a)
    
    print(sess.run(predicted,feed_dict={feature:[[9.9,9.9],[1,1]],PF:[[1],[0]]}))

