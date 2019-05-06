$(document).ready(function() {
    $("#uS1").click(function () {

         $("#uS2").css("color","#6c757d");
         $("#uS3").css("color","#6c757d");
        $("#uS1").css("color","#c80000");
        $("#titleUs").text("关于我们")
    })
     $("#uS2").click(function () {
        $("#uS1").css("color","#6c757d");
         $("#uS3").css("color","#6c757d");
        $("#uS2").css("color","#c80000");
        $("#titleUs").text("团队介绍")
    })
     $("#uS3").click(function () {
          $("#uS2").css("color","#6c757d");
         $("#uS1").css("color","#6c757d");
        $("#uS3").css("color","#c80000");
        $("#titleUs").text("联系我们")
    })
});