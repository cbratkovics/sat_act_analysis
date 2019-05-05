# Function to print out properties of each DataFrame:
def print_props(df_list, prop = '.head()'):
    
    for df in df_list:
        if (prop == '.head()'):
            title = '\tFirst 5 rows of '
            data = df.head()
            
        elif (prop == '.tail()'):
            title = '\tLast 5 rows in '
            data = df.tail()
            
        elif (prop == '.columns'):
            title = '\tColumn Features of '
            data = df.columns
            
        elif (prop == '.dtypes'):
            title = '\tData Types of '
            data = df.dtypes
            
        elif (prop == '.shape'):
            title = '\tShape of '
            data = df.shape
            
        elif (prop == '.isnull().sum()'):
            title = '\tNull Values in '
            data = df.isnull().sum()
            
        elif (prop == '.describe()'):
            title = '\tSummary Statistics of '
            data = df.describe()
        
        print(title + df.name)
        print('----------------------------------------')
        print(data)
        print()
        

def compare_values(act_col, sat_col):
    act_vals = []
    sat_vals = []
    
    for a_val in act_col:
        act_vals.append(a_val)
    for s_val in sat_col:
        sat_vals.append(s_val)
    
    print('Values in ACT only: ')
    for val_a in act_vals:
        if (val_a not in sat_vals):
            print(val_a)
            
    print('----------------------------')
        
    print('Values in SAT only: ')
    for val_s in sat_vals:
        if (val_s not in act_vals):
            print(val_s)

    
def fix_participation(column):
    return column.apply(lambda cells: cells.strip('%'))
    
def convert_to_float(df):
    features = [col for col in df.columns if col != 'State']
    df[features] = df[features].astype(float)
    return df
    
    
    
    