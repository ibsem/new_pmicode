import psycopg2
from connection import Connection

#pip install psycopg2

class Operacoes():

    def save_chamado_ti(self,json):

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
            info_func, info_chamado, status) values ('{0}', {1}, {2}, '{3}', '{4}', '{5}', '{6}');""".format(
            tipo_chamado, prioridade, data_criacao, info_criador,
            info_func, info_chamado, status)
        cursor.execute(insert)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error", error)
    finally:
        if connection:
            cursor.close()
            connection.close()

    def save_chamado_pape(self, json):
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
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            insert = """insert into chamdopapelaria (q_caneta, q_lapis, q_resma, q_cola, 
                    prioridade, data_criacao, info_criador, info_func, info_chamado, status ) values ({0}, {1}, {2}, {3}, 
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


    def atualizar(self,id,nome,sobrenome,curso):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            '''
            checa = """select {0} from pessoa;""".format({0})
            cursor.execute(checa)
            connection.commit()
            volta = cursor.fetchall()
            if volta == None:
                print("Id inexistente")
            else:'''
            atualiza= """UPDATE pessoa 
                        SET nome = '{0}', sobrenome = '{1}', curso='{2}' 
                        WHERE id={3};""".format(nome,sobrenome,curso,id)
            #print(atualiza)
            cursor.execute(atualiza)
            connection.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
    def deletar(self,id):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            deleta="delete from pessoa where id={0}".format(id)
            cursor.execute(deleta)
            connection.commit()
            self.listar()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error", error)

        finally:
            if connection:
                cursor.close()
                connection.close()

    def listar(self):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            select = "select * from pessoa"
            cursor.execute(select)
            pessoas = cursor.fetchall()

            for row in pessoas:
                print("Id = ", row[0], )
                print("nome = ", row[1])
                print("sobrenome  = ", row[2])
                print("curso = ", row[3], "\n")

        except (Exception, psycopg2.Error) as error:
            print("Error", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()