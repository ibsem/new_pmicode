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


def add_setor(self, json):

    setor = json['setor']
    idsetor = json['id_setor']

    try:
        connection = Connection().get_connection()
        cursor = connection.cursor()
        insert = """insert into setor (setor, idsetor) values ('{0}', {1});""".format(
            setor, idsetor)
        cursor.execute(insert)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error", error)
    finally:
        if connection:
            cursor.close()
            connection.close()

def remove_setor(self, json):
    idsetor = json['id_setor']

    try:
        connection = Connection().get_connection()
        cursor = connection.cursor()
        deleta = "delete from setor where id={0}".format(idsetor)
        cursor.execute(deleta)
        connection.commit()
        self.listar()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error", error)

    finally:
        if connection:
            cursor.close()
            connection.close()


def list_todos_chamados_ti(self):
    try:
        connection = Connection().get_connection()
        cursor = connection.cursor()
        select = "select * from chamadoti"
        cursor.execute(select)
        chamado = cursor.fetchall()

        for row in chamado:
            print("Id = ", row[0], )
            print("tipo_chamado = ", row[1])
            print("prioridade  = ", row[2])
            print("data_criacao = ", row[3] )
            print("info_criador  = ", row[4])
            print("info_func  = ", row[5])
            print("info_chamado  = ", row[6])
            print("status  = ", row[7], "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()

def save_usuario(self, json):
    nome = json['nome']
    email = json['email']
    login = json['login']
    senha = json['senha']
    id_setor = json['id_setor']
    nivel_permissao = json['nivel_permissao']

    try:
        connection = Connection().get_connection()
        cursor = connection.cursor()
        insert = """insert into usuario (nome, email, login, senha, idsetor, nivelpermissao) values ('{0}', '{1}', '{2}', 
        '{3}', {4}, {5});""".format(nome, email, login, senha, id_setor, nivel_permissao)
        cursor.execute(insert)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error", error)
    finally:
        if connection:
            cursor.close()
            connection.close()

def consultar_usu(self, json):
    login = json['login']

    try:
        connection = Connection().get_connection()
        cursor = connection.cursor()
        select = "select * from usuario where login = {0}".format(login)
        cursor.execute(select)
        chamado = cursor.fetchall()

        for row in chamado:
            nome = row[0]
            email = row[1]
            login = row[2]
            idsetor = row[4]
            nivelpermissao = row[5]

        json_volta = {

            'nome': nome,
            'emial': email,
            'login': login,
            'idsetor': idsetor,
            'nivelpermissao': nivelpermissao,
        }

    except (Exception, psycopg2.Error) as error:
        print("Error", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()






