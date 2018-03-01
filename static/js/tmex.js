$(".alert").fadeTo(2000, 500).slideUp(500, function(){
    $(".alert").slideUp(500);
});

$('#signInForm').submit(function(){ //listen for submit event
    var params = [
               {name: "redirect_path",value: $('#signInForm').attr('redirect_path')},
               {name: "username"     ,value: $('#emailInput').val()},
               {name: "password"     ,value: $('#passwordInput').val()},
    ];


   $('#signInForm').append($.map(params, function (param) {
        return   $('<input>', {
            type: 'hidden',
            name: param.name,
            value: param.value
        })
   }));
   //alert($('#signInForm').attr('redirect_path'));
   return true;
});
