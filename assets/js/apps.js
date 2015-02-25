$( document ).ready(function (){
 getApps();
});

function getApps(){
 $.get('/apps', function(data){
      $("#apps").html(data);
  }); 
}

function resetForm () {
  $(':input','#addAppForm')
   .not(':button, :submit, :reset, :hidden')
   .val('')
   .removeAttr('checked')
   .removeAttr('selected');
}

function saveApp(){
    var name = $('#appNameField').val();
    if(name.length > 0){
        $("#addAppErr").removeClass("divErr");
        $("#addAppErr").html("");
        data = {name:name};
        $.post('/apps/add', data, function(res){
            getApps();
            resetForm();
        });
    }
    else{
        $("#addAppErr").addClass("divErr");
        $("#addAppErr").html("Error, please fill all fields");
    }
}

function appsChangeState(){
    $("#appsList").children('input').change(function (){
    if(this.checked)
      var isprivate = 1;
    else
      var isprivate = 0;

        console.log(this.value);
    if(this.name.length === 0){
        console.log("VALUE"+this.value);
    }
    $.post(
	'/apps/updateState',
	{id:$(this).val(),isprivate:isprivate,name:this.name},
	function () {
	  getApps();
	}
    ).fail(function(){
	console.log('Error when try to update app state');
    });			       
  });
}

/*function removeApp(id){
    $.post('/apps/remove',{id:id},function(){
      getApps();
    }).fail(function(){
      console.log('Error when try to delete app');
    });
}*/