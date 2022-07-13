$(function(){
    $("#boton_registro").click(function(){

        var usuario1 = $("#id_usuario").val();
        var pass = $("#id_pass").val();

        if (usuario1 == "usuario_registrado"){
            if(pass == 1234){
                alert("USUARIO CORRECTO")
                alert("BIENVENIDO!!")
                window.open('/usuario_registrado')
            }
            else{
                alert("usuario o contraseña incorrecto")
                alert("ACCESO DENEGADO!!")
                
            }
        }
        else{
            alert("usuario o contraseña incorrecto")
            alert("ACCESO DENEGADO!!")
            
        }



    })
});


