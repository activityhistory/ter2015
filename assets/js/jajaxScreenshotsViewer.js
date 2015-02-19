/**
 * Created by maxime on 04/02/15.
 */



function previousSCSs(nb)
{
    var firstImageSrc = $(".swiper-slide.blue-slide:first").find("img")[0].src;

    //cleaning the path
    var firstmage = firstImageSrc.split("/");
    firstmage = firstmage[firstmage.length -1];

    emptySmartScrollBar();
    removeAllInfos();
    jajaxSCSImages(nb, firstmage, true);
}

function nextSCSs(nb)
{
    var lastImageSrc = $(".swiper-slide.blue-slide:last").find("img")[0].src;

    //cleaning the path
    var lastImage = lastImageSrc.split("/");
    lastImage = lastImage[lastImage.length -1];

    emptySmartScrollBar();
    removeAllInfos();
    jajaxSCSImages(nb, lastImage, false);
}


function jajaxSCSImages(nb, off, negativeQ)
{
    $.get('/selectSCS', {nombre : nb, offset: off, negative: negativeQ}, function(data){
        MAJSCS(data["liste"]);
    });
}

//met aussi a jour ce qui est supp !!
function MAJSCS(newSCSList)
{
    var SCScontener = document.getElementById("swiper-wrapper");

    deleteAllSCS();

    for(var key in newSCSList)
    {
        //creation
        var newDivImage = document.createElement("div");
        var newImage = document.createElement("img");
        //cfg
        newDivImage.className = "swiper-slide blue-slide";
        newImage.src="/images/screens/"+newSCSList[key];
        //insertion
        newDivImage.appendChild(newImage);
        SCScontener.appendChild(newDivImage);
    }

}

function deleteAllSCS()
{
    document.getElementById("swiper-wrapper").innerHTML = "";
}
