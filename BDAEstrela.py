import pyodbc

class BD():
    def conecta_ao_banco(driver='SQL Server', server='LAPTOP-O1IN2UDE', database='AEstrela', username = None, password = None, trusted_connection='yes'):

        string_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TRUSTED_CONNECTION={trusted_connection}"

        conexao = pyodbc.connect(string_conexao)
        cursor = conexao.cursor()

        return conexao, cursor

    conexao, cursor = conecta_ao_banco()
            
    query = 'SELECT NomeCidade FROM cidade'
    cursor.execute(query)


    #Cidades BD    
    ciudades = [row.NomeCidade for row in cursor.fetchall()]

    #Heuristica Curitiba
    HCuritiba = cursor.execute('SELECT Heuristica FROM cidade').fetchall()

    #Conexão com os 5 destinos possíveis:
    ObjCuritiba = cursor.execute('select NomeCidade from cidade where CidadeID = 7').fetchall()
    ObjPalmeira = cursor.execute('select NomeCidade from cidade where CidadeID = 8').fetchall()
    ObjLapa = cursor.execute('select NomeCidade from cidade where CidadeID = 12').fetchall()
    ObjContenda = cursor.execute('select NomeCidade from cidade where CidadeID = 16').fetchall()
    ObjSJP = cursor.execute('select NomeCidade from cidade where CidadeID = 15').fetchall()


    