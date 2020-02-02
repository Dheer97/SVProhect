import numpy as np
import os
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
from scipy import ndimage
from skimage.measure import regionprops
from skimage import io
from skimage.filters import threshold_otsu   # For finding the threshold for grayscale to binary conversion
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import pandas as pd
import numpy as np
from time import time
import keras
from tensorflow.python.framework import ops
ops.reset_default_graph()
import ipywidgets as widgets
import IPython.display as display
from tkinter import *
import tkinter
import Pmw
from PIL import Image,ImageTk 
import tkinter.filedialog
import FeatureExtraction as fe 

def testing(path):
    feature = fe.getCSVFeatures(path)
    if not(os.path.exists('DataSet/TestFeatures')):
        os.makedirs('DataSet/TestFeatures')
    with open('DataSet\\TestFeatures/testcsv.csv', 'w') as handle:
        handle.write('ratio,cent_y,cent_x,eccentricity,solidity,skew_x,skew_y,kurt_x,kurt_y\n')
        handle.write(','.join(map(str, feature))+'\n')


def demofunc(train_person_id,test_image_path): 

    train_path = 'DataSet\\Features\\Training/training_'+train_person_id+'.csv'
    #testing(paths)
    testing(test_image_path)
    test_path = 'DataSet\\TestFeatures/testcsv.csv'
                                            #True
    def readCSV(train_path, test_path, type2=False):
        # Reading train data
        df = pd.read_csv(train_path, usecols=range(n_input))
        train_input = np.array(df.values)
        train_input = train_input.astype(np.float32, copy=False)  # Converting input to float_32
        #Reading train data
        df = pd.read_csv(train_path, usecols=(n_input,))
        temp = [elem[0] for elem in df.values]
        correct = np.array(temp)
        corr_train = keras.utils.to_categorical(correct,2)      # Converting to one
        # Reading test data
        df = pd.read_csv(test_path, usecols=range(n_input))
        test_input = np.array(df.values)
        test_input = test_input.astype(np.float32, copy=False)
        if not(type2):
            df = pd.read_csv(test_path, usecols=(n_input,))
            temp = [elem[0] for elem in df.values]
            correct = np.array(temp)
            corr_test = keras.utils.to_categorical(correct,2)      # Converting to one 
        if not(type2):
            return train_input, corr_train, test_input, corr_test
        else:
            return train_input, corr_train, test_input

    ops.reset_default_graph()
    # Parameters
    learning_rate = 0.001
    training_epochs = 1000
    display_step = 1

    # Network Parameters
    n_hidden_1 = 7 # 1st layer number of neurons
    n_hidden_2 = 10 # 2nd layer number of neurons
    n_hidden_3 = 30 # 3rd layer
    n_classes = 2 # no. of classes (genuine or forged)

    # tf Graph input
    X = tf.placeholder("float", [None, n_input])
    Y = tf.placeholder("float", [None, n_classes])

    # Store layers weight & bias
    weights = {
        'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1], seed=1)),
        'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
        'h3': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_3])),
        'out': tf.Variable(tf.random_normal([n_hidden_1, n_classes], seed=2))
    }
    biases = {
        'b1': tf.Variable(tf.random_normal([n_hidden_1], seed=3)),
        'b2': tf.Variable(tf.random_normal([n_hidden_2])),
        'b3': tf.Variable(tf.random_normal([n_hidden_3])),
        'out': tf.Variable(tf.random_normal([n_classes], seed=4))
    }


    # Create model
    def multilayer_perceptron(x):
        layer_1 = tf.tanh((tf.matmul(x, weights['h1']) + biases['b1']))
        layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
        layer_3 = tf.add(tf.matmul(layer_2, weights['h3']), biases['b3'])
        out_layer = tf.tanh(tf.matmul(layer_1, weights['out']) + biases['out'])
        return out_layer

    # Construct model
    logits = multilayer_perceptron(X)


    loss_op = tf.reduce_mean(tf.squared_difference(logits, Y))
    #minimize the error
    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)  
    train_op = optimizer.minimize(loss_op)
    # For accuracies
    pred = tf.nn.softmax(logits) 
    correct_prediction = tf.equal(tf.argmax(pred,1), tf.argmax(Y,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    # Initializing the variables
    init = tf.global_variables_initializer()

    def evaluate(train_path, test_path, type2=TRUE):   
        if not(type2):
            train_input, corr_train, test_input, corr_test = readCSV(train_path, test_path)
        else:
            train_input, corr_train, test_input = readCSV(train_path, test_path, type2)
        ans = 'Random'
        with tf.Session() as sess:
           
            for epoch in range(training_epochs):                
                _, cost = sess.run([train_op, loss_op], feed_dict={X: train_input, Y: corr_train})
                if cost<0.0001:
                    break
                if epoch % 999 == 0:
                    print("Epoch:", '%04d' % (epoch+1), "cost={:.9f}".format(cost))
                #print("Optimization Finished!")
            
            # Finding accuracies
            accuracy1 =  accuracy.eval({X: train_input, Y: corr_train})
            print("Accuracy for train:", accuracy1)
            #print("Accuracy for test:", accuracy2)
            if type2 is False:
                accuracy2 =  accuracy.eval({X: test_input, Y: corr_test})
                print("Accuracy for test:", accuracy2)
                return accuracy1, accuracy2
            else:
                prediction = pred.eval({X: test_input})
                print(prediction[0][1])
                print(prediction[0][0])
                if prediction[0][1]>prediction[0][0]:
                #if prediction[0][1]>0.78:
                    print('Genuine Image')
                    strdemo = 'Genuine Image'
                    return strdemo
                    #return True
                else:
                    print('Forged Image')
                    strdemo = 'ForgedImage'
                    return strdemo
                    #return False
                

    

    #trainAndTest()
    result = evaluate(train_path, test_path, type2=True)
    lblResult = Label(topFrame, text=result)
    lblResult.place(x=120,y=460,anchor=CENTER)
    #root.update()



n_input = 9

root = tkinter.Tk() 
root.geometry("500x500")
topFrame= Frame(root,bg='#03f8fc')
topFrame.pack(fill="both", expand=True)
train_person_id ="global"
def color_entry_label():
    global train_person_id
    global test_image_path
    new_str = select_image()[37:]
    nw=new_str[:-4]
    train_person_id =nw        #entry_number.get()
    #test_image_path= entry_path.get()
    test_image_path=display_image()    
    print(train_person_id)
    print(test_image_path)    
    demofunc(train_person_id,test_image_path)

def load_img(g,a,b):
    img1 = Image.open(g)
    img1 = img1.resize((250, 250), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    panel1 = Label(topFrame, image=img1)
    panel1.image = img1
    #panel.pack()
    panel1.place(x=a,y=b)


def select_image():
    global g
    g = tkinter.filedialog.askopenfilename(
        parent=root, initialdir='DataSet\\real',
        title='Choose file',
        filetypes=[('png images', '.png'),
                   ('gif images', '.gif')]
        )
    print(g)
    load_img(g,50,10)
    return g

def display_image():
    global f
    f = tkinter.filedialog.askopenfilename(
        parent=root, initialdir='DataSet\\forged',
        title='Choose file',
        filetypes=[('png images', '.png'),
                   ('gif images', '.gif')]
        )
    print(f)
    load_img(f,400,10)
    return f

ok_button = tkinter.Button(topFrame, text="OK", command=color_entry_label)

ok_button.pack(side=BOTTOM)    

root.mainloop()


   