    
$('.banner-slider').owlCarousel({
    loop: true,
    margin: 10,
    nav:false,
    dot:true,
    autoplay:true,
    autoplayTimeout: 5000,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
})


$('.sup-deal').owlCarousel({
    loop: true,
    margin: 10,
    nav:true,
    dot:false,
    autoplay:true,
    autoplayTimeout: 5000,
    responsive: {
        0: {
            items: 2
        },
        600: {
            items: 3
        },
        1000: {
            items: 5
        }
    }
})

$('.mb-ls1').owlCarousel({
    loop: true,
    margin: 10,
    nav:false,
    dot:false,
    autoplay:true,
    autoplayTimeout: 5000,
    responsive: {
        0: {
            items: 2
        },
        600: {
            items: 3
        },
        1000: {
            items: 5
        }
    }
})

$('.mb-ls2').owlCarousel({
    loop: true,
    margin: 10,
    nav:false,
    dot:false,
    autoplay:true,
    autoplayTimeout: 5000,
    responsive: {
        0: {
            items: 2
        },
        600: {
            items: 3
        },
        1000: {
            items: 5
        }
    }
})

$('.mb-ls3').owlCarousel({
    loop: true,
    margin: 10,
    nav:false,
    dot:false,
    autoplay:true,
    autoplayTimeout: 5000,
    responsive: {
        0: {
            items: 2
        },
        600: {
            items: 3
        },
        1000: {
            items: 5
        }
    }
})


$('.it-lst1').owlCarousel({
    loop: true,
    margin: 0,
    nav:true,
    dot:false,
    autoplay:true,
    autoplayTimeout: 5000,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
})

$('.it-lst2').owlCarousel({
    loop: true,
    margin: 0,
    nav:true,
    dot:false,
    autoplay:true,
    autoplayTimeout: 5000,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
})

$('.it-lst3').owlCarousel({
    loop: true,
    margin: 0,
    nav:true,
    dot:false,
    autoplay:true,
    autoplayTimeout: 5000,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
})



 $('.slider-for').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: true,
  fade: true,
  asNavFor: '.slider-nav',
  // autoplay: true,
  // autoplaySpeed: 2000,

});


$('.slider-nav').slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  asNavFor: '.slider-for',
  dots: false,
  arrows: true,
  centerMode: true,
  focusOnSelect: true,
  // autoplay: true,
  // autoplaySpeed: 2000,
});
    
$(function() {
   $(".colors").click(function() {
      // remove classes from all
      $(".colors").removeClass("active");
      // add class to the one we clicked
      $(this).addClass("active");
   });
});



var progressBarOptions = {
    startAngle: -1.55,
    size: 200,
    value: 0.75,
    fill: {
        color: '#ffa500'
    }
}

$('.circle').circleProgress(progressBarOptions).on('circle-animation-progress', function(event, progress, stepValue) {
    $(this).find('strong').text(String(stepValue.toFixed(2)).substr(1));
});

$('#circle-b').circleProgress({
    value : 0.25,
    fill: {
        color: '#FF0000'
    }
});

$('#circle-c').circleProgress({
    value : 0.92,
    fill: {
        color: '#008000'
    }
});