const $head = $('header');
const $divRedHead = $('dev#red_header');

$divRedHead.on('click', function () {
  $head.css('color', '#FF0000');
});
