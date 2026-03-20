import pandas as pd
import re

def clean_praga_nome_comum(text):
    if isinstance(text, str):
        # remove (1), (2), etc
        text = re.sub(r"\(\d+\)", "", text)
        return text.strip()
    return text


def explode_praga_nome_comum(df):
    df = df.copy()

    df['praga_nome_comum'] = df['praga_nome_comum'].apply(clean_praga_nome_comum)

    df['praga_nome_comum'] = df['praga_nome_comum'].str.split(';')

    df = df.explode('praga_nome_comum')

    df['praga_nome_comum'] = df['praga_nome_comum'].str.strip()

    return df

def create_dim_praga(df_pragas):
    df_dim = df_pragas[['praga_nome_cientifico']].dropna().drop_duplicates()

    # criar chave surrogate
    df_dim['id_praga'] = range(1, len(df_dim) + 1)

    # GARANTIR TIPO INTEIRO
    df_dim['id_praga'] = df_dim['id_praga'].astype(int)

    # reorganizar colunas
    df_dim = df_dim[['id_praga', 'praga_nome_cientifico']]

    return df_dim

def create_dim_praga_nome_comum(df_pragas, df_dim_praga):
    df = df_pragas.merge(
        df_dim_praga,
        on='praga_nome_cientifico',
        how='left'
    )

    df_nome = df[['id_praga', 'praga_nome_comum']].dropna().drop_duplicates()

    df_nome['id_praga'] = df_nome['id_praga'].astype('Int64')

    df_nome['id_nome'] = range(1, len(df_nome) + 1)

    df_nome = df_nome[['id_nome', 'id_praga', 'praga_nome_comum']]

    return df_nome

def create_bridge_produto_praga(df_pragas, df_dim_praga):
    df = df_pragas.merge(
        df_dim_praga,
        on='praga_nome_cientifico',
        how='left'
    )

    df_bridge = df[['nr_registro', 'id_praga']].drop_duplicates()

    df_bridge['id_praga'] = df_bridge['id_praga'].astype('Int64')

    return df_bridge

def explode_multivalue_column(df, column, sep=';'):
    df = df.copy()

    df[column] = df[column].fillna('')
    df[column] = df[column].astype(str)

    df[column] = df[column].str.split(sep)
    df = df.explode(column)

    df[column] = df[column].str.strip()

    return df

def create_dimension(df, column, id_name):
    df_dim = df[[column]].dropna().drop_duplicates()

    df_dim[id_name] = range(1, len(df_dim) + 1)

    df_dim = df_dim[[id_name, column]]

    return df_dim

def create_bridge(df, df_dim, column, id_name, key='nr_registro'):
    df_merge = df.merge(df_dim, on=column, how='left')

    df_bridge = df_merge[[key, id_name]].drop_duplicates()

    return df_bridge

def create_fato_produto(df, dim_empresa):
    df_fato = df.copy()

    # merge empresa
    df_fato = df_fato.merge(
        dim_empresa,
        on='titular_de_registro',
        how='left'
    )

    # selecionar colunas principais
    df_fato = df_fato[
        [
            'nr_registro',
            'id_empresa',
            'marca_comercial',
            'formulacao',
            'classe',
            'classe_toxicologica',
            'classe_ambiental',
            'situacao'
        ]
    ].drop_duplicates()

    return df_fato