import psycopg2
from connection import Connection

#pip install psycopg2

class Operacoes():

    def salvar(self, nome, sobrenome, curso):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            insert = """insert into chamadoti (nome, sobrenome, curso) values ('{0}', '{1}','{2}');""".format(nome, sobrenome, curso)
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