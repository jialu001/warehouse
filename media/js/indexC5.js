$(document).ready(
    function(){
        var  tishi = {"分公司":"如：广州分公司","备件名称":"设备分类，如：A9K备件","规格型号":"设备型号","设备类型":"所属厂家：如思科"
        ,"sn码":"SN码","订单号":"","入库地点":"入库地点，如太阳城","数量":"数量","货位号":"所在库房的位置",
        "所属网络":"如承载网","资产标签":"资产标签 可不填","备注":"其他信息"};
        var idset = ["fenggongsi","name","xinghao","leixing","sn","dingdanhao","rukudidian",
            "shuliang","huoweihao","suoshuwangluo","zichanbiaoqian","beizhu"];
        var iptoS ={};
        var ptag = document.getElementsByTagName("h5");
        var i=0;

         //此处往json 加入用户email 信息
         var email =$.cookie('email');
         iptoS["email"] = email;

        var shuruku = document.getElementsByClassName("myinp");
        for(var key in tishi){
            if(i<ptag.length){
                ptag[i].innerHTML=(key);
                shuruku[i].setAttribute("placeholder",tishi[key]);
                shuruku[i].setAttribute("id",idset[i]);
            }
            i++;
        }
        console.log("已设置输入框的相关参数");
        //入库页面确认
        $("#save").click(function(){
           console.log("准备获取输入框的相关参数");
           for(i=0;i<shuruku.length;i++){
              iptoS[idset[i]]=shuruku[i].value;
           }
           console.log("已获取输入框的相关参数，准备上传至服务器");
             $.post("add",
                 iptoS,
                    function(data,status){
                alert(data["info"]);

                if(data["type"]==1){
                     hideMask();
                     $("#gengxin").css("display","none");
                     $("#dh_result").css("display","block");
                     var margintop = $(document).scrollTop()+50;
                     $("#dh_result").css("margin-top",(margintop));
                     setTimeout(function(){
                         $("#dh_result").css("display","none");
                     },1000);
                }else {
                    //此处进行权限不够操作

                    return ;
                }
                 });

      });
        //入库按钮点击
        $("#zeng").click(function(){
            showMask();
             var margintop = $(document).scrollTop()+100;
            $("#ruku_select").css("margin-top",(margintop));
            $("#ruku_select").css("display","block");
        });
        //选择页面 取消按钮
         $("#ruku_no").click(function(){
            hideMask();
            $("#ruku_select").css("display","none");
        });
         //进入承载网入库填写页面
         $("#ruku_czw").click(function(){
            $("#ruku_select").css("display","none");
            var margintop = $(document).scrollTop();
            $("#gengxin").css("margin-top",(margintop));
            $("#gengxin").css("display","block");
        });
         //辅助填写
          $("#gengxin_auto").click(function(){
              fuzhuInfo = ["广州分公司","A9K","","思科","","","太阳城",
                  "1","","承载网","暂无","某工程入库"];
           for(i=0;i<shuruku.length;i++){
              shuruku[i].value = fuzhuInfo[i];
           }
        });
        // 打开光模块搜索
        $("#gMKout").click(function(){
            showMask();
            var margintop = $(document).scrollTop()+100;
            $("#out_gmk").css("margin-top",(margintop));
            $("#out_gmk").css("display","block");
        });

        // 关闭光模块搜索
        $("#cancel_gmk").click(function(){
            hideMask();
            $("#out_gmk").css("display","none");
        });

        //入库页面的关闭按钮
      $("#close").click(function(){
            hideMask();
            $("#gengxin").css("display","none");
      });
        //系统日志按钮
      $("#sys_btn").click(function () {
          $("#user_Table").css("display","block");
          $("#chengdh0").css("display","none");
          iptoS = {};
            $.ajax({
                 type : "get",
                 url : "op/show",
                 data : iptoS,
                 success : function(data,status){
                     if (status=="success"){
                    var table = document.getElementById("user_Table");
                    var i = 1;
                    var j = 0;
                 data.forEach(function (item,index,array)
                 {
                    var row = table.insertRow(i);
                        j=0;
                    for (var key in item) {
                        row.insertCell(j).innerHTML =item[key]  ;
                        j++;
                        }
                            i++;
                    }) //此处ret处理循环结束
                        }
                 }
             });
      });
        //出库按钮点击
      // $("#out").click(function () {
      //     showMask();
      //     var margintop = $(document).scrollTop()+100;
      //     $("#out_info").css("margin-top",(margintop));
      //     $("#out_info").css("display","block");
      // });


    function showMask(){
        $("#mask").css("height",$(document).height());
        $("#mask").css("width",$(document).width());
        $("#mask").show();
    }
    //隐藏遮罩层
    function hideMask(){
        $("#mask").hide();
    }


    }




    );
