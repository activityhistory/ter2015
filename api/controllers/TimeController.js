/**
 * TimeController
 *
 * @description :: Server-side logic for managing times
 * @help        :: See http://links.sailsjs.org/docs/controllers
 */

module.exports = {
  show:function(req,res){
      Time.getAll(req,res);
  },
  saveTime:function(req,res){
    var params = req.params.all();
    Time.save(params,res); 
  },
  removeTime:function(req,res){
    var params = req.params.all();
    Time.remove(params,res);
  }
};

