import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

# *****************************************************************************************************

cols = ['parcel_id', 'bed_rooms', 'bath_rooms', 'finished_sqft', 'year_built', 'county', 'log_error']

def plot_variable_pair(df, cols= cols):
    for i in cols:
        sns.lmplot(x=i, y="tax_value", data=df, line_kws={'color': 'red'})
        plt.show()


# *****************************************************************************************************

def scale_data(train, 
               validate, 
               test, 
               columns_to_scale=['bed_rooms', 'bath_rooms', 'finished_sqft'],
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
    scaler = StandardScaler()
    #     fit the thing
    scaler.fit(train[columns_to_scale])
    # applying the scaler:
    train_scaled[columns_to_scale] = pd.DataFrame(scaler.transform(train[columns_to_scale]),
                                                  columns=train[columns_to_scale].columns.values).set_index([train.index.values])
                                                  
    validate_scaled[columns_to_scale] = pd.DataFrame(scaler.transform(validate[columns_to_scale]),
                                                  columns=validate[columns_to_scale].columns.values).set_index([validate.index.values])
    
    test_scaled[columns_to_scale] = pd.DataFrame(scaler.transform(test[columns_to_scale]),
                                                 columns=test[columns_to_scale].columns.values).set_index([test.index.values])
    
    if return_scaler:
        return scaler, train_scaled, validate_scaled, test_scaled
    else:
        return train_scaled, validate_scaled, test_scaled