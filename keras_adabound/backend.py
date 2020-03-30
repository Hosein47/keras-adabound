import os
os.environ['TF_KERAS']='1'

__all__ = [
    'keras', 'utils', 'activations', 'applications', 'backend', 'datasets', 'engine',
    'layers', 'preprocessing', 'wrappers', 'callbacks', 'constraints', 'initializers',
    'metrics', 'models', 'losses', 'optimizers', 'regularizers',
]

from tensorflow.python import keras
from tensorflow.python.keras import utils
from tensorflow.python.keras import activations
from tensorflow.python.keras import applications
from tensorflow.python.keras import backend
from tensorflow.python.keras import datasets
from tensorflow.python.keras import engine
from tensorflow.python.keras import layers
from tensorflow.python.keras import preprocessing
from tensorflow.python.keras import wrappers
from tensorflow.python.keras import callbacks
from tensorflow.python.keras import constraints
from tensorflow.python.keras import initializers
from tensorflow.python.keras import metrics
from tensorflow.python.keras import models
from tensorflow.python.keras import losses
from tensorflow.keras import optimizers
from tensorflow.python.keras import regularizers
