from Bdd import *
from Productos import *

class Administrador:
    def __init__(self) -> None:
        pass
    
    
    def verProductos():
        pass
    
    def eliminarProductos():
        pass
    
    def modificarProductos():
        pass
    
    def agregarProductos(self, codigo, nombre, descipcion, precio, stock, categoria):
        
        self.codigo= input('Ingrese el código del producto.')
        self.nombre= input('Ingrese nombre del producto.')        
        self.descipcion= input('Ingrese la descripción del producto.')
        self.precio= input('Ingrese el precio del producto.')
        self.stock= input('Ingrese el stock del producto.')        
        self.categoria= input('Ingrese la categoria del producto.')
        
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (idproducto, nombre, descripcion, precio, stock, ) VALUES (?,?,?,?,?,?)", (self.codigo, self.nombre, self.descripcion, self.precio, self.stock, self.categoria))
    self.conexion.commit()
    print(f"El producto {self.nombre} se agrego exitosamente. ")
   

        
    
        
        
