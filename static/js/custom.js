$(document).ready(function( $ ){
    $('.hamburger').click(function(){
      $(this).toggleClass('is-active');
      $('.cusdashboard').toggleClass('hideSidebar');
    });
});

