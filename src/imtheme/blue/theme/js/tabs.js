let carrusel_index = 1;

function showcarruselPlus(n) {
  carrusel_index += n
  let slides = $("#galleria > a");
  slides.hide();

  if (carrusel_index > slides.length) {carrusel_index = 1}
  if (carrusel_index < 1) {carrusel_index = slides.length}

  slides[carrusel_index-1].style.display = "unset";
}

function showcarrusel() {
  let slides = $("#galleria > a");
  slides.hide();
  carrusel_index++;
  if (carrusel_index > slides.length) {carrusel_index = 1;}
  slides[carrusel_index-1].style.display = "unset";
  setTimeout(showcarrusel, 6000); // Change image every x seconds
};

$(document).ready(function(){
    $(".tab").click(function(){
        $(".new-widget > div").hide();
        $('#tab'+this.id).show();
        $(".tab").removeClass("active-tab");
        $(this).addClass("active-tab");
    });
    $(".tab:first").click();

    showcarrusel();

}); 
