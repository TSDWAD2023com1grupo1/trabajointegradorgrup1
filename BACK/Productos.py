from Persona import *


class Productos:
    def __init__(self, idproducto, nombre, descripcion, precio, stock, idproveedor, idCategoria):
        self.idproducto = idproducto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.idproveedor = idproveedor
        self.idCategoria = idCategoria


def get_idproducto(self):
        return self.idproducto

def set_idproducto(self, idproducto):
        self.codigo = idproducto
        
def get_nombre(self):
        return self.nombre

def set_nombre(self, nombre):
        self.nombre = nombre

def get_descripcion(self):
        return self.descripcion

def set_descripcion(self, descripcion):
        self.descripcion = descripcion

def get_precio(self):
        return self.precio

def set_precio(self, precio):
        self.precio = precio

def get_stock(self):
        return self.stock

def set_stock(self, stock):
        self.stock = stock

def get_categoria(self):
        return self.categoria

def set_categoria(self, idCategoria):
        self.idCategoria = idCategoria

def get_idproveedor(self):
       return self.idproveedor

def set_idproveedor(self, idproveedor):
       self.idproveedor = idproveedor
  

def __str__(self):
        
        return f"Nombre: {self.nombre}\nDescripción: {self.descripcion}\nPrecio: {self.precio}\nStock: {self.stock}\nCategoría: {self.idCategoria}\nUsuarios: {', '.join(self.usuarios)}"



