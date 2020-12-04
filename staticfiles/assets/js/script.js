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