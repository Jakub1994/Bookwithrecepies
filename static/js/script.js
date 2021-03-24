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

  $('#recipe_name, #preparation_time, #difficulty_level, #short_describe, #ingredients, #step_1_of_preparation, #step_2, #step_3').val('');
  M.textareaAutoResize($('#recipe_name, #preparation_time, #difficulty_level, #short_describe, #ingredients, #step_1_of_preparation, #step_2, #step_3'));

   document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, {});
  });