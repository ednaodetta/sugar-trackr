$(document).ready(function(){
  $('.post-wrapper').slick({
      slidesToShow: 3,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 3000,
      prevArrow: $('.prev'),
      nextArrow: $('.next'),
      dots: true,
      responsive: [
        {
          breakpoint: 1200,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
      ]
  });
  
  // Add animation on scroll
  $(window).scroll(function() {
      $('.card, .post').each(function() {
          var position = $(this).offset().top;
          var scroll = $(window).scrollTop();
          var windowHeight = $(window).height();
          
          if (scroll > position - windowHeight + 200) {
              $(this).addClass('visible');
          }
      });
  });
});