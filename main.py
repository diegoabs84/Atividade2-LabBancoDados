
import psycopg2
from faker import Faker

#config
host = 'localhost'
dbname = 'folhadb'
user = 'postgres'
password = 'admin'
sslmode = 'require'

#string de conexão
conn_string = 'host={0} user = {1} dbname={2} password={3} sslmode={4}'.format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Conexão estabelecida!")

#criando um cursor para interagir com o banco
cur = conn.cursor()

#Inserindo dados na tabela
inserir_carreiras = """INSERT INTO folha.carreiras 
                        (cod_carreira, dsc_carreira) 
                        VALUES  
                        (2, 'Analista'),
                        (3, 'Professor'),
                        (4, 'Médico')
                        """
inserir_cargos = """INSERT INTO folha.cargos
                    (cod_cargo, dsc_cargo, cod_carreira)
                    VALUES
                    (1, 'Técnico administrativo', 1),
                    (2, 'Analista administrativo', 2),
                    (3, 'Professor adjunto', 3),
                    (4, 'Médico do trabalho', 4)
                    """
inserir_grupos = """INSERT INTO folha.grupos_rubricas
                    (cod_grupo, dsc_grupo)
                    VALUES
                    (1, 'técnicos'),
                    (2, 'analistas'),
                    (3, 'professores'),
                    (4, 'médicos')
                    """
inserir_rubricas = """INSERT INTO folha.rubricas
                    (cod_rubrica, dsc_rubrica, tpo_rubrica, cod_grupo)
                    VALUES
                    (1, 'total', 'P', 1),
                    (2, 'total', 'D', 1),
                    (3, 'total', 'P', 2),
                    (4, 'total', 'D', 2),
                    (5, 'total', 'P', 3),
                    (6, 'total', 'D', 3),
                    (7, 'total', 'P', 4),
                    (8, 'total', 'D', 4)
                    """
#executando a query
cur.execute(inserir_carreiras)
cur.execute(inserir_cargos)
cur.execute(inserir_grupos)
cur.execute(inserir_rubricas)


inserir_evolucoes_funcionais = """INSERT INTO folha.evolucoes_funcionais
                                  VALUES
                                 (3837, DATE '2017-12-17', 1, 1),
                                 (3471, DATE '2018-01-17', 2, 1),
                                 (3544, DATE '2018-02-17', 3, 2),
                                 (3767, DATE '2018-03-17', 4, 3),
                                 (3840, DATE '2018-04-17', 5, 4),
                                 (3769, DATE '2018-05-17', 6, 1),
                                 (2741, DATE '2018-06-17', 7, 1),
                                 (2614, DATE '2018-07-17', 8, 2),
                                 (2633, DATE '2018-08-17', 9, 3),
                                 (2635, DATE '2018-09-17', 10, 4),
                                 (2658, DATE '2018-10-17', 11, 1),
                                 (2670, DATE '2018-11-17', 12, 1),
                                 (2774, DATE '2018-12-17', 13, 2),
                                 (2834, DATE '2019-01-17', 14, 3),
                                 (2783, DATE '2019-02-17', 15, 4),
                                 (2784, DATE '2019-03-17', 16, 1),
                                 (2805, DATE '2019-04-17', 17, 1),
                                 (2827, DATE '2019-05-17', 18, 2),
                                 (2891, DATE '2019-06-17', 19, 3),
                                 (2893, DATE '2019-07-17', 20, 4),
                                 (2899, DATE '2019-08-17', 21, 1),
                                 (2908, DATE '2019-09-17', 22, 1),
                                 (2932, DATE '2019-10-17', 23, 2),
                                 (2933, DATE '2019-11-17', 24, 3),
                                 (2934, DATE '2019-12-17', 25, 4),
                                 (2935, DATE '2020-01-17', 25, 1),
                                 (2938, DATE '2020-02-17', 27, 1),
                                 (2939, DATE '2020-03-17', 28, 2),
                                 (2941, DATE '2020-04-17', 29, 3),
                                 (2952, DATE '2020-05-17', 29, 4),
                                 (2954, DATE '2020-06-17', 31, 1),
                                 (2958, DATE '2020-07-17', 32, 1),
                                 (2916, DATE '2020-08-17', 33, 2),
                                 (5867, DATE '2020-09-17', 34, 3),
                                 (5870, DATE '2020-10-17', 35, 4),
                                 (6078, DATE '2020-11-17', 36, 1),
                                 (6081, DATE '2020-12-17', 37, 1),
                                 (6139, DATE '2021-01-17', 37, 2),
                                 (6141, DATE '2021-02-17', 35, 3),
                                 (6188, DATE '2021-03-17', 40, 4)
                                 """

cur.execute(inserir_evolucoes_funcionais)

