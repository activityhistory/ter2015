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
    if(params.isprivate === 'on'){
      params.isprivate = 1;
    }
    else{
      params.isprivate = 0;
    }
    var found = null;
    Locations.getLocation(params,found);
    if(found === null || found.length <=0){
      Locations.save(params,res);
    }
    else if(found[0].address === params.address){
      res.status(200).send('Location already registered');
    }
    else{
      res.status(200).send('Location name already registered ');
    }
    
  },
  updateLocation:function(req,res){
    var params = req.params.all();
    Locations.updateLocation(params,res);
  }
};

module.exports.blueprints = {
    actions: true,
    rest: true,
    shortcuts: true
};