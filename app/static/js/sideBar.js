/**
 * Created by yue on 11/2/16.
 */
$('#sidebar').affix({
    offset: {
        top: 235
    }
});

/* activate scrollspy menu */
var $body   = $(document.body);

$body.scrollspy({
    target: '#leftCol'
});

/* smooth scrolling sections */
$('a[href*=\\#]:not([href=\\#])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
        if (target.length) {
            $('html,body').animate({
                scrollTop: target.offset().top - 50
            }, 1000);
            return false;
        }
    }
});