import sqlite3

historiaConnection=sqlite3.connect("historiasql")
historiacursor=historiaConnection.cursor()
historiacursor.execute("CREATE TABLE lista_PreguntasHistoria (pregunta VARCHAR(100), respuesta1 VARCHAR(50), respuesta2 VARCHAR(50), respuesta3 VARCHAR(50), respuesta4 VARCHAR(50))")


historiaConnection.close()