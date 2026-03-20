import pandas as pd

def load_csv(path):
    """
    Carrega CSV tratando possíveis problemas de encoding e separador.
    """
    try:
        df = pd.read_csv(path, sep=';', encoding='utf-8', low_memory=False)
    except UnicodeDecodeError:
        df = pd.read_csv(path, sep=';', encoding='latin1', low_memory=False)
    
    return df