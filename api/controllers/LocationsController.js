/**
 * LocationsController
 *
 * @description :: Server-side logic for managing locations
 * @help        :: See http://links.sailsjs.org/docs/controllers
 */

module.exports = {
  getLocations:function(req,res){
    Locations.getAll(req,res);
  },
  saveLocation:function(req,res){
    var params = req.params.all();
    Locations.save(params,res);
  },
  updateLocation:function(req,res){
    var params = req.params.all();
    Locations.updateLocation(params,res);
  },
  removeLocation:function(req,res){
   var params = req.params.all();
   Locations.removeLocation(params,res);
  }
};

module.exports.blueprints = {
    actions: true,
    rest: true,
    shortcuts: true
};