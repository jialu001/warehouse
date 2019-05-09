$(document).ready(function() {
        //上传后台的iptoS
         var iptoS ={};
         var email =$.cookie('email');
         iptoS["email"] = email;

          $.ajax({
         type : "get",
         url : "users/info",
         data : iptoS,
         async : true,
         success : function(ret){

                        $("#user_id").text(ret["id"]);
                        $("#user_email").text(ret["邮箱"]);
                        $("#user_level").text(ret["权限等级"]);
                         $("#user_name").text(ret["姓名"]);
                          $("#user_phone").text(ret["电话"]);
                           $("#user_psd").text(ret["密码"]);
                }
            });
})