import pandas


def auto_clean(data, missing_threshold = 0.5, important_cols=None, split_dates=True):
    data = data.copy()
    
    if important_cols == None:
        important_cols = []
    
    report = {}
    
    for cols in data.columns:
        missing_ratio = data[cols].isnull().mean()
        unique_values = df[cols].nunique()
        
        # skip important columns
        if cols = important_cols:
            continue
        #drop columns with too many missing values
        if missing_ratio >= missing_threshold:
            data.drop(columns=[cols], implace = True)
        report[cols] = 'Dropped(too many missing values)'
        #drop values with no variation
        elif unique_values <= 1:
            df.drop(columns = [cols], inplace = True)
            
        report[cols] = 'Dropped(no variation)'
        #Fill numeric columns with the mean value
        elif data[cols].dtypes in ['int64','float64']:
            data[cols].fillna(data[cols].mean(), inplace=True)
        else:
            if split_dates:
                try:
                    data[cols] = pandas.to_datetime(data[cols])
                    data[f'{cols}_year'] =  data[cols].dt.year
                    data[f'{cols}_month'] =  data[cols].dt.month
                except:
                    data[cols].fillna(data[cols].mode(), inplace=True)
            else:
                data[cols].fillna(data[cols].mode(), inplace=True)
            
    return data, report
        
        
    