inserir_folha = """INSERT INTO folha.folhas_pagamentos
                                  VALUES
                                  (2017, 12, 'R', 'completa'),
                                  (2018, 01, 'R', 'completa'),
                                  (2018, 02, 'R', 'completa'),
                                  (2018, 03, 'R', 'completa'),
                                  (2018, 04, 'R', 'completa'),
                                  (2018, 05, 'R', 'completa'),
                                  (2018, 06, 'R', 'completa'),
                                  (2018, 07, 'R', 'completa'),
                                  (2018, 08, 'R', 'completa'),
                                  (2018, 09, 'R', 'completa'),
                                  (2018, 10, 'R', 'completa'),
                                  (2018, 11, 'R', 'completa'),
                                  (2018, 12, 'R', 'completa'),
                                  (2018, 12, 'C', 'completa'),
                                  (2019, 01, 'R', 'completa'),
                                  (2019, 02, 'R', 'completa'),
                                  (2019, 03, 'R', 'completa'),
                                  (2019, 04, 'R', 'completa'),
                                  (2019, 05, 'R', 'completa'),
                                  (2019, 06, 'R', 'completa'),
                                  (2019, 07, 'R', 'completa'),
                                  (2019, 08, 'R', 'completa'),
                                  (2019, 09, 'R', 'completa'),
                                  (2019, 10, 'R', 'completa'),
                                  (2019, 11, 'R', 'completa'),
                                  (2019, 12, 'R', 'completa'),
                                  (2019, 12, 'C', 'completa'),
                                  (2020, 01, 'R', 'completa'),
                                  (2020, 02, 'R', 'completa'),
                                  (2020, 03, 'R', 'completa'),
                                  (2020, 04, 'R', 'completa'),
                                  (2020, 05, 'R', 'completa'),
                                  (2020, 06, 'R', 'completa'),
                                  (2020, 07, 'R', 'completa'),
                                  (2020, 08, 'R', 'completa'),
                                  (2020, 09, 'R', 'completa'),
                                  (2020, 10, 'R', 'completa'),
                                  (2020, 11, 'R', 'completa'),
                                  (2020, 12, 'R', 'completa'),
                                  (2020, 12, 'C', 'completa'),
                                  (2021, 01, 'R', 'completa'),
                                  (2021, 02, 'R', 'completa'),
                                  (2021, 03, 'R', 'completa')
                                  """

cur.execute(inserir_folha)

inserir_lancamentos = """INSERT INTO folha.lancamentos
                                  VALUES
                                  (2017, 12, 'R', 1, 3837, DATE '2017-12-17', 1000.00),
                                  (2017, 12, 'R', 2, 3471, DATE '2017-12-17', 1100.00),
                                  (2017, 12, 'R', 3, 3544, DATE '2017-12-17', 1200.00),
                                  (2018, 01, 'R', 4, 3767, DATE '2017-12-17', 1300.00),
                                  (2018, 02, 'R', 1, 2741, DATE '2017-12-17', 1400.00),
                                  (2018, 03, 'R', 2, 2893, DATE '2017-12-17', 1500.00),
                                  (2018, 04, 'R', 3, 2941, DATE '2017-12-17', 1600.00),
                                  (2018, 05, 'R', 4, 5867, DATE '2017-12-17', 1700.00),
                                  (2018, 06, 'R', 1, 6139, DATE '2017-12-17', 1800.00),
                                  (2018, 07, 'R', 2, 6188, DATE '2017-12-17', 1900.00),
                                  (2018, 08, 'R', 3, 6081, DATE '2017-12-17', 2000.00),
                                  (2018, 09, 'R', 4, 2934, DATE '2017-12-17', 2100.00),
                                  (2018, 10, 'R', 1, 2958, DATE '2017-12-17', 2200.00),
                                  (2018, 11, 'R', 2, 2916, DATE '2017-12-17', 2300.00),
                                  (2018, 12, 'R', 3, 2774, DATE '2017-12-17', 2400.00),
                                  (2018, 12, 'C', 1, 2932, DATE '2017-12-17', 2500.00),
                                  (2019, 01, 'R', 1, 3837, DATE '2017-12-17', 2600.00)
                                  """

cur.execute(inserir_lancamentos)

####-----------------------####

#Extração de dados e preenchimento do banco dimensional


extraindo_dados_e_preenchendo_dw_cargos = "INSERT INTO folhadw.dm_cargos SELECT f.cod_cargo , f.dsc_cargo, c.dsc_carreira from folha.cargos f join folha.carreiras c on f.cod_carreira = c.cod_carreira"
cur.execute(extraindo_dados_e_preenchendo_dw_cargos)

extraindo_dados_e_preenchendo_dm_rubricas = "INSERT INTO folhadw.dm_rubricas SELECT r.cod_rubrica, g.dsc_grupo, r.dsc_rubrica, r.tpo_rubrica  from folha.rubricas r join folha.grupos_rubricas g on r.cod_grupo = g.cod_grupo"
cur.execute(extraindo_dados_e_preenchendo_dm_rubricas)

extraindo_dados_e_preenchendo_dm_setores = "INSERT INTO folhadw.dm_setores SELECT s.cod_setor, u.dsc_und, u.cid_und, u.uf_und, s.dsc_setor from folha.setores s join folha.unidades u on s.cod_und = u.cod_und"
cur.execute(extraindo_dados_e_preenchendo_dm_setores)

preenchendo_dados_dm_faixas_etarias = """INSERT INTO folhadw.dm_faixas_etarias
                                         VALUES
                                         (1, 'primeira', 18, 21),
                                         (2, 'segunda', 22, 30),
                                         (3, 'terceira', 31, 45),
                                         (4, 'quarta', 46, 80)"""
cur.execute(preenchendo_dados_dm_faixas_etarias)

extraindo_dados_e_preenchendo_dm_tempos_folhas = "INSERT INTO folhadw.dm_tempos_folhas (ano, mes) SELECT ano, mes FROM folha.folhas_pagamentos"
cur.execute(extraindo_dados_e_preenchendo_dm_tempos_folhas)







#commit
conn.commit()

#fechando o cursor
cur.close()

#fechando a conexão com o banco
conn.close()

