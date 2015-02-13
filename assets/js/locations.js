$( document ).ready(function (){
 getLocations();
});

function getLocations(){
 $.get('/locations', function(data){
      $("#location").html(data);
  }); 
}


function resetForm () {
  $(':input','#newLocationForm')
   .not(':button, :submit, :reset, :hidden')
   .val('')
   .removeAttr('checked')
   .removeAttr('selected');
}

function saveLocation(){
    var name = $('#nameField').val();
    var address = $('#autocomplete').val();
    var longitude = $('#longitudeField').val();
    var latitude = $('#latitudeField').val();
    var isprivate = $('#privateField').is(':checked');
    
    if(isprivate)
      isprivate = 1;
    else
      isprivate = 0;

    data = {name:name,address:address,longitude:longitude,latitude:latitude,isprivate:isprivate};
    $.post('/locations', data, function(res){
      getLocations();
      resetForm();
    });
    
}

//TODO UpdateLocation