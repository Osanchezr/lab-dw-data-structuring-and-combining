import pandas as pd

def load_data(url):
    """Load data from a CSV file."""
    df = pd.read_csv(url)
    return df

def clean_column_names(df, rename_map=None):
    """Clean column names by making them lowercase and replacing spaces with underscores."""
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    if rename_map:
        df.rename(columns=rename_map, inplace=True)
    return df

def clean_clv(df, mapping_clv):
    """Clean specific columns by replacing patterns specified in mapping_clv."""
    for column, replacements in mapping_clv.items():
        for old, new in replacements.items():
            df[column] = df[column].str.replace(old, new, regex=False)
    return df
        
def clean_invalid_values(df, mappings):
    """Replace invalid values in specific columns using provided mappings."""
    for column, mapping in mappings.items():
        df[column] = df[column].replace(mapping, regex=False)
    return df

def format_data_types(df, conversions):
    """Convert columns to appropriate data types using provided conversion rules."""
    for column, tipe in conversions.items():
        if tipe == 'split':
            # Assuming 'split' indicates a specific transformation needed
            df[column] = df[column].str.split("/").str[1]
            df[column] = df[column].astype(float)
        else:
            df[column] = df[column].astype(tipe)
    return df

def deal_with_null_values(df, fill_values):
    """Handle missing values using provided fill values."""
    df = df.dropna(how="all")
    for column, value in fill_values.items():
        if value == 'mean':
            # Usar .loc[] para asignar valores
            df.loc[:, column] = df[column].fillna(df[column].mean())
        else:
            # Usar .loc[] para asignar valores
            df.loc[:, column] = df[column].fillna(value)
    return df

def remove_duplicates(df):
    """Remove duplicate rows and reset the index."""
    df = df.drop_duplicates()
    df.reset_index(drop=True, inplace=True)
    return df

# Función principal que llama a todas las funciones de limpieza
def main(url, rename_map=None, mapping_clv=None, mappings=None, conversions=None, fill_values=None):
    """Main function to perform all the data cleaning steps."""
    df = load_data(url)
    df = clean_column_names(df, rename_map)
    df = clean_clv(df, mapping_clv)
    df = clean_invalid_values(df, mappings)
    df = format_data_types(df, conversions)
    df = deal_with_null_values(df, fill_values)
    df = remove_duplicates(df)
    return df

    
 