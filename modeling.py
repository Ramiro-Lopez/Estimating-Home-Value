from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, QuantileTransformer # now that our data is split we can scale it
import pandas as pd

mms = MinMaxScaler() # creeating the scaler 
ss = StandardScaler() # creating the scaler
rs = RobustScaler() # creating the scaler 
qt = QuantileTransformer() # creating the scaler

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# *****************************************************************************************************

def scale_train_data(train, 
               validate, 
               test, 
               cols_to_scale,
               scale,
               return_scaler=False):
    '''
    Scales the 3 data splits. 
    Takes in train, validate, and test data splits and returns their scaled counterparts.
    If return_scalar is True, the scaler object will be returned as well
    '''
    # make copies of our original data so we dont gronk up anything
    train_scaled = train.copy()
    validate_scaled = validate.copy()
    test_scaled = test.copy()
    #     make the thing
    scaler = scale
    #     fit the thing
    scaler.fit(train[cols_to_scale])
    # applying the scaler:
    train_scaled[cols_to_scale] = pd.DataFrame(scaler.transform(train[cols_to_scale]),
                                                  columns=train[cols_to_scale].columns.values).set_index([train.index.values])
                                                  
    validate_scaled[cols_to_scale] = pd.DataFrame(scaler.transform(validate[cols_to_scale]),
                                                  columns=validate[cols_to_scale].columns.values).set_index([validate.index.values])
    
    test_scaled[cols_to_scale] = pd.DataFrame(scaler.transform(test[cols_to_scale]),
                                                 columns=test[cols_to_scale].columns.values).set_index([test.index.values])
    
    if return_scaler:
        return scaler, train_scaled, validate_scaled, test_scaled
    else:
        return train_scaled, validate_scaled, test_scaled

# *****************************************************************************************************

def split_X(df):
    '''takes in the train data frame and splits it into y train, y validate, y test'''
    X_train = df.drop(columns=['tax_value', 'propertylandusedesc', 'parcel_id', 'tax_amount', 'log_error', 'transaction_date', 'county'])
    X_validate = df.drop(columns=['tax_value', 'propertylandusedesc', 'parcel_id', 'tax_amount', 'log_error', 'transaction_date', 'county'])
    X_test = df.drop(columns=['tax_value', 'propertylandusedesc', 'parcel_id', 'tax_amount', 'log_error', 'transaction_date', 'county'])
    return X_train, X_validate, X_test

# *****************************************************************************************************

def split_y(df):
    '''takes in the train data frame and splits it into X train, X, validate, X test'''
    y_train = df.tax_value
    y_validate = df.tax_value
    y_test = df.tax_value
    return y_train, y_validate, y_test

# *****************************************************************************************************

def metrics_reg(y, yhat):
    """
    send in y_true, y_pred & returns RMSE, R2
    """
    rmse = mean_squared_error(y, yhat, squared=False)
    r2 = r2_score(y, yhat)
    return rmse, r2

