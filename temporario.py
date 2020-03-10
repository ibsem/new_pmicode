def salvar(self, nome, sobrenome, curso):
    try:
        connection = Connection().get_connection()
        cursor = connection.cursor()
        insert = """insert into chamadoti (nome, sobrenome, curso) values ('{0}', '{1}','{2}');""".format(nome,
                                                                                                          sobrenome,
                                                                                                          curso)
        cursor.execute(insert)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error", error)
    finally:
        if connection:
            cursor.close()
            connection.close()



def save_chamado_ti(json):

    tipo_chamado = json['tipo_chamado']
    prioridade = json['prioridade']
    data_criacao = json['data_criacao']
    info_criador = json['info_criador']
    info_func = json['info_func']
    info_chamado = json['info_chamado']
    status = json['status']
 try:
        connection = Connection().get_connection()
        cursor = connection.cursor()
        insert = """insert into chamadoti (tipo_chamado, prioridade, data_criacao, info_criador, 
        info_func, info_chamado, status) values ('{0}', {1}, {2}, '{3}', '{4}', '{5}', '{6}');""".format(tipo_chamado,prioridade, data_criacao,info_criador,
                                                                                                         info_func, info_chamado, status )
        cursor.execute(insert)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error", error)
    finally:
        if connection:
            cursor.close()
            connection.close()


  def save_chamado_pape(self,json):
    q_caneta = json['q_caneta']
    q_lapis = json['q_lapis']
    q_resma = json['q_resma']
    q_cola = json['q_cola']
    prioridade = ['prioridade']
    data_criacao = json['data_criacao']
    info_criador = json['info_criador']
    info_func = json['info_func']
    info_chamado = json['info_chamado']
    status = json['status']


    connection = Connection().get_connection()
    cursor = connection.cursor()
    insert = """insert into chamadoti (q_caneta, q_lapis, q_resma, q_cola, 
            prioridade, data_criacao, info_criador, info_func, info_chamado, status ) values ('{0}', {1}, {2}, '{3}', 
            '{4}', '{5}', '{6}', '{7}', '{8}');""".format(q_caneta, q_lapis, q_resma, q_cola,
        prioridade, data_criacao, info_criador, info_func,
        info_chamado, status)
    cursor.execute(insert)
    connection.commit()

except (Exception, psycopg2.DatabaseError) as error:
print("Error", error)
finally:
if connection:
    cursor.close()
    connection.close()


  def save_cadastro_usu(self, json):
     nome = json['nome']
     email = json['email']
     login = json['login']
     senha = json['senha']
     try:
         connection = Connection().get_connection()
         cursor = connection.cursor()
         insert = """insert into cadastrousuario (nome, email, login, senha) values ('{0}', '{1}', {2}, {3});""".format(
             nome, email, login, senha)
         cursor.execute(insert)
         connection.commit()
     except (Exception, psycopg2.DatabaseError) as error:
         print("Error", error)
     finally:
         if connection:
             cursor.close()
             connection.close()


def save_cadastro_func(self, json):

    nome = json['nome']
    email = json['email']
    login = json['login']
    senha = json['senha']

    try:
        connection = Connection().get_connection()
        cursor = connection.cursor()
        insert = """insert into cadastrofuncionario (nome, email, login, senha) values ('{0}', '{1}', {2}, {3});""".format(
            nome, email, login, senha)
        cursor.execute(insert)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error", error)
    finally:
        if connection:
            cursor.close()
            connection.close()

def val_cadastro_gest(self, json):

    login = json['login']
    senha = joson['senha']



def valida_login(self, json):

    login = json['login']
    senha = json['senha']

def v_meuchamdo_cria(self, json):

    info_criador = json['info_criador']

def v_meuchamdo_func(self, json):

    info_func = json['info_func']


