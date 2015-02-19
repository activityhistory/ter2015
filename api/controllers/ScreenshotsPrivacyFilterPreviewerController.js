/**
 * ScreenshotsPrivacyFilterPreviewerController
 *
 * @description :: Server-side logic for managing Screenshotsprivacyfilterpreviewers
 * @help        :: See http://links.sailsjs.org/docs/controllers
 */

module.exports = {


    /**
     * `ScreenshotsPrivacyFilterPreviewerController.show()`
     * Show the page with the screenshots slider, and the smartslider wich higlight filtred screenshots
     */
    show: function (req, res) {
        //TODO : define the first offset
        res.view('ScreenshotsPrivacyFilterPreviewer', {
            nbSCS: 15,
            offset: "150129-190317044212_540_672.jpg",
            layout: null
        })
    },


    select: function (req, res) {
        console.log(require('path').dirname(require.main.filename));
        var nombre = req.query.nombre;
        var offset = req.query.offset;
        var negative = req.query.negative;

        console.log("nombre : " + nombre + " offset :" + offset + " negative : " + negative);
        //return;

        var lst = walkSync("assets/images/screens/");
        lst.sort();
        lst = selectSCS(lst, nombre, offset, negative);
        res.json({liste: lst, layout: null});
    },

    getFiltredList: function (req, res) {

        var PythonShell = require("python-shell");
        var path = require("path");

        var start = req.query.start;
        var stop = req.query.stop;
        var options = {
            mode: 'json',
            scriptPath: "assets/python/",
            args: [start, stop]
        };
        var shell = new PythonShell('test.py', options);
        shell.on('message', function (message) {
            res.json(message);
        });
    }


};

/**
 *
 * @param dir
 * @param filelist
 * @returns {*|Array}
 */
var walkSync = function (dir, filelist) {
    var fs = fs || require('fs'),
        files = fs.readdirSync(dir);
    filelist = filelist || [];
    files.forEach(function (file) {
        if (fs.statSync(dir + file).isDirectory()) {
            filelist = walkSync(dir + file + '/', filelist);
        }
        else {
            filelist.push(file);
        }
    });
    return filelist;
};

/**
 * Filter a list of SCS names by a date  : YYMMDD
 * return only the SCS wich math with this date
 //TODO: Filter by regex, in case of milliseconds match the date
 */
function getOneDayScreensList(allSCSList, pathDay) {
    var listDay = new Array();
    for (var i = 0; allSCSList[i]; i++) {
        if (allSCSList[i].search(pathDay) != -1)
            listDay.push(allSCSList[i]);
    }
    return listDay;
}



function getTheFirstTodaySCS(lst)
{
    return "150216-110235592918_1057_514.jpg";
}

/**
 * Return nb screens,
 * started by offset wich is the name of the first SCS that you don't want to have
 */
function selectSCS(list, nb, offset, negative) {
    var selectedList = new Array();
    list.sort();

    if(offset == "today")
        offset = getTheFirstTodaySCS(list);

    var i = findTheNearestSCS(list, offset, negative=="true");
    console.log("hi : "+i);
    if (negative == "true") {
        for (var k = nb; k != 0 && list[i]; k--, i--) {
            selectedList.push(list[i]);
        }
        selectedList.reverse();
    }
    else {
        for (var k = nb; k != 0 && list[i]; k--, i++) {
            selectedList.push(list[i]);
        }
    }
    return selectedList;

}

function findTheNearestSCS(list, scsBase, before)
{
    var i;
    for(i=0; list[i] && list[i] < scsBase; i++);
    if(before)
        return i-1;
    else
        return i >= 0 ? i : 0;
}
