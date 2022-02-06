// SHOW ERROR MODAL
$(document).ready(function() {
    if ($('#flashes').children().length > 0){
      $("#modal-login-error").modal();
    }

    //////////// BORRAR CLIENTE ////////////
    $("#borrar-usuario").click(function(){
      $("#modal-borrar").modal();
    });


    $('#send-mail').click(function(){
      
      var mail = $('#mail').val();

      $.ajax({
        url: "/validate_mail/",
        type: "post",
        data: {'mail': mail},
        success: function(usuario) {
          if (usuario == null){
            $('#modal-alert-text').text('El mail ingresado no existe')
            $("#modal-alert").modal();
          } else{
            $.ajax({
              url: "/send_mail/",
              type: "post",
              data: {'mail': mail},
              success: function() {
                $('#modal-alert-text').text('Un mail fue enviado a ' + mail + ' con las instrucciones para cambiar la contraseña.')
                $("#modal-alert").modal();
              }
            });
          }
        }
    });

      
    });
    
});