/**
 * ApplicationsController
 *
 * @description :: Server-side logic for managing applications
 * @help        :: See http://links.sailsjs.org/docs/controllers
 */

module.exports = {
  getApps: function(req,res){
    Applications.getAll(req,res);
  },
  changeState:function(req,res){
    var params = req.params.all();
    Applications.changeState(params,res);
  },
  remove:function(req,res){
    var params = req.params.all();
    Applications.remove(params,res);
  },
    addApp:function(req,res){
    var params = req.params.all();
    Applications.add(params,res);
  }

};

