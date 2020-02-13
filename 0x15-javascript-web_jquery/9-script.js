const url = `https://fourtonfish.com/hellosalut/?lang=${document.documentElement.lang}`;
jQuery.getJSON(url, function(data){
    $('DIV#hello').text(data.hello);
});