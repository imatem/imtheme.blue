$(document).ready(function(){
    $(".tab").click(function(){
        $(".new-widget > div").hide();
        $('#tab'+this.id).show();
        $(".tab").removeClass("active-tab");
        $(this).addClass("active-tab");
    });
    $(".tab:first").click();

    // carrusel proximas actividades
    var carrusel_index = 0;
    showcarrusel();

    function showcarrusel() {
      var i;
      var slides = $("#galleria > a");
      slides.hide();
      carrusel_index++;
      if (carrusel_index > slides.length) {
        carrusel_index = 1;
      }
      slides[carrusel_index-1].style.display = "unset";
      setTimeout(showcarrusel, 8000); // Change image every x seconds
    }

});
