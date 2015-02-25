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

    if(name.length > 0 && address.length >= 0){
        $("#errAddLocation").html("");
        data = {name:name,address:address,longitude:longitude,latitude:latitude,isprivate:isprivate};
        $.post('/locations', data, function(res){
            console.log('FINI AJOUT');
            getLocations();
            resetForm();
        });
    }
    else{
        $("#errAddLocation").html("Error, please fill all fields");
    }
}

function locationChangeState(){
  $("#locationsKnown").children('input').change(function (){
    if(this.checked)
      var isprivate = 1;
    else
      var isprivate = 0;
    $.post(
	'/locations/updateState',
	{id:$(this).val(),isprivate:isprivate,name:this.name},
	function () {
	  getLocations();
	}
    ).fail(function(){
	console.log('Error when try to update location state');
    });			       
  });
}

function removeLocation(id){
    $.post('/locations/removeLocation',{id:id},function(){
      getLocations();
    }).fail(function(){
      console.log('Error when try to delete location');
    });
}
