let n = 0;
$('#add_item').click(function () {
  $('UL.my_list').append(`<li>item ${n}</li>`);
  n++;
});
