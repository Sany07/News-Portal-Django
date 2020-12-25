$(function () {
    'use strict';
    // --------------------------------------------------------------------
    // PreLoader
    // --------------------------------------------------------------------
    (function () {
        $('#preloader').delay(200).fadeOut('slow');
    }());
    // --------------------------------------------------------------------
    // One Page Navigation
    // --------------------------------------------------------------------
    (function () {
        $(window).scroll(function () {
            if ($(this).scrollTop() >= 50) {
                $('nav.navbar').addClass('sticky-nav');
            }
            else {
                $('nav.navbar').removeClass('sticky-nav');
            }
        });
    }());
    // --------------------------------------------------------------------
    // jQuery for page scrolling feature - requires jQuery Easing plugin
    // --------------------------------------------------------------------
    (function () {
        $('a.page-scroll').on('click', function (e) {
            e.preventDefault();
            var $anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top
            }, 1500, 'easeInOutExpo');
        });
    }());
    // -------------------------------------------------------------
    // mobile menu
    // -------------------------------------------------------------
    (function () {
        $('button.navbar-toggle').ucOffCanvasMenu({
            documentWrapper: '#main-wrapper'
            , contentWrapper: '.content-wrapper'
            , position: 'uc-offcanvas-left', // class name
            // opener         : 'st-menu-open',            // class name
            effect: 'slide-along', // class name
            closeButton: '#uc-mobile-menu-close-btn'
            , menuWrapper: '.uc-mobile-menu', // class name below-pusher
            documentPusher: '.uc-mobile-menu-pusher'
        });
    }());
    // -------------------------------------------------------------
    // top scrolling
    // -------------------------------------------------------------
    (function () {
        var offset = 220;
        var duration = 500;
        jQuery(window).scroll(function () {
            if (jQuery(this).scrollTop() > offset) {
                jQuery('.crunchify-top').fadeIn(duration);
            }
            else {
                jQuery('.crunchify-top').fadeOut(duration);
            }
        });
        jQuery('.crunchify-top').click(function (event) {
            event.preventDefault();
            jQuery('html, body').animate({
                scrollTop: 0
            }, duration);
            return false;
        });
    }());
    // --------------------------------------------------------------------
    // Search
    // --------------------------------------------------------------------
    $("#search-button, #search-icon").click(function (e) {
        e.preventDefault();
        $("#search-button, #search-form").toggle();
    });
    // --------------------------------------------------------------------
    // Carousel slider for blog page
    // --------------------------------------------------------------------
    $("#feature-news-carousel").owlCarousel({
        loop: true
        , dots: false
        , items: 1
        , autoplay: true
        , singleItem: true
            // "singleItem:true" is a shortcut for:
            // items : 1,
            // itemsDesktop : false,
            // itemsDesktopSmall : false,
            // itemsTablet: false,
            // itemsMobile : false
    });
});
// JQuery end
$(document).on('click', '.m-menu .dropdown-menu', function (e) {
    e.stopPropagation()
})

$('#shareBlock').cShare({
    data: {
      fb: {
        fa: 'fab fa-facebook-f',
        name: 'Fb',
        href: (url) => {
          return `https://www.facebook.com/sharer.php?u=${url}`
        },
        show: true
      },
      line: {
        fa: 'fab fa-line fa-2x',
        name: 'Line',
        href: (url) => {
          return `https://social-plugins.line.me/lineit/share?url=${url}`
        },
        show: true,
        hideWrapper: true
      },
      plurk: {
        fa: 'fa-plurk',
        name: 'Plurk',
        href: (url, description) => {
          return `http://www.plurk.com/?qualifier=shares&status=${description} ${url}`
        },
        show: false
      },
      weibo: {
        fa: 'fab fa-weibo',
        name: '微博',
        href: (url, description) => {
          return `http://service.weibo.com/share/share.php?title=${description}&url=${url}`
        },
        show: false
      },
      twitter: {
        fa: 'fab fa-twitter',
        name: 'Twitter',
        href: (url, description) => {
          return `https://twitter.com/intent/tweet?original_referer=${url}&url=${url}&text=${description}`
        },
        show: false
      },
      tumblr: {
        fa: 'fab fa-tumblr',
        name: 'Tumblr',
        href: (url, description) => {
          return `http://www.tumblr.com/share/link?name=${description} ${url}&url=${url}`
        },
        show: false
      },
      email: {
        fa: 'fas fa-envelope',
        name: 'E-mail',
        href: (url, description) => {
          return `mailto:?subject=${description}&body=${description} ${url}`
        },
        show: false
      }
    },
  });