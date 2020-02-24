import urlmarker as um

# Call with dataframe column
def regularize_urls(df_col):
    return df_col.str.replace(um.WEB_URL_REGEX, ' _url_ ')

def regularize_numbers(df_col):
    return df_col.str.replace('\d+', ' _num_ ')