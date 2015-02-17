/**
 * Created by maxime on 04/02/15.
 */


function MAJSmartScrollBar(redList)
{
    emptySmartScrollBar();
    fillSmartScrollBar(redList);
    unInvertImages();
    invertImages(redList);
}

function fillSmartScrollBar(redList)
{
    nbSCS = redList.length;
    var smartScrollBarDiv = document.getElementById("smartScrollBar");
    for(var i=0; i!= nbSCS;i++) //Add the good number of images block
    {
        var newBlockImage = document.createElement("div");
        newBlockImage.className = "imageBlock";
        if(redList[i] == 1) //Image should be red
            newBlockImage.className += " redImageBlock";
        else
            newBlockImage.className += " blueImageBlock";
        smartScrollBarDiv.appendChild(newBlockImage);
    }
}

function emptySmartScrollBar()
{
    document.getElementById("smartScrollBar").innerHTML = "";
}

function invertImages(redList)
{
    var slidesWrapper = document.getElementById("swiper-wrapper");
    var _slides = slidesWrapper.getElementsByTagName('div');
    for(var k = 0; _slides[k]; k++)
    {
        if(redList[k] == 1)
            _slides[k].getElementsByTagName('img')[0].className = "imageInvert";
    }
}

function unInvertImages()
{
    var slidesWrapper = document.getElementById("swiper-wrapper");
    var _slides = slidesWrapper.getElementsByTagName('div');
    for(var k = 0; _slides[k]; k++)
    {
            _slides[k].getElementsByTagName('img')[0].className = "";
    }
}


/**
 * ************************ JAJAX *******************************
 * **/

function jajaxSmartScrollBar()
{

    var lastImageSrc = $(".swiper-slide.blue-slide:last").find("img")[0].src;

    //cleaning the path
    var lastImage = lastImageSrc.split("/");
    lastImage = lastImage[lastImage.length -1];

    var firstImageSrc = $(".swiper-slide.blue-slide").find("img")[0].src;

    //cleaning the path again
    var firstImage = firstImageSrc.split("/");
    firstImage = firstImage[firstImage.length -1];

    $.get('/getFiltredList', {start : firstImage, stop: lastImage}, function(data){
        //TODO : remanier la façon de recevoir et traiter l'info !
        removeAllInfos();
        printAllInfos(data);
        //Make a JS table from data
        var redTable = [];
        for(var key in data)
        {
            for(var i =0; i != data[key]['length']; i++)
            {
                if(data[key]['acceptable'] == true)
                    redTable.push(0);
                else
                    redTable.push(1);
            }
        }
        console.log(redTable);
        MAJSmartScrollBar(redTable);
        hidePleaseWait();
    }).fail(function(){
        $("#errorTimeOut").show();
        hidePleaseWait();
    })

    printPleaseWait();
    $("errorTimeOut").hide();
}

function printPleaseWait()
{
    $("#majSpan").empty();
    $("#majSpan").append("<img src='/images/ajax-loader.gif'>");
}

function hidePleaseWait()
{
    $("#majSpan").empty();
    $("#majSpan").append("<input id='majButton' type='button' onClick='jajaxSmartScrollBar()' value='Preview'/>");
}
