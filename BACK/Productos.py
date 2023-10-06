from Usuarios import *


class Productos:
    def _init_(self, nombre, descripcion, precio, stock, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
        self.usuarios = []  #  lista  usuarios
        self.productos = []  # lista productos

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

def set_categoria(self, categoria):
        self.categoria = categoria

def ver_productos(self):
        return self.productos

def agregar_producto(self, producto):
        self.productos.append(producto)

def comprar_producto(self, indice):
        if 0 <= indice < len(self.productos):
            if self.productos[indice].stock > 0:
                self.productos[indice].stock -= 1
                return f"Has comprado {self.productos[indice].nombre}"
            else:
                return f"Producto {self.productos[indice].nombre} sin stock"
        else:
            return "Índice de producto fuera de rango"

def eliminar_producto(self, indice):
        if 0 <= indice < len(self.productos):
            del self.productos[indice]
        else:
            print("producto eliminado")
    #tostring 
def _str_(self):
        # función para mostrar la información 
        return f"Nombre: {self.nombre}\nDescripción: {self.descripcion}\nPrecio: {self.precio}\nStock: {self.stock}\nCategoría: {self.categoria}\nUsuarios: {', '.join(self.usuarios)}"



# Ejemplo:
#producto = Productos("Producto1", "Descripción del producto", 100, 10, "Categoría")
#producto.agregar_usuario("Usuario1")
#producto.agregar_usuario("Usuario2")

#producto1 = Producto("ProductoA", "Descripción A", 50, 5, "Categoría A")
#producto2 = Producto("ProductoB", "Descripción B", 60, 3, "Categoría B")

#producto.agregar_producto(producto1)
#producto.agregar_producto(producto2)

#print(producto.ver_productos())

#print(producto.comprar_producto(0))
#print(producto.comprar_producto(0))

#producto.eliminar_producto(1)

#print(producto.ver_productos())