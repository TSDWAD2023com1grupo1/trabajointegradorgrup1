const btnSignIn = document.getElementById("sign-in"),
      btnSignUp = document.getElementById("sign-up"),
      formRegister = document.querySelector(".register"),
      formLogin = document.querySelector(".login");
     
if (window.location.href.includes("login.html")){
    btnSignIn.addEventListener("click", () =>{
    
        formRegister.classList.add("hide"),
        formLogin.classList.remove("hide");
        }
    );
    btnSignUp.addEventListener("click", e =>{
        formLogin.classList.add("hide"),
        formRegister.classList.remove("hide");     
        }
    );
    document.getElementById("user-registrar").addEventListener("click", function(e) {
    e.preventDefault(); 
    
    registrar(); 
    }
    );
};

if(window.location.href.includes("login.html")){


    function registrar(){
        
        let nombre = document.getElementById("name").value;
        let email = document.getElementById("email").value;
        let pass = document.getElementById("clave").value;
        let passrepit = document.getElementById("clave-repite").value;
    
        let warnings = "";
        let entrar = false;
        let regexEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        let regexNombre = /^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$/;
        let regexContraseña = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).{8,16}$/;
        
        
        if (nombre === "" || email === "" || pass === "") {
            warnings += "Todos los campos son obligatorios.\n"
            entrar = true;
        };
        if(nombre.length < 4){
            warnings += "El nombre no es valido.\n";
            entrar = true;
        };
        if(!regexNombre.test(nombre)) {
            warnings += "El nombre solo debe contener letras.\n";
            entrar = true;
        };
        if (!regexEmail.test(email)) {
            warnings += 'El email ingresado no es válido..\n';
            entrar = true;
        };  
        if(pass.length <8){
            warnings += 'La contraseña debe contener mínimo 8 caracteres.\n';
            entrar = true;
        };
        
        if(pass.length >16){
            warnings += 'La contraseña no puede superar los 16 caracteres.\n';
            entrar = true;
        };
        if(!regexContraseña.test(pass)){
            warnings += 'La contraseña debe contener al menos un número, una letra mayúscula, una letra minúscula y un caracter no alfanumérico.\n';
            entrar = true;
        };
        if( pass !== passrepit){
            warnings += "Las contraseñas no coinciden.\n";
            entrar = true;
        };