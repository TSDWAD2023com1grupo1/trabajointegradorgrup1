
from Conexion import connect


class Persona:
    def __init__(self, idUsuario, email, password, fechaRegistro, nombre, direccion):
        self.idUsuario = idUsuario
        self.email = email
        self.password = password
        self.fechaRegistro = fechaRegistro
        self.nombre = nombre
        self.direccion = direccion
    
    
    def login():
        pass
    
    def loginOut():
        pass
    
    def verProd(self):
        print("--------NUESTROS PRODUCTOS----------")
            
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM productos")
        resultado =cursor.fetchall()
        self.conn.commit()
        contador=1
        for prod in resultado:
            datos="{0}. IDProducto {1} | Nombre: {2} | Precio: {4}"
            print(datos.format(contador,prod[0],prod[1],prod[2],prod[3]))
            contador = contador +1
            print("")   

    

class Usuarios(Persona):
    def __init__(self, idUsuario, email, password, fechaRegistro, nombre, direccion):
        super().__init__(idUsuario, email, password, fechaRegistro, nombre, direccion)


class Administrador(Persona):
    def __init__(self, idUsuario, email, password, fechaRegistro, nombre, direccion):
        super().__init__(idUsuario, email, password, fechaRegistro, nombre, direccion)
        self.conn, self.cursor = connect() # con esto guarda la conexión y el cursor en el objeto
        
        
    # def verProd(self):
        
    #     print("--------NUESTROS PRODUCTOS----------")
            
    #     cursor = self.conn.cursor()
    #     cursor.execute("SELECT * FROM productos")
    #     resultado =cursor.fetchall()
    #     self.conn.commit()
    #     contador=1
    #     for prod in resultado:
    #         datos="{0}. IDProducto {1} | Nombre: {2} | Precio: {4}"
    #         print(datos.format(contador,prod[0],prod[1],prod[2],prod[3]))
    #         contador = contador +1
    #         print("")    
        
        
    def cargarProd(self):
        
        self.nombre = input('Ingrese nombre del producto: ')
        self.descripcion = input('Ingrese la descripción del producto: ')
        self.precio = float(input('Ingrese el precio del producto: '))
        self.stock = int(input('Ingrese el stock del producto: '))
        self.idproveedor = int(input("Ingrese el id del proveedor: "))
        self.idCategoria = int(input('Ingrese la categoría del producto: '))
        

        cursor = self.conn.cursor()

        cursor.execute("INSERT INTO productos (nombre, descripcion, precio, stock, idproveedor, idCategoria) VALUES (%s, %s, %s, %s, %s, %s)", (self.nombre, self.descripcion, self.precio, self.stock, self.idproveedor, self.idCategoria))
        self.conn.commit()


        print("-" * 60)
        print(f"El Producto {self.nombre} se agregó exitosamente.")
        print("-" * 60)
    
    
    def eliminarProd(self):
         print("--------ELIMINAR PRODUCTO----------")
         
         cursor = self.conn.cursor()         

         cursor.execute("SELECT idproducto, nombre FROM productos")
         productos = cursor.fetchall()
         
         print("Elige un producto para eliminar:")
         for i, producto in enumerate(productos):
             print(f"{i+1}. {producto[1]}")
         
         seleccion = int(input("Ingrese el número del producto que desea eliminar: "))
         producto_a_eliminar = productos[seleccion-1]
         
         sql = "DELETE FROM productos WHERE idproducto = %s"
         val = (producto_a_eliminar[0], )
                 
         cursor.execute(sql, val)
         self.conn.commit()
         print(f"El producto {producto_a_eliminar[1]} ha sido eliminado.")    
        
    
    def modificarProd(self):
        print("--------ACTUALIZAR PRODUCTO----------")
        
        cursor = self.conn.cursor()         

        cursor.execute("SELECT idproducto, nombre FROM productos")
        productos = cursor.fetchall()
         
        print("Elige un producto para actualizar:")
        for i, producto in enumerate(productos):
             print(f"{i+1}. {producto[1]}")
         
        seleccion = int(input("Ingrese el id del producto que desea actualizar: "))
        
        nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
        nuevo_descr = input("Ingrese la nueva descripción del producto: ")
        nuevo_precio = input("Ingrese el nuevo precio del producto: ")
        nuevo_stock = input("Ingrese el nuevo stock del producto: ")
        nuevo_idprove = input("Ingrese el nuevo ID del proveedor del producto: ")
        nuevo_idcat = input("Ingrese el nuevo ID de la categoría del producto: ")

        
        producto_modificar = productos[seleccion-1]
         
        sql = "UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, stock = %s, idproveedor = %s, idCategoria = %s WHERE idproducto = %s"

        val = (nuevo_nombre, nuevo_descr, nuevo_precio, nuevo_stock, nuevo_idprove, nuevo_idcat, producto_modificar[0])
                 
        cursor.execute(sql, val)
        self.conn.commit()
        print(f"El producto {producto_modificar[1]} ha sido actualizado.")    
    







