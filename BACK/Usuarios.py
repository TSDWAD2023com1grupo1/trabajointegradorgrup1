
class Usuarios:
    def _init_(self, password, registrofecha, email, direccion):
        self.password = password
        self.registrofecha = registrofecha
        self.email = email
        self.direccion = direccion
        self.usuarios = []  # lista los usuarios

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_registrofecha(self):
        return self.registrofecha

    def set_registrofecha(self, registrofecha):
        self.registrofecha = registrofecha  

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def ingresar_usuario(self, usuario):
        # Agregar lógica para verificar la existencia del usuario
        if usuario not in self.usuarios:
            self.usuarios.append(usuario)
        else:
            print("El usuario ya existe")
            
    def ingresar_contraseña(self, contraseña):
        if password == password.len():
            for password in self.password:
                if password.isupper():
                    return True
            return False

    def modificar_password (self, password) :
    self.password = nueva_password

    

# Ejemplo de uso:
#usuario1 = Usuarios("password1", "01/01/2023", "usuario1@example.com", "Dirección 1")
#usuario2 = Usuarios("password2", "02/01/2023", "usuario2@example.com", "Dirección 2")

#usuario1.ingresar_usuario(usuario2)  # Agregar usuario2 a la lista de usuarios de usuario1
#print(usuario1.usuarios)  # Debería mostrar ["usuario2@example.com"]

#usuario1.eliminar_usuario(usuario2)  # Eliminar usuario2 de la lista de usuarios de usuario1
#print(usuario1.usuarios)  # Debería mostrar []