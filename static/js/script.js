document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {edge: "right"});
  });
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems, {inDuration: "200"});
  });
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.tooltipped');
    var instances = M.Tooltip.init(elems, {enterDelay: "100"});
  });
  $(document).ready(function() {
    $('input#input_text, textarea#textarea2, textarea#textarea3, textarea#textarea4, textarea#textarea5, textarea#textarea6').characterCounter();
  });
  $('input#input_text, textarea#textarea2, textarea#textarea3, textarea#textarea4, textarea#textarea5, textarea#textarea6').val('');
  M.textareaAutoResize($('input#input_text, textarea#textarea2, textarea#textarea3, textarea#textarea4, textarea#textarea5, textarea#textarea6'));