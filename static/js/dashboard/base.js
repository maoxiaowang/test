// nav side
$(function () {
   var $navSide = $('#nav-side');
   var $accordionItems = $navSide.find('div.collapsible-body');
   console.log($accordionItems);
   $.each($accordionItems.find('a'), function (i, item) {
       var $item = getJQueryObject(item);
       if (getRelativeUrl().indexOf($item.attr('href')) === 0) {
           $item.parent().parent().parent().slideDown(
               { duration: 350, easing: "easeOutQuart", queue: false, complete: function () {
                   $(this).css('height', '');}});
           // $item.parent().parent().parent().css('display', 'block');
           $item.parent().addClass('active');
           $item.parent().parent().parent().prev('a').addClass('active');
           $item.parent().parent().parent().parent().addClass('active');
       }
   });

    // For mobile nav initialization
    $(".button-collapse").sidenav();
    $('.collapsible').collapsible();
});
