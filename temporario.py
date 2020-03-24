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



def save_chamado_ti(self, json):

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
    insert = """"insert into chamdopapelaria (qcaneta, qlapis, qresma, qcola, 
                    prioridade, datacriacao, infocriador, infofunc, infochamado, status ) values ({0}, {1}, {2}, {3}, 
                    {4}, {5}, '{6}', '{7}', '{8}','{9}');""".format(q_caneta, q_lapis, q_resma, q_cola,
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


def remove_chamado_ti(self, json):
    id_ti = json['id']

    try:
        connection = Connection().get_connection()
        cursor = connection.cursor()
        deleta = "delete from chamadoti where id={0}".format(id_ti)
        cursor.execute(deleta)
        connection.commit()
        self.listar()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

def remove_chamado_pape(self, json):
    id_pape = json['id']

    try:
        connection = Connection().get_connection()
        cursor = connection.cursor()
        deleta = "delete from chamdopapelaria where id={0}".format(id_pape)
        cursor.execute(deleta)
        connection.commit()
        self.listar()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error", error)

    finally:
        if connection:
            cursor.close()
            connection.close()

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
            Id = row[0]
            tipo_chamado = row[1]
            prioridade = row[2]
            data_criacao = row[3]
            info_criador = row[4]
            info_func = row[5]
            info_chamado = row[6]
            status = row[7]
        json_volta = {

            'id': Id,
            'tipo_chamado': tipo_chamado,
            'prioridade': prioridade,
            'data_criacao': data_criacao,
            'info_criador': info_criador,
            'info_func': info_func,
            'info_chamado': info_chamado,
            'status': status,
        }

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



def lista_ti_id(self, json):
    id_chamado = json['id']

    try:
        connection = Connection().get_connection()
        cursor = connection.cursor()
        select = "select * from chamadoti where id = {0}".format(id_chamado)
        cursor.execute(select)
        chamado = cursor.fetchall()

        for row in chamado:
            Id = row[0]
            tipo_chamado =  row[1]
            prioridade = row[2]
            data_criacao = row[3]
            info_criador = row[4]
            info_func = row[5]
            info_chamado =  row[6]
            status =  row[7]
        json_volta = {

            'id': Id,
            'tipo_chamado': tipo_chamado,
            'prioridade': prioridade,
            'data_criacao': data_criacao,
            'info_criador': info_criador,
            'info_func': info_func,
            'info_chamado': info_chamado,
            'status': status,
        }

    except (Exception, psycopg2.Error) as error:
        print("Error", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()

def lista_pape_id(self, json):
    id_chamado = json['id']

    try:
        connection = Connection().get_connection()
        cursor = connection.cursor()
        select = "select * from chamadopapelaria where id = {0}".format(id_chamado)
        cursor.execute(select)
        chamado = cursor.fetchall()

        for row in chamado:
            Id = row[0]
            qcaneta =  row[1]
            qlapis = row[2]
            qresma = row[3]
            qcola = row[4]
            prioridade = row[5]
            datacriacao = row[6]
            infocriador =  row[7]
            infofunc =  row[8]
            infochamado = row[9]
            status = row[10]
        json_volta = {

            'id': Id,
            'qcaneta': qcaneta,
            'qlapis': qlapis,
            'qresma': qresma,
            'qcola': qcola,
            'prioridade': prioridade,
            'datacriacao': datacriacao,
            'infocriador': infocriador,
            'infofunc': infofunc,
            'infochamado': infochamado,
            'status': status,
        }
    except (Exception, psycopg2.Error) as error:
        print("Error", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()

def list_todos_setores(self):
    try:
        connection = Connection().get_connection()
        cursor = connection.cursor()
        select = "select * from setor"
        cursor.execute(select)
        chamado = cursor.fetchall()

        for row in chamado:
            Id = row[0]
            setor = row[1]
            idsetor =row[2]
        json_volta = {

            'id': Id,
            'setor': setor,
            'idsetor': idsetor,
        }

    except (Exception, psycopg2.Error) as error:
        print("Error", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()



