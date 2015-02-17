/**
 * ScreenshotsPrivacyFilterPreviewerController
 *
 * @description :: Server-side logic for managing Screenshotsprivacyfilterpreviewers
 * @help        :: See http://links.sailsjs.org/docs/controllers
 */

module.exports = {
  getKeywords:function(req,res){
    Keywords.getAll(req,res);
  },
  saveKeyword: function(req,res){
    params = req.params.all();
    Keywords.save(params,res);
    Keywords.getAll(req,res);
  },
};

