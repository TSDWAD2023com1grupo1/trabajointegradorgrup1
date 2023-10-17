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