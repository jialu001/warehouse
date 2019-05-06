$(document).ready(function(){
        //页面加载时触发

       var  tishi = {"分公司":"如：广州分公司","配件名称":"设备分类，如：A9K备件","规格型号":"设备型号","类型":"所属厂家：如思科"
        ,"sn码":"SN码","入库时间":"入库时间","入库地点":"入库地点，如太阳城","数量":"数量","货位号":"所在库房的位置",
        "所属网络":"如承载网","资产标签":"资产标签 可不填","备注":"其他信息"};
       var idset = ["fenggongsi","name","xinghao","leixing","sn","rukushijian","rukudidian",
            "shuliang","huoweihao","suoshuwangluo","zichanbiaoqian","beizhu"];
       //上传后台的iptoS
       var iptoS ={};
       var ajaxret = [];
       var retID ;
       var searchIsDisplay = 0;
        for(var key in tishi){
                 $("#SEARCH_DIV").append(
          "<div class='row' style='height: 7%;padding-top: 5px;border-width: medium;border-style:solid;border-color: #6c757d;border-radius: 6px;'> " +
               " <div class=\"col-4\"  style=''> "+key+"</div> " +
                " <div class=\"col-6\"style='' >" +
                      "<input class='myinp' type='text'  placeholder='"+tishi[key]+"' style='width: 90%'>"+" </div> " +
               " <div class=\"col-2\" style=''>" +
                      "<input class='checkbox' type='checkbox'  >"+"√"+" </div> " +
               "</div>"
      );
        }
         $("#SEARCH_DIV").append(
          "<div class='row ' style='height: 7%;'> " +
                    "<button type='button' class='btn' id='search_btn0' style='margin-left: 70%;'>搜索</button>" +
               "</div>");
        var test = 1

      $('#search_input0').keydown(function(e){
        if(e.keyCode==13){
            postFastQuery("search_input0");
        }
        });

        // Nor 搜索页面的搜索按钮
      $("#search_btn0").click(function(){
         var shuruku = document.getElementsByClassName("myinp");
         var checkres = document.getElementsByClassName("checkbox");
         console.log("准备获取输入框的相关参数");
         for(i=0;i<shuruku.length;i++){
              iptoS[idset[i]]=shuruku[i].value;
              var str =idset[i] + "ischecked" ;
              iptoS[str] = checkres[i].checked;
         }
         console.log("已获取输入框的相关参数，准备上传至服务器");
         iptoS["type"]="nor";

         //此处往json 加入用户email 信息
         var email =$.cookie('email');
         iptoS["email"] = email;

         console.log(iptoS);
         $.get("search-post", iptoS,
             function(ret,status){
             console.log("数据: \n" + ret + "\n状态: " + status);
             console.log(typeof(status));
             if(status=="success"){
                    var table = document.getElementById("myTable");
                    var i = 1;
                    var j = 0;
                 ret.forEach(function (item,index,array)
                 {


                     $("#main_1").css("height","auto");
                      $("#SEARCH_DIV").css("display","none");
                      searchIsDisplay = 1;
                      $("#close_search").text("显示搜索框");

                    var row = table.insertRow(i);
                        j=0;
                    for (var key in item) {
                        row.insertCell(j).innerHTML =item[key]  ;
                        j++;
                        }
                            i++;
                    }) //此处ret处理循环结束
                }
                 });
      });

      //显示页面的搜索按钮
      $("#query1").click(function () {
          postFastQuery("input1");
      })

      //入库的搜索按钮
      $("#query2").click(function () {
          postFastQuery("input2");
          hideMask();
          $("#out_info").css("display","none");
      })

        //入库的取消按钮
      $("#cancel2").click(function () {
             hideMask();
          $("#out_info").css("display","none");
      })

        //index页面快捷查询控制
      $("#formquery").click(function(){
            postFastQuery("search_input0");
      });

      $("#close_search").click(function () {
          if(searchIsDisplay==0){
               $("#SEARCH_DIV").css("display","none");
               $("#close_search").text("显示搜索框") ;
               searchIsDisplay = 1;
          }
          else if(searchIsDisplay==1){
               $("#SEARCH_DIV").css("display","block");
               $("#close_search").text("隐藏搜索框") ;
               searchIsDisplay = 0;
          }

      })

      // 为mytable中生成的button 绑定点击事件 ， 使能够弹出确认框
      $("#myTable").on("click","button",function () {
           var itemID = $(this).attr("value")-1;
           retID = itemID;
           var margintop = $(document).scrollTop()+100;
           item =(ajaxret[itemID]) ;
           var  str="" ;
            for (var key in item) {
                str =str+"<h4>"+item[key] +"</h4>";
            }
           $("#out2_item_info").html(str);
           showMask();
           $("#out2_info").css("display","block");
           $("#out2_info").css("margin-top",(margintop));
           console.log("距离顶部位置"+$(document).scrollTop());
      })

      // out2_info 的确认按钮
        $("#out_yes").click(function () {
           var itemID = $(this).attr("value")-1;
           var Oip = {};
           var email =$.cookie('email');
           Oip["email"] = email;
           var outUp =(ajaxret[retID]) ;
           outUp["email"] =email;
           console.log(outUp);
           hideMask();
           $("#out2_info").css("display","none");


           success();


      })
      // out2_info 的取消按钮
      $("#out_no").click(function () {
          hideMask();
           $("#out2_info").css("display","none");
      })



        // ip_name 输入框的值，以FAST方式将输入框的值上传到后台服务器
      function  postFastQuery(ip_name) {
           var data = {};
        var toolsname = $("#"+ip_name).val();
        data["toolsname"] = toolsname;
        data["type"] = "fast"   ;
        var email =$.cookie('email');
        data["email"] = email;
        var rownum = 0;
        var column_len = 15;
        var i = 1;
        var j = 0;
        //console.log(toolsname);


          $.ajax({
         type : "get",
         url : "search-post",
         data : data,
         async : true,
         success : function(ret){
             ajaxret =ret;

                 if(ret[0]=="error"){
                     alert("发生异常");
                     return;
                 }
                 if(ret[0]=="null"){
                     alert("无法检索到数据，请核实");
                     return;
                 }
                 $("#index_c1").css("display","none");
                 $("#search_row").css("display","none");
                 $("#main_3").css("display","inline");
                 var table = document.getElementById("myTable");
                 var rowNum=table.rows.length;
                    for (i=1;i<rowNum;i++)
                    {
                        table.deleteRow(i);
                        rowNum=rowNum-1;
                         i=i-1;
                     }
                 ret.forEach(function (item) {
                        if(i>6){
                        $("#main_1").css("height","auto");
                    }
                    var row = table.insertRow(i);
                    j=0;

                    for (var key in item) {

                        if(j==Object.keys(item).length-1){
                            var  str = i  ;
                            row.insertCell(j).innerHTML =item[key] +"   "+"<button type=\"button\" class='btn outbut' value="+str+" id='out_bt'>出库</button>" ;
                        }else {
                             row.insertCell(j).innerHTML =item[key]  ;
                        }
                    j++;
                    }
                    i++;
                 })
                }
            });


      }
      function hideMask(){

        $("#mask").hide();
    }
      function showMask(){
        $("#mask").css("height",$(document).height());
        $("#mask").css("width",$(document).width());
        $("#mask").show();
    }
      function success() {
          $("#dh_result").css("display","block");
           setTimeout(function(){
                         $("#dh_result").css("display","none");
                     },1000);
      }
    });
