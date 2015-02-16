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
        $('<div class="imageSetInfo">' +
        'Start :' + data[i]['start'] +
        '<br>' +
        'Stop :' + data[i]['stop'] +
        '<br>' +
        'FocusedApp : ' + data[i]['focusedApp'] +
        '<br>' +
        'Acceptable : ' + data[i]['acceptable'] +
        '<br>' +
        'Texte :<textarea> ' + data[i]['OCRedText'] + "</textarea>" +
        '</div>').appendTo('#previewerInfo')
    }
}