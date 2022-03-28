const toggle = document.querySelector(".toggle");
const menu = document.querySelector(".supermenu");
const items = document.querySelectorAll('[id$="-level1"]');

/* Toggle mobile menu */
function toggleMenu() {
  if (menu.classList.contains("active")) {
    menu.classList.remove("active");
    toggle.querySelector("a").innerHTML = "<i class='fa fa-bars'> <span class='text-menu'>Menú</span></i>";
  } else {
    menu.classList.add("active");
    toggle.querySelector("a").innerHTML = "<i class='fa fa-times'> <span class='text-menu'>Menú</span></i>";
  }
}

/* Event Listeners */
toggle.addEventListener("click", toggleMenu, false);

$('.supermenu a').on('click','.nav-plus',function(){
  if($(this).hasClass('nav-minus') == false){
      $(this).parent('a').parent('li').find('> ul').addClass("submenu-active");
      $(this).addClass('nav-minus');
    }else{
      $(this).parent('a').parent('li').find('> ul').removeClass("submenu-active");
      $(this).removeClass('nav-minus');
  }
  return false;
});
