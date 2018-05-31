import pandas as pd 
import numpy as np 
import tensorflow as tf 
import matplotlib.pyplot as plt
import time 
import json



PDAT = "../../_data_tmp/food/"
PMOD = "../../dmodels/foo"
ifil = "file.csv"


BATCH_SIZE = 1000
USER_NUM = 20052 
ITEM_NUM = 674
DIM = 15
EPOCH_MAX = 100
DEVICE = "/cpu:0"
spn = 5000 #split