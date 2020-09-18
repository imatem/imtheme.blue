$(document).ready(function(){
  // var newWidget="<div class='widget-wrapper'> <ul class='tab-wrapper'></ul> <div class='new-widget'></div></div>";
  var newWidget = $(".widget-wrapper")
  $(".widget").hide();
  $(".widget:first").before(newWidget);
  $(".widget > div").each(function(){
      // $(".tab-wrapper").append("<li class='tab'>"+this.id+"</li>");
      $(this).appendTo(".new-widget");
  });
  $(".tab").click(function(){
      $(".new-widget > div").hide();
      $('#tab'+$(this).id).show();
      $(".tab").removeClass("active-tab");
      $(this).addClass("active-tab");
  });
  $(".tab:first").click();
});
