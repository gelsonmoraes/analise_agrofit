from src.ingestao import load_csv
from src.limpeza import clean_dataframe, standardize_columns
from src.transformacao import (
    explode_praga_nome_comum,
    create_dim_praga,
    create_dim_praga_nome_comum,
    create_bridge_produto_praga,
    explode_multivalue_column,
    create_dimension,
    create_bridge,
    create_fato_produto
)


def main():
    print("Iniciando pipeline...")

    path = "data/raw/agrofitprodutosformulados.csv"
    
    # 1. INGESTÃO
    
    df = load_csv(path)
    print("Dados carregados!")

    df = standardize_columns(df)

    
    # 2. LIMPEZA
    
    df = clean_dataframe(df)
    print("Dados limpos!")

    
    # 3. PRAGAS (ESPECÍFICO)
    
    df_pragas = explode_praga_nome_comum(df)
    print("Pragas normalizadas!")

    df_dim_praga = create_dim_praga(df_pragas)
    df_dim_praga_nome = create_dim_praga_nome_comum(df_pragas, df_dim_praga)

    bridge_produto_praga = create_bridge_produto_praga(df_pragas, df_dim_praga)

    # 4. INGREDIENTE ATIVO
    
    df_ing = explode_multivalue_column(df, 'ingrediente_ativo')

    dim_ingrediente = create_dimension(df_ing, 'ingrediente_ativo', 'id_ingrediente')

    bridge_produto_ingrediente = create_bridge(
        df_ing,
        dim_ingrediente,
        'ingrediente_ativo',
        'id_ingrediente'
    )

    
    # 5. CULTURA
    
    df_cultura = explode_multivalue_column(df, 'cultura')

    dim_cultura = create_dimension(df_cultura, 'cultura', 'id_cultura')

    bridge_produto_cultura = create_bridge(
        df_cultura,
        dim_cultura,
        'cultura',
        'id_cultura'
    )

    
    # 6. EMPRESA
    
    dim_empresa = create_dimension(df, 'titular_de_registro', 'id_empresa')

    
    # 7. FATO
    
    fato_produto = create_fato_produto(df, dim_empresa)

    print("Tabela fato criada!")

    
    # 8. EXPORTAÇÃO
    
    print("Salvando arquivos...")

    fato_produto.to_csv("data/processed/fato_produto.csv", index=False)

    df_dim_praga.to_csv("data/processed/dim_praga.csv", index=False)
    df_dim_praga_nome.to_csv("data/processed/dim_praga_nome.csv", index=False)

    dim_ingrediente.to_csv("data/processed/dim_ingrediente.csv", index=False)
    dim_cultura.to_csv("data/processed/dim_cultura.csv", index=False)
    dim_empresa.to_csv("data/processed/dim_empresa.csv", index=False)

    bridge_produto_praga.to_csv("data/processed/bridge_produto_praga.csv", index=False)
    bridge_produto_ingrediente.to_csv("data/processed/bridge_produto_ingrediente.csv", index=False)
    bridge_produto_cultura.to_csv("data/processed/bridge_produto_cultura.csv", index=False)

    print("Pipeline finalizado com sucesso!")


if __name__ == "__main__":
    main()