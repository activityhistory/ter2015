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
    console.log(params.days);
    console.log(params.hourStart);
    console.log(params.hourStop);
    
    if(params.days === null || !params.days){
      res.status(200).send('Erreur veuillez choisir les jours d\'enregistrement');
    }
    else if(params.days.length === 1){
	if(params.days[0] === 1){
	  params.week = 1;
	  params.weekEnd = 0;
	}
	  
	else{
	  params.weekEnd = 1;
	  params.week = 0;
	}
    }
    else{
      params.week = 1;
      params.weekEnd = 1;
    }
    Time.save(params,res); 
    Time.getAll(req,res);
  }
};

