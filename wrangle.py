import env
import os
import pandas as pd
import numpy as np 

from sklearn.model_selection import train_test_split

# Wrangle functions for Zillow Data 

def get_connection(db: str, user: str = env.user, host: str = env.host, password=env.password) -> str: 
    '''
       This function takes in a data base, username, password, and hoast from MySQL
       and returns a my url as a string
    '''
    return f"mysql+pymysql://{user}:{password}@{host}/{db}"

# *****************************************************************************************************

def get_zillow_data(file_name="zillow_all.csv") -> pd.DataFrame: # add to wrangle file 
    if os.path.isfile(file_name):
        return pd.read_csv(file_name)
    query = """select propertylandusedesc, parcelid, bedroomcnt, 
               bathroomcnt, calculatedfinishedsquarefeet, 
               taxvaluedollarcnt, yearbuilt, taxamount, fips, 
               logerror, transactiondate
               from propertylandusetype 
               left join properties_2017
               using (propertylandusetypeid)
               left join predictions_2017
               using(parcelid)
               where propertylandusedesc = 'Single Family Residential';
            """
    connection = get_connection("zillow")
    df = pd.read_sql(query, connection, parse_dates=['transactiondate'])
    df.to_csv(file_name, index=False)
    return df

# *****************************************************************************************************

def prep_zillow(df: pd.DataFrame) -> pd.DataFrame: # add to wrangle file 
    '''
    This function takes in a dataframe
    renames the columns, drops nulls values
    Additionally it changes datatypes for appropriate columns.
    Also drops all values that are 0.
    Then returns a cleaned dataframe
    '''
    df = df.rename(columns={'parcelid': 'parcel_id', 'logerror': 'log_error', 'transactiondate': 'transaction_date', 
                            'bedroomcnt':'bed_rooms', 'bathroomcnt':'bath_rooms', 'calculatedfinishedsquarefeet':'finished_sqft', 
                            'taxvaluedollarcnt':'tax_value', 'fips':'county', 'yearbuilt': 'year_built', 'taxamount': 'tax_amount'})
    
    df = df.dropna()
    
    make_ints = ['bed_rooms','finished_sqft','tax_value','year_built', 'county']

    for col in make_ints:
        df[col] = df[col].astype(int)

    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    df = df.drop(df[df['bed_rooms'] == 0].index)
    df = df.drop(df[df['bath_rooms'] == 0].index)
    df = df.drop(df[df['bath_rooms'] == 13].index)
    df = df.drop(df[df['bath_rooms'] == 8.5].index)
    df = df.drop(df[df['bath_rooms'] == 11].index)
    df = df.drop(df[df['bed_rooms'] == 14].index)
    df = df.drop(df[df['bed_rooms'] == 12].index)
    df = df.drop(df[df['bed_rooms'] == 10].index)
    df = df.drop(df[df['bed_rooms'] == 11].index)
    


        
    return df

# *****************************************************************************************************

def split_data(df: pd.DataFrame) -> pd.DataFrame: 
    '''splits data into train test and validate dataframes'''
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate,
                                       test_size=.3,
                                       random_state=123)
    return train, validate, test

# *****************************************************************************************************

def view_split(train, validate, test):
    ''''''
    print(f'train    -> {train.shape}')
    print(f'validate -> {validate.shape}')
    print(f'test     -> {test.shape}')