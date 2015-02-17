$( document ).ready(function (){
 getKeywords();
});

function getKeywords(){
 $.get('/keywords', function(data){
      $("#keywords").html(data);
  }); 
}