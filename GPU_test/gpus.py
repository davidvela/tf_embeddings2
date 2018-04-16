import tensorflow as tf
import time
from datetime import datetime

def test1_dp(): # logging device placement
    # Creates a graph.
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
    c = tf.matmul(a, b)
    # Creates a session with log_device_placement set to True.
    sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
    # Runs the op.
    print(sess.run(c))
    print("logging device placement")

def test2_mp(): # manual placement 
    # Creates a graph.
    with tf.device('/cpu:0'):
        a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
        b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
    c = tf.matmul(a, b)
    # Creates a session with log_device_placement set to True.
    sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
    # Runs the op.
    print(sess.run(c))
    print("Manual placement")

def test3_gg(): # Allow GPU Memory Grow 
    #By default, TensorFlow maps nearly all of the GPU memory of all GPUs ... 
    config = tf.ConfigProto()
    # config.gpu_options.per_process_gpu_memory_fraction = 0.4 - only 40%
    config.gpu_options.allow_growth = True
    # session = tf.Session(config=config, ...)

def test4_mg(): # Allow multiple GPUs
    # Creates a graph.
    c = []
    for d in ['/device:GPU:0', '/device:GPU:1']:
        with tf.device(d):
            a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3])
            b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2])
            c.append(tf.matmul(a, b))
    with tf.device('/cpu:0'):
        sum = tf.add_n(c)
    # Creates a session with log_device_placement set to True.
    sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
    # Runs the op.
    print(sess.run(sum))
    print("Multiple GPUs")

def test5_ms1(): # check model size
    # Creates a graph.
    tf_config = tf.ConfigProto(allow_soft_placement=False) #,log_device_placement=True)
    # tf_config.gpu_options.allow_growth = True

    c = []
    for d in ['/device:GPU:0', '/device:GPU:1']:
        with tf.device(d):
            a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3])
            b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2])
            c.append(tf.matmul(a, b))
    # with tf.device('/cpu:0'):
            sum = tf.add_n(c)
    with tf.Session(config=tf_config) as sess:
        for i in range(1000000):
            r = sess.run(sum)
            # if i % 5000 == 0 : print(i)
        print(r)
    # Creates a session with log_device_placement set to True.
    sess = tf.Session(config= tf_config)

    # Runs the op.
    print(sess.run(sum))
    print("Model Size")

def test5_ms2(): # check model size
    # Creates a graph.
    tf_config = tf.ConfigProto(allow_soft_placement=False) #,log_device_placement=True)
    # tf_config.gpu_options.allow_growth = True
    dim = 4
    aa = []; bb = []
    for i in range(dim): 
        aa.append(float(i))
        bb.append(float(i))
    c = []
    print(aa)
    for d in ['/device:GPU:0', '/device:GPU:1']:
        # with tf.device('/cpu:0'):
        with tf.device(d):
            # a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3])
            # b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2])
            a = tf.constant(aa, shape=[dim/2, dim/2])
            b = tf.constant(bb, shape=[dim/2, dim/2])
            c.append(tf.matmul(a, b))
            d = tf.matmul(a,b)
    # with tf.device('/cpu:0'):
            sum = tf.add_n(c)

    with tf.Session(config=tf_config) as sess:
        for i in range(epochs):
            r1 = sess.run(sum)
            r2 = sess.run(d)
            if i % 5000 == 0 : print(i)
        print(r)
    # Creates a session with log_device_placement set to True.
    sess = tf.Session(config= tf_config)

    # Runs the op.
    print(sess.run(sum))
    print("Model Size")

def test5_ms3(): # check model size
    # Creates a graph.
    tf_config = tf.ConfigProto(allow_soft_placement=True) #,log_device_placement=True)
    tf_config.gpu_options.allow_growth = True
    
    dim = 10000
    aa = []; bb = []
    for i in range(dim): 
        aa.append(float(i))
        bb.append(float(i))
    c = []
    print(aa)

    with tf.device('/cpu:0'):
        # a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3])
        # b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2])
        a = tf.constant(aa, shape=[dim/2, dim/2])
        b = tf.constant(bb, shape=[dim/2, dim/2])

    # with tf.device('/gpu:1'):
        d = tf.matmul(a,b)
        d1 = tf.matmul(a,b)
    
    # with tf.device('/gpu:0'):
        c.append(tf.matmul(a, b))
        s = tf.add_n(c)
        s1 = tf.add_n(c)
    
    start = time.time()    
    with tf.Session(config=tf_config) as sess:
        for i in range(epochs):
            r1 = sess.run([s,s1])
            r2 = sess.run([d,d1])
            if i % dis == 0 : print(i)
        print(r1)
    calc_time(start)
    
    # Creates a session with log_device_placement set to True.
    sess = tf.Session(config= tf_config)

    # Runs the op.
    print(sess.run(s))
    print("Model Size")

def calc_time(start):
    print(datetime.now().strftime('%H:%M:%S'))
    elapsed_time = float(time.time() - start)
    print("loop - {} - time:{}" .format( epochs, elapsed_time ))

# main    
if __name__ == '__main__':
    print(datetime.now().strftime('%H:%M:%S'))

    epochs = 100
    dis = epochs/5

    start = time.time()    
    
    # test1_dp()
    # test2_mp()
    # test4_mg()
    test5_ms3()

    calc_time(start)
