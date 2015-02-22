/**
 * Created by maxime on 16/02/15.
 */


function removeAllInfos()
{
    $("#previewerInfo").empty();
}

function printAllInfos(data)
{
    for(var i=0; i<data.length; i++)
    {
        if(data[i]['acceptable'] == true)
            cls = "acceptable";
        else
            cls = "unacceptable";

        startTime = dateParser(data[i]['startTime']);
        stopTime = dateParser(data[i]['stopTime']);


        $('<div class="oneInfo '+cls+'">' +
        'From : ' + startTime + " to "+ stopTime +
        '<br>' +
        'Foreground app : ' + data[i]['focusedApp'] +
        '<br>' +
        'Location : ' + data[i]['locationName'] +
        '<br>' +
        'Filtred by : ' + data[i]['filtredBy'] +
        '<br>' +
        '<textarea> ' + data[i]['OCRedText'] + "</textarea>" +
        '<div id="delete_'+data[i]['start'].split(".")[0]+'">' +
        '<input type="button" value="delete" onClick=\'confirmClean("'+data[i]['start']+'","'+data[i]['stop']+'", "'+startTime+'", "'+stopTime+'");\' >' +
        '</div>'+
        '</div>').appendTo('#previewerInfo')
    }
}


function dateParser(input)
{
    splited = input.split(" ");
    time = splited[1];
    date = splited[0];
    splitedDate = date.split("-");
    splitedTime = time.split(":");

    microsec = splitedTime[2].split(".")[1];
    sec = splitedTime[2].split(".")[0];
    min = splitedTime[1];
    hour = splitedTime[0];
    day = splitedDate[2];
    month = splitedDate[1];
    year = splitedDate[0];

    return month+"-"+day+"-"+year+" at "+hour+"h"+min+"min"+sec+"s"
}


function confirmClean(start, stop, startTime, stopTime)
{
    if(confirm("Do you really want to delete all data from "+ startTime + " to "+ stopTime + " ?"))
        jajaxCleaner(start, stop);
}

function jajaxCleaner(startImg, stopImg)
{

    $.get('/clean', {start : startImg, stop: stopImg}, function(data){
        cleanDone(startImg);
    }).fail(function(){
        cleanFail(startImg);
    })

    waitCleaning(startImg);

}

function cleanDone(start)
{
    $("#delete_"+start.split(".")[0]).empty();
    $("#delete_"+start.split(".")[0]).append("Deleted content. Will not appear next session.");
}

function cleanFail(start)
{
    $("#delete_"+start.split(".")[0]).empty();
    $("#delete_"+start.split(".")[0]).append("Error durring deleting. Sorry for that.");
}

function waitCleaning(start)
{
    $("#delete_"+start.split(".")[0]).empty();
    $("#delete_"+start.split(".")[0]).append("<img src='/images/loader_delete.gif'>");
}
