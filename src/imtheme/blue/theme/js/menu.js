function myFunction() {
  var x = document.getElementById("portal-globalnav");
  if (x.className === "supermenu") {
    x.className += " responsive";
  } else {
    x.className = "supermenu";
  }
}

// split menu list in two list
// $(document).ready(function(){
//   $('#portal-globalnav').filter('ul').each(function() {
//     var $li = $(this).children(),
//         $newUl = $('<ul>').insertAfter(this),
//         middle = $li.length - 4;
//     $li.filter(':gt(' + middle + ')').appendTo($newUl);
//     $newUl.addClass("supermenu");
//   });
// });
