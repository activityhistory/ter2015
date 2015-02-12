/**
 * Created by maxime on 04/02/15.
 */



function previousSCSs(nb)
{
    alert("Heuu, je calcule comment l'offset moi ??");
    emptySmartScrollBar();
}

function nextSCSs(nb)
{
    var lastImageSrc = $(".swiper-slide.blue-slide:last").find("img")[0].src;

    //cleaning the path
    var lastImage = lastImageSrc.split("/");
    lastImage = lastImage[lastImage.length -1];

    emptySmartScrollBar();
    jajaxSCSImages(nb, lastImage);
}


function jajaxSCSImages(nb, off)
{
    $.get('/selectSCS', {nombre : nb, offset: off}, function(data){
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
