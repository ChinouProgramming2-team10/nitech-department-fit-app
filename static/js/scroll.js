$(document).ready(function () {
    $(".hidden-footer").hide();
});
$(window).on('scroll', function(){
    var docHeight = $(document).innerHeight(),
        windowHeight = $(window).innerHeight(),
        pageBottom = docHeight - windowHeight; 
    if(pageBottom <= $(window).scrollTop() + 10) {
        //ウィンドウの一番下までスクロールした時に実行
        // console.log("bottom");
        $(".hidden-footer").show();
    }
    else {
        // console.log("other");
        $(".hidden-footer").hide();
    }
});