$(document).ready(
    function(){
        var  tishi = {"分公司":"如：广州分公司","备件名称":"设备分类，如：A9K备件","规格型号":"设备型号","设备厂家":"所属厂家：如思科"
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
        //入库czw table相关信息
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
        //chengzaiwang页面确认

        $("#save").click(function(){
           console.log("准备获取输入框的相关参数");
           for(i=0;i<shuruku.length;i++){
              iptoS[idset[i]]=shuruku[i].value;
           }
           console.log("已获取输入框的相关参数，准备上传至服务器");
            // alert("已提交入库申请，等待管理员审核");
              hideMask();
            $("#gengxin").css("display","none");
             $.post("add", iptoS, function(data,status){
                // alert(data["info"]);

                if(data["type"]==1){
                    toCache("ruku","承载网",data['id'],"");
                     // $("#gengxin").css("display","none");
                     // $("#dh_result").css("display","block");
                     // var margintop = $(document).scrollTop()+50;
                     // $("#dh_result").css("margin-top",(margintop));
                     // setTimeout(function(){
                     //     $("#dh_result").css("display","none");
                     // },1000);
                }else {
                    //此处进行权限不够操作

                    return ;
                }
                 });

      });
        //入库按钮点击
        $("#zeng").click(function(){
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
                    if(ret["level"]=="1"){
                        alert("权限不足");
                        return ;
                    }
                    else {   showMask();
             var margintop = $(document).scrollTop()+100;
            $("#ruku_select").css("margin-top",(margintop));
            $("#ruku_select").css("display","block");
                    }
                }
            });


        });
        //选择页面 取消按钮
         $("#ruku_no").click(function(){
            hideMask();
            $("#ruku_select").css("display","none");
        });
        //进入光模块入库填写页面
         $("#ruku_gmk").click(function(){
            $("#ruku_select").css("display","none");
            var margintop = $(document).scrollTop();
            $("#ruku_table_gmk").css("margin-top",(margintop));
            $("#ruku_table_gmk").css("display","block");
            getInfo("gmk/allinfo");
        });

         $("#dropdown-content-gmk-right-2").on("click","li",function (){


             if($(this).text()=="下一页"){
                setNext2();
             }
             else {
                 $("#xingHaoInfo-2").text("选择型号为"+":"+($(this).text()));
             }
             //alert($(this).text());

         });
          $("#dropdown-content-gmk-right").on("click","li",function (){


             if($(this).text()=="下一页"){
                setNext();
             }
             else {
                 $("#xingHaoInfo").text("选择型号为"+":"+($(this).text()));
             }
             //alert($(this).text());

         });

         $("#gmk_save").click(function () {
             var changJ = getCJinfo($("#changJiaInfo").text());

             var xH =getXh($("#xingHaoInfo").text());

             var num = $("#gmk_ip").val();

             var data={};
             data['cj']=changJ;
             data['xh']=xH;

             data['num']="0;"+num;
             var email =$.cookie('email');
             data["email"] = email;
             var ID_gmk = (ruKu("gmk/add",data));
               if(ID_gmk.toString() == "-1" ){
                alert("重复操作，请等待审核");
                hideMask();
                $("#ruku_table_gmk").css("display","none");
                return ;
            }
              // gmk needs id and num
             toCache("ruku","gmk",ID_gmk,"");
              hideMask();
            $("#ruku_table_gmk").css("display","none");
         });

        $("#gmk_save-2").click(function () {

             var changJ = getCJinfo($("#changJiaInfo-2").text());
            //
              var xH =getXh($("#xingHaoInfo-2").text());
            //
              var num = $("#gmk_ip-2").val();
            //
             var data={};
             data['cj']=changJ;
             data['xh']=xH;
             data['num']="1"+";"+num;
             var email =$.cookie('email');
             data["email"] = email;
             console.log(data);
             var ID_gmk = (ruKu("gmk/add",data));
               if(ID_gmk.toString() == "-1" ){
                alert("重复操作，请等待审核");
                hideMask();
                $("#out_gmk").css("display","none");
                return ;
            }
              // gmk needs id and num
             toCache("出库","gmk",ID_gmk,"");
              hideMask();
            $("#out_gmk").css("display","none");
         });

         $("#dropdown-hw").click(function () {
                $("#dropdown-1-s").text("华为");
                setChangJiaInfo("huawei");
                setdropdown(0,hwgmk);
         })
         $("#dropdown-hw-2").click(function () {
                $("#dropdown-2-s").text("华为");
                setChangJiaInfo2("huawei");
                setdropdown2(0,hwgmk);
         })
         $("#dropdown-sk").click(function () {
             $("#dropdown-1-s").text("思科");
             setChangJiaInfo("sike");
              setdropdown(0,skgmk);
         })
         $("#dropdown-sk-2").click(function () {
             $("#dropdown-2-s").text("思科");
             setChangJiaInfo2("sike");
              setdropdown2(0,skgmk);
         })
         $("#dropdown-h3").click(function () {
             $("#dropdown-1-s").text("H3C");
              setChangJiaInfo("h3c");
              setdropdown(0,h3gmk);
         })
         $("#dropdown-h3-2").click(function () {
             $("#dropdown-2-s").text("H3C");
              setChangJiaInfo2("h3c");
              setdropdown2(0,h3gmk);
         })
         $("#dropdown-br").click(function () {
             $("#dropdown-1-s").text("贝尔");
              setChangJiaInfo("beier");
              setdropdown(0,brgmk);

         })
          $("#dropdown-br-2").click(function () {
             $("#dropdown-2-s").text("贝尔");
              setChangJiaInfo2("beier");
              setdropdown2(0,brgmk);

         })
         $("#dropdown-dp").click(function () {
             $("#dropdown-1-s").text("迪普");
              setChangJiaInfo("dipu");
              setdropdown(0,dpgmk);

         })

        $("#dropdown-dp-2").click(function () {
             $("#dropdown-2-s").text("迪普");
              setChangJiaInfo2("dipu");
              setdropdown2(0,dpgmk);

         })
         //光模块取消按钮
         $("#gmk_close").click(function(){
            hideMask();
            $("#ruku_table_gmk").css("display","none");
        });
         //光模块2取消按钮
         $("#gmk_close-2").click(function(){
            hideMask();
            $("#out_gmk").css("display","none");
        });
         //进入承载网入库填写页面
         $("#ruku_czw").click(function(){
            $("#ruku_select").css("display","none");
            var margintop = $(document).scrollTop();
            $("#gengxin").css("margin-top",(margintop));
            $("#gengxin").css("display","block");
        });
        var  label169=["厂家","名称","型号","SN","数量"
             ,"货柜号","备注","工程","资产标签"];
          //进入169网入库填写页面
         $("#ruku_169").click(function(){
            $("#ruku_select").css("display","none");
            var margintop = $(document).scrollTop();
            $("#ruku_table_169").css("margin-top",(margintop));
            $("#ruku_table_169").css("display","block");
            // 往入库table填充相关信息
             var str = "测试";
             var placeIn = "请输入信息";
             $("#left_169").empty();
             $("#right_169").empty();
             for (var i=0;i<label169.length;i++){
                 if(i<5){
                      $("#left_169").append(
            "<div class='row ' style='width:100%;height: 7%;margin-top: 2%'> " +
                        //label
                       "<div style='width: 40%;height: 60%'> <label class='leftmove5' style='float:right;margin-right: 10%'>"+label169[i]+ "</label>" +
                       "</div> "+
                        //input
                        "<div class='leftmovelittle' style='width: 55%;height: 60%'>" +
                       " <input class='ip_169 leftmovelittle' type='text'  id='srk_169' placeholder='"+placeIn+"' " +
                       " style='border-radius: 6px;'> " +
                       " </div>" +
            "</div>"
                   );
                 }else{
                     $("#right_169").append(
            "<div class='row ' style='width:100%;height: 7%;margin-top: 2%'> " +
                        //label
                       "<div style='width: 40%;height: 60%'> <label class='leftmove5' style='float:right;margin-right: 10%'>"+label169[i]+ "</label>" +
                       "</div> "+
                        //input
                        "<div class='leftmovelittle' style='width: 55%;height: 60%'>" +
                       " <input class='ip_169 leftmovelittle' type='text'  id='srk_169' placeholder='"+placeIn+"' " +
                       " style='border-radius: 6px;'> " +
                       " </div>" +
            "</div>"
                     );
                 }

             } //FOR循环填写结束

        });
         //辅助填写169
          $("#169_auto").click(function(){
              fuzhuInfo = ["思科","A9K","","","1","","169网入库",
                  "XX工程","暂无"];
           var toShuruku = document.getElementsByClassName("ip_169");
           for(i=0;i<toShuruku.length;i++){
              toShuruku[i].value = fuzhuInfo[i];
           }
        });
          //169-save
          $("#169_save").click(function(){
                var toShuruku = document.getElementsByClassName("ip_169");
                var ipto169={};
                 for(i=0;i<toShuruku.length;i++){
                ipto169[label169[i]]=toShuruku[i].value;
           }
           var email =$.cookie('email');
            ipto169["email"] = email;
            var ID_169 = (ruKu("169/add",ipto169));


             toCache("ruku","169",ID_169,"");
               //alert("已提交入库申请，等待管理员审核");
            $("#ruku_table_169").css("display","none");
             hideMask();
        });
          //169-close
          $("#169_close").click(function(){
              hideMask();
               $("#ruku_table_169").css("display","none");
        });
         //辅助填写CWZ
          $("#gengxin_auto").click(function(){
              fuzhuInfo = ["广州分公司","A9K","","思科","","暂无","",
                  "1","","承载网","暂无","某工程入库"];
           for(i=0;i<shuruku.length;i++){
              shuruku[i].value = fuzhuInfo[i];
           }
        });
        // 打开光模块出库NEW 528
        $("#gMKout").click(function(){
            showMask();
            var margintop = $(document).scrollTop()+10;
            $("#out_gmk").css("margin-top",(margintop));
            $("#out_gmk").css("display","block");
             getInfo("gmk/allinfo");
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



    function showMask(){
        $("#mask").css("height",$(document).height());
        $("#mask").css("width",$(document).width());
        $("#mask").show();
    }
    //隐藏遮罩层
    function hideMask(){
        $("#mask").hide();
    }

    function ruKu(url,data) {
          var id = -1 ;
          $.ajax({
         type : "post",
         url : url,
         data : data,
         async : false,
         success : function(ret){

             if(ret["type"]==1) {
                 id = ret["id"];
             }

                }
            });
          return id;
    }


    var hwgmk=[];
    hwgmk[0] ="huawei";
    var h3gmk=[];
    h3gmk[0] = "h3c";
    var skgmk=[];
    skgmk[0] = "sike";
    var dpgmk=[];
    dpgmk[0] = "dipu";
    var brgmk=[];
    brgmk[0] = "beier";
    var nextInfo = ["",""];
    function getInfo(url) {

          $.ajax({
         type : "get",
         //url : "search-post",
         url : url,
         data : " ",
         async : true,
         success : function(ret){
                 ret.forEach(function (item) {
                      var cjID = 0;
                    for (var key in item) {
                      if(key=="changjia"){
                          if(item[key]=="华为"){
                                cjID =1;
                          }
                          if(item[key]=="思科"){
cjID =2;
                          }
                          if(item[key]=="H3C"){
cjID =3;
                          }
                          if(item[key]=="贝尔"){
cjID =4;
                          }
                          if(item[key]=="迪普"){
cjID =5;
                          }
                      }
                       if(key=="xinghao"){
                          if( cjID ==1){
                                hwgmk.push(item[key]);
                          }
                            if( cjID ==2){
                                skgmk.push(item[key]);
                          }
                          if( cjID ==3){
                                h3gmk.push(item[key]);
                          }
                           if( cjID ==4){
                                brgmk.push(item[key]);
                          }
                            if( cjID ==5){
                                dpgmk.push(item[key]);
                          }
                      }
                      else {
                          continue;
                      }
                    }//for 结束
                 })
                }
            });

    }

    function setdropdown(start,changJia) {
             $("#dropdown-content-gmk-right").empty();
             var contNum = 6+start;
             for (i=start;((i<changJia.length-1));i++){
                 if(i<contNum ){
                       $("#dropdown-content-gmk-right").append(
                   "<li >"+ changJia[i+1] +"</li>"
                    );
                 }
                  else if(i==contNum){
                            $("#dropdown-content-gmk-right").append(
                   "<li id='right-down'>"+ "下一页" +"</li>"
                    );
                            nextInfo[0]=(contNum+1).toString();
                            nextInfo[1]=changJia[0];
                 }
             }//for循环结束
    }

    function setChangJiaInfo(str) {
        if(str=="huawei"){
            $("#changJiaInfo").text("选择厂家为：华为");
        }
         if(str=="sike"){
            $("#changJiaInfo").text("选择厂家为：思科");
        }
         if(str=="h3c"){
            $("#changJiaInfo").text("选择厂家为：华三");
        }
         if(str=="dipu"){
            $("#changJiaInfo").text("选择厂家为：迪普");
        }
         if(str=="beier"){
            $("#changJiaInfo").text("选择厂家为：贝尔");
        }
    }

     function setdropdown2(start,changJia) {
             $("#dropdown-content-gmk-right-2").empty();
             var contNum = 6+start;
             for (i=start;((i<changJia.length-1));i++){
                 if(i<contNum ){
                       $("#dropdown-content-gmk-right-2").append(
                   "<li >"+ changJia[i+1] +"</li>"
                    );
                 }
                  else if(i==contNum){
                            $("#dropdown-content-gmk-right-2").append(
                   "<li id='right-down'>"+ "下一页" +"</li>"
                    );
                            nextInfo[0]=(contNum+1).toString();
                            nextInfo[1]=changJia[0];
                 }
             }//for循环结束
    }

    function setChangJiaInfo2(str) {
        if(str=="huawei"){
            $("#changJiaInfo-2").text("选择厂家为：华为");
        }
         if(str=="sike"){
            $("#changJiaInfo-2").text("选择厂家为：思科");
        }
         if(str=="h3c"){
            $("#changJiaInfo-2").text("选择厂家为：华三");
        }
         if(str=="dipu"){
            $("#changJiaInfo-2").text("选择厂家为：迪普");
        }
         if(str=="beier"){
            $("#changJiaInfo-2").text("选择厂家为：贝尔");
        }
    }

    function setNext() {
           if(nextInfo[1]=="huawei"){
                     setdropdown(parseInt(nextInfo[0]),hwgmk);
                 }
           if(nextInfo[1]=="sike"){
                     setdropdown(parseInt(nextInfo[0]),skgmk);
                 }
           if(nextInfo[1]=="h3c"){
                     setdropdown(parseInt(nextInfo[0]),h3gmk);
                 }
           if(nextInfo[1]=="dipu"){
                     setdropdown(parseInt(nextInfo[0]),dpgmk);
                 }
           if(nextInfo[1]=="beier"){
                     setdropdown(parseInt(nextInfo[0]),brgmk);
                 }
    }
    function setNext2() {
           if(nextInfo[1]=="huawei"){
                     setdropdown2(parseInt(nextInfo[0]),hwgmk);
                 }
           if(nextInfo[1]=="sike"){
                     setdropdown2(parseInt(nextInfo[0]),skgmk);
                 }
           if(nextInfo[1]=="h3c"){
                     setdropdown2(parseInt(nextInfo[0]),h3gmk);
                 }
           if(nextInfo[1]=="dipu"){
                     setdropdown2(parseInt(nextInfo[0]),dpgmk);
                 }
           if(nextInfo[1]=="beier"){
                     setdropdown2(parseInt(nextInfo[0]),brgmk);
                 }
    }

    function getCJinfo(str) {
        if(str=="选择厂家为：华为"){
           return "huawei";
        }
         if(str=="选择厂家为：思科"){
           return "sike";
        }
         if(str=="选择厂家为：华三"){
           return "h3c";
        }
         if(str=="选择厂家为：迪普"){
           return "dipu";
        }
         if(str=="选择厂家为：贝尔"){
           return "beier";
        }

    }

    function getXh(str) {
            str=str.split(":");
            return str[1];
    }
    function toCache(op_type,op_net,item_ID,op_reason) {
        var data = {};
        var email =$.cookie('email');
        data["email"] = email;
        data["type"] = op_type;
        data["item"] = op_net;
        data["id"] = item_ID;
        data["reason"] = op_reason;
         $.ajax({
         type : "get",
         url : "cache/up",
         data : data,
         async : true,
         success : function(ret){
                    alert(ret["info"])
                }
            });
    }

    }
    );
