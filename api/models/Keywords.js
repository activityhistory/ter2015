/**
* Keywords.js
*
* @description :: TODO: You might write a short summary of how this model works and what it represents here.
* @docs        :: http://sailsjs.org/#!documentation/models
*/

module.exports = {
  getAll:function(req,res){
   var sqlite3 = require('sqlite3').verbose();
   var db = new sqlite3.Database('./assets/db/selfspy.sqlite');
   db.all("SELECT keyword FROM privacy_keywords", function(err, rows) {
      if(err)
	console.log(err);
     
      res.view('keywords',{keywords:rows});
    });
    db.close;
  },
  save: function(keyword,res){
    var sqlite3 = require('sqlite3').verbose();
    var db = new sqlite3.Database('./assets/db/selfspy.sqlite');
    
    //Check if location isn't already in DB
     db.all("SELECT * FROM privacy_keywords WHERE keyword='"+keyword.keyword+"'", function(err,rows){
	if(err)
	  console.log(err);
	else if(rows.length ===0){
	  //Insert in DB
	  var stmt = db.prepare("INSERT INTO privacy_keywords(keyword) VALUES ('"+keyword.keyword+"')");
	  
	  stmt.run();
	  stmt.finalize();
	  
	}
	else{
	  res.view('keywords',{keywordsErr:'Keyword already exists'});
	}
     });
    db.close;
  }/*,
  removeLocation:function(location,res){
    var sqlite3 = require('sqlite3').verbose();
    var db = new sqlite3.Database('./assets/db/test');
    var query = "DELETE FROM locations WHERE id = "+location.id;    
    var stmt = db.prepare(query);
    
    stmt.run();
    stmt.finalize();
    db.all("SELECT * FROM locations", function(err, rows) {
      if(err)
	console.log(err);
  
      res.view('locations',{locations:rows});
    });    
    db.close;
  }*/
};

