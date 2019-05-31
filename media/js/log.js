
(function ($) {
    "use strict";

    
    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');
    var iptoS ={};

    $('.validate-form').on('submit',function(){
        var check = false;
        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
            switch(i){
                case 0:iptoS["email"]=input[i].value;
                case 1:iptoS["password"] =input[i].value;
                default: ;
            }
        }
        $.ajax({
                 type : "post",
                 url : "users/check",
                 data : iptoS,
                 async : false,
                 success : function(data,status){
                     if (status=="success"){
                     //      alert(data["info"]+"\n"+
                     //  data["type"]  +"\n"+
                     // location.href);

                          if(data["type"] =="t"){
                                check = true ;
                          }

                    $.cookie('email',data["email"] , { expires: 7, path:'/'  });
                     }
                 }
             });
        //alert(check);
        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    

})(jQuery);