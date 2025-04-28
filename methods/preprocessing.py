import pandas as pd

import datetime as dt

import numpy as np

def null_columns_remover(df,threshold: float):


    '''This function is used for removing those columns which have more than 50% null values, but based
    on the dataset we can change the threshold of null value presence for which we will remove the columns
    * here we pass in 2 arguments


        *- df:- this is the dataframe from which we wish to remove the columns

        *- threshold:- what percentage or proportion of values are we ok with having the issues'''
    

    di={}


    null_df_details=df.isnull().mean()


    for index,value in zip(null_df_details.index,null_df_details.values):
        if value>threshold:
            di[index]=value


    return list(di.keys())



def NoVariaton_columns_remover(df, threshold: int):
    """
        Identifies columns in a DataFrame with unique value counts below a specified threshold.
        This function analyzes the number of unique values in each column of the given DataFrame
        and returns a list of column names where the count of unique values is less than the 
        specified threshold.
        Args:


            df (pandas.DataFrame): The input DataFrame to analyze.
            threshold (int): The threshold for the minimum number of unique values a column 
                             must have to not be included in the result.


        Returns:
            list: A list of column names from the DataFrame that have fewer unique values 
                  than the specified threshold.
    """
    
    di={}


    var_df_details=df.nunique()


    for index, value in zip(var_df_details.index,var_df_details.values):
        if value<threshold:
            di[index]=value


    return list(di.keys())


def convert_to_datetime(df):
    """
    We know for a fact that our dataset has a column called `Timestamp` this column has a
    lot of valuable data in the form of Day, Day of the Week, Hour, Month, Year. All of which
    can be useful for making predictions.
    thus in this function:

    Converts the 'Timestamp' column in the given DataFrame to a datetime object and extracts 
    additional features such as day, month, year, hour, and weekday. The original 'Timestamp' 
    column is dropped after the extraction.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing a 'Timestamp' column.

    Returns:
    pd.DataFrame: The modified DataFrame with new columns: 'day', 'month', 'year', 'hour', 
                  and 'weekday', and without the original 'Timestamp' column.

    Notes:
    - The 'Timestamp' column in the input DataFrame must be in a format that can be parsed 
      by pandas' `to_datetime` function.
    - The 'weekday' column represents the day of the week as an integer, where Monday is 0 
      and Sunday is 6.
    """
    
    df['Timestamp']=pd.to_datetime(df['Timestamp'])

    df['day'] = df['Timestamp'].dt.day

    df['month'] = df['Timestamp'].dt.month

    df['year'] = df['Timestamp'].dt.year

    df['hour'] = df['Timestamp'].dt.hour

    df['weekday'] = df['Timestamp'].dt.dayofweek

    df.drop('Timestamp',axis=1,inplace=True)

    return df


def remove_highly_correlated_features(df, threshold=0.8):
    """
    Remove features from the dataframe that have a correlation higher than the threshold.
    This function iteratively checks each column with all others and removes columns with 
    high correlation, ensuring no highly collinear columns remain.

    Parameters:
        df (pd.DataFrame): The input dataframe.
        threshold (float): The correlation threshold (default is 0.8).

    Returns:
        pd.DataFrame: The dataframe with highly correlated features removed.
    """
    # Compute the correlation matrix (absolute value)
    corr_matrix = df.corr().abs()

    # Create a set to hold columns to drop
    to_drop = set()

    # Iterate over each column
    for i in range(len(corr_matrix.columns)):
        for j in range(i + 1, len(corr_matrix.columns)):
            if corr_matrix.iloc[i, j] > threshold:
                col_to_drop = corr_matrix.columns[j]
                if col_to_drop not in to_drop:
                    to_drop.add(col_to_drop)

    # Drop the columns
    df_reduced = df.drop(columns=list(to_drop))

    return df_reduced
