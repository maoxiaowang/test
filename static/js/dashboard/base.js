// nav side
$(function () {

   var $navCollapse = $('#nav-side .collapsible');
   var relUrl = getRelativeUrl();
   if (relUrl.split('/').length === 4) {
       var $accordionItems = $navCollapse.find('div.collapsible-body');
       $.each($accordionItems.find('a'), function (i, item) {
           var $item = getJQueryObject(item);
           if (relUrl.indexOf($item.attr('href')) === 0) {
               // $item.parent().parent().parent().slideDown(
               //     { duration: 350, easing: "easeInOutCubic", queue: false, complete: function () {
               //         $(this).css('height', '');}});
               $item.parent().parent().parent().slideDown(350, function () {
                   $(this).css('height', '');
               });
               $item.parent().parent().parent().css('display', 'block');
               $item.parent().addClass('active');
               $item.parent().parent().parent().prev('a').addClass('active');
               $item.parent().parent().parent().parent().addClass('active');
           }
       });
   } else {
       $.each($navCollapse.find('> li > a[href]'), function (i, item) {
           var $item = getJQueryObject(item);
           console.log($item.attr('href'));
           console.log(relUrl);
           if ($item.attr('href') === relUrl) {
               $item.css('color', '#fff');
               $item.parent().addClass('active').css({'background-color': '#ee6e73'});
           }
       });

   }

    // For mobile nav initialization
    $(".button-collapse").sidenav();
    $('.collapsible').collapsible();
});
