from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score , balanced_accuracy_score
from sklearn.preprocessing import StandardScaler
import seaborn as sns
from sklearn.metrics import (confusion_matrix , precision_recall_curve , auc,roc_curve) 
from keras.models import Model , load_model
from keras.layers import Input, Dense
from keras.callbacks import ModelCheckpoint , TensorBoard
from keras import regularizers
from sklearn.neural_network import MLPClassifier
# OCSVM model
# def oneclass_svm(dataset , kernel , nu):
# svm = OneClassSVM(kernel=kernel , nu=nu).fit(dataset) return svm
print("SDfsd")