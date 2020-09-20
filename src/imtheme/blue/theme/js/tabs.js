$(document).ready(function(){
    $(".tab").click(function(){
        $(".new-widget > div").hide();
        $('#tab'+this.id).show();
        $(".tab").removeClass("active-tab");
        $(this).addClass("active-tab");
    });
    $(".tab:first").click();
});
