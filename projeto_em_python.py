import sqlite3 
import pandas as pd
conx = sqlite3.connect('loja.db')

cod_prod = input("Digite o código do Produto: ")
produto_df = pd.read_sql_query(f'SELECT sku, preco FROM produto WHERE sku = ({cod_prod})', conx)

cod_clie = input("Digite o código do cliente: ")
cliente_df = pd.read_sql_query(f'SELECT codigo, nome_razao_social, condicao FROM cliente WHERE codigo = ({cod_clie})', conx)

#inserindo as colulas da tabela produto na tabela cliente com novos nomes.
cliente_df.insert(2, 'cod_produto', produto_df['sku'])
cliente_df.insert(3, 'preco_produto', produto_df['preco'])

    
for condicao in cliente_df['condicao']:
  if condicao < 7: cliente_df['preco_condicao_1'] = produto_df['preco'] 
  else: cliente_df['preco_condicao_1'] =(produto_df['preco'] * 0.1)

  if condicao >= 14: cliente_df['preco_condicao_2'] = (produto_df['preco'] * 0.15)
  else: cliente_df['preco_condicao_2'] = 'Não há condição'

  if condicao >= 21: cliente_df['preco_condicao_3'] = (produto_df['preco'] * 0.2)
  else: cliente_df['preco_condicao_3'] = 'Não há condição'

  if condicao == 28: cliente_df['preco_condicao_4'] = (produto_df['preco'] * 0.25)
  else: cliente_df['preco_condicao_4'] = 'Não há condição'

  

display(cliente_df)
