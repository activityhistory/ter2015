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

    data = {name:name};
    $.post('/apps/add', data, function(res){
      getApps();
      resetForm();
    }); 
}

function appsChangeState(){
    $("#appsList").children('input').change(function (){
    if(this.checked)
      var isprivate = 1;
    else
      var isprivate = 0;
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