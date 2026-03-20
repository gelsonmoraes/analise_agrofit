import unicodedata

def fix_encoding(text):
    try:
        return text.encode('latin1').decode('utf-8')
    except:
        return text

def normalize_text(text):
    if isinstance(text, str):
        text = fix_encoding(text)
        text = unicodedata.normalize('NFKD', text)
        return text.strip()
    return text

def clean_dataframe(df):
    for col in df.columns:
        df[col] = df[col].apply(normalize_text)
    return df

def standardize_columns(df):
    df = df.copy()
    
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    
    return df