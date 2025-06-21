import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import Flask,request,jasonify,render_template


application=Flask(__name__)

app=application

