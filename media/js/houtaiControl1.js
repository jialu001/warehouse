$(document).ready(
    function () {
         $("#houtaiSH").click(function () {
        // level check
          var data = {};
          var email =$.cookie('email');
          data["email"] = email;
           $.ajax({
         type : "get",
         url : "users/levelCheck",
         data : data,
         async : true,
         success : function(ret){
             // 1 权限仅能出库光模块
                    if(ret["level"]=="1"||ret["level"]=="2"){
                        alert("权限不足");
                        return ;
                    }
                    else {
                        window.location.href = 'dh';

                    }
                }
            });
    });


         $("#BuChongGongNeng").click(function () {
             alert("功能待开发中");
         })
    }


);