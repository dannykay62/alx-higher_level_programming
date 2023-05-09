const $headerEl = $('header');
const $divRedHeader = $('div#red_header');

$divRedheader.on('click', function () {
  $headerEl.addClass('red');
});
