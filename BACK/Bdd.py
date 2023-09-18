
import mysql.connector

class Conexion:
    
    def __init__(self, host, user, password, db):
        self.host = 'host'
        self.user = 'root'
        self.password = '05061992'
        self.db = 'proyectofinal'
        
    def obtenerConexion(self):
        return mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            db = self.db  
            
        )
        
