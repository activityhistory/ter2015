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
    res.view('ScreenshotsPrivacyFilterPreviewer', {nbSCS:5, offset:"150129-190317044212_540_672.jpg", layout: null})
  },


  select: function(req, res) {
    console.log(require('path').dirname(require.main.filename));
    var nombre = req.query.nombre;
    var offset = req.query.offset;
    var lst = walkSync("assets/images/screens/");
    lst.sort();
    lst = selectSCS(lst, nombre, offset);
    res.json({liste : lst, layout: null});
  },

  getFiltredList: function(req, res ){

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
    shell.on('message', function(message){
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
var walkSync = function(dir, filelist) {
  var fs = fs || require('fs'),
    files = fs.readdirSync(dir);
  filelist = filelist || [];
  files.forEach(function(file) {
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
function getOneDayScreensList(allSCSList, pathDay)
{
  var listDay = new Array();
  for(var i = 0; allSCSList[i]; i++)
  {
    if(allSCSList[i].search(pathDay) != -1)
      listDay.push(allSCSList[i]);
  }
  return listDay;
}

/**
 * Return nb screens,
 * started by offset wich is the name of the first SCS that you don't want to have
 */
function selectSCS(list, nb, offset)
{
  var selectedList = new Array();
  var start = false;
  for(var i = 0; list[i] && nb != 0; i++)
  {
    if(start) {
      selectedList.push(list[i]);
      nb--;
    }
    else
    if(list[i] == offset)
      start = true;
  }
  return selectedList;

}

