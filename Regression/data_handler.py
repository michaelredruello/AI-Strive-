import pandas as pd
import numpy as np
import torch
from sklearn.model_selection import train_test_split

def load_data(pth, batch_size, shuffle = True):
    
    data = pd.read_csv(pth)
    
    data.drop(['date'], axis = 1, inplace = True)
    
    y = data['DAX'].values
    x = data.drop(['DAX'], axis = 1).values
    
    x, y = to_batches(x, y, batch_size)
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.1, random_state=0)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    x_train = torch.tensor(x_train.as_type(np.float32)).to(device)
    x_test = torch.tensor(x_test.as_type(np.float32)).to(device)
    
    y_train = torch.tensor(y_train.as_type(np.float32)).to(device)
    y_test = torch.tensor(y_test.as_type(np.float32)).to(device)
    
def to_batches(x, y, batch_size):
    n_batches = x.shape[0] // batch_size
    
    indexes = np.random.permutation(x.shape[0])
    
    x = x[indexes]
    y = y[indexes]
    
    x = x[:batch_size * n_batches].reshape(n_batches, batch_size, x.shape[1])
    y = y[:batch_size * n_batches].reshape(n_batches, batch_size, 1)
    
    return x, y

x_train, x_test, y_train, y_test = load_data("data")
    
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

