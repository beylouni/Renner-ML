import pandas as pd 
import numpy as np 

#pipeline de pré-processamento
def sales_pipeline_v1(dataframe):
    """
        Args:
            dataframe: Pandas dataframe com os dados de vendas
        Return:
            df_web: dataframe com os dados necessários para previsão das lojas web
            df_fisica: dataframe com os dados necessários para previsão das lojas fisicas
        OBS:
            Para previsão de séries temporais, após chamar o metodo e receber os novos dataframes, é preciso transformar
            a coluna 'data_semana_comercial' em datetime novamente e coloca-lá como index do df.
        OBS2:
            Se precisar usar os dias da semana, mes ou ano, basta usar os atributos do index após transformá-lo
    """
    df_pipe = dataframe.copy()
    print('Dataframe carregado!')

    #Dropando colunas desnecessárias
    df_pipe.drop(['item', 'semana_comercial'], axis=1, inplace=True)
    print("Colunas 'item' e 'semana_comercial' dropadas!")

    #Dropando linhas com vendas Guide Shop ('GS')
    df_pipe = df_pipe.loc[df_pipe['clima'] != 'GS']
    print('Vendas Guide Shop (GS) dropadas!')

    #Alterando vendas negativas para zero
    df_pipe.loc[df_pipe.venda < 0, 'venda'] = 0
    print('Vendas negativas alteradas para zero!')

    #Transformando variaveis categóricas em variaveis numéricas
    df_pipe['localidade'] = df_pipe['localidade'].map({ 'br':2, 'uy':1, 'ar':0 })
    df_pipe['loja_tamanho'] = df_pipe['loja_tamanho'].map({ 'PP':0, 'P':1, 'M':2, 'G':3, 'GG':4 })
    df_pipe['clima'] = df_pipe['clima'].map({ 'SPO':5, 'RIO':4, 'NOR':3, 'SUL':2 ,'URU':1 ,'ARG': 0, 'W':'W'})
    print('Variaveis categoricas transformadas em numéricas!')

    #Transformando a coluna 'data_semana_comercial' em datetime
    df_pipe.data_semana_comercial = pd.to_datetime(df_pipe.data_semana_comercial)
    print("coluna 'data_semana_comercial' transformada em datetime!")

    #Tratando dataset para lojas web
    df_web = df_pipe[df_pipe['categoria_loja'] == 'web']
    del df_web['categoria_loja']
    del df_web['clima']
    del df_web['localidade']
    del df_web['loja_tamanho']
    print('Dataset de treino para lojas web criado')
    

    #Tratando dataset para lojas web
    df_fisica = df_pipe[df_pipe['categoria_loja'] == 'fisica']
    del df_fisica['categoria_loja']
    print('Dataset de treino para lojas fisicas criado')
    
    #Criando csv's com os dados tratados e separados
    df_web.to_csv('../input/clean_data/renner_web_treino.csv', index=False)
    df_fisica.to_csv('../input/clean_data/renner_fisica_treino.csv', index=False)
    print('CSVs criados e salvos na pasta input/clean_data')
    return df_web, df_fisica