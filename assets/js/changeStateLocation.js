/*$("#locationsKnown").click(function() {
  //$( ".target" ).change();
  var test = $(this).children();
  alert(test);
});*/
$("#locationsKnown").children('input').change(function (){
  $.post(
      '/locations/updateState',
      {id:$(this).val(),isprivate:this.checked,name:this.name},
      function () {
	  alert("OK");
      }
  ).fail(function(res){
      alert("Error: " + res.getResponseHeader("error"));
  });			       
});