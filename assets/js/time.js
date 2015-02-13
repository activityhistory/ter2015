$( document ).ready(function (){
 getTimes();
});

function resetForm () {
  $(':input','#addTime')
   .not(':button, :submit, :reset, :hidden')
   .val('')
   .removeAttr('checked')
   .removeAttr('selected');
}

function getTimes(){
 $.get('/time', function(data){
      $("#time").html(data);
  }); 
}

function saveTime(){
    var week =$('#week').is(':checked');
    var weekEnd = $('#weekEnd').is(':checked');
    var fromHour = $('#hourStart').val();
    var toHour = $('#hourStop').val();
    
    if(!week && !weekEnd){
	$('#timeError').html('Please select days');
    }
    else{
	if(week)
	  week = 1;
	else
	  week = 0;
	
	if(weekEnd)
	  weekEnd = 1;
	else
	  weekEnd = 0;
	
	data = {week:week, weekEnd:weekEnd,hourStart:fromHour,hourStop:toHour};
	$.post('/time', data, function(res){
	  getTimes();
	  resetForm();
	});
    }
}