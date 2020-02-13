$('DIV#toggle_header').click(function() {
    className = $("header").attr('class');
    if(className === 'green') {
        $('header').removeClass("green");
        $('header').addClass("red");
    } if(className === 'red') {
        $('header').removeClass("red");
        $('header').addClass("green");
    }
});