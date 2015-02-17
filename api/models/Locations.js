/**
* Locations.js
*
* @description :: TODO: You might write a short summary of how this model works and what it represents here.
* @docs        :: http://sailsjs.org/#!documentation/models
*/

module.exports = {
  attributes: {
    name:	'STRING',
    address:	'STRING',
    latitude:	'FLOAT',
    longitude:	'FLOAT',
    isprivate:	'BOOLEAN'
  },
  getAll:function(req,res){
   var sqlite3 = require('sqlite3').verbose();
   var db = new sqlite3.Database('./test');
    db.all("SELECT * FROM locations", function(err, rows) {
      if(err)
	console.log(err);
      console.log('Requete OK');
  
      console.log(rows);
  
      res.view('locations',{locations:rows});
    });
    db.close;
  },
  getLocation:function(location,found){
    var sqlite3 = require('sqlite3').verbose();
    var db = new sqlite3.Database('./test');
    var query = "SELECT * FROM locations WHERE name = '"+location.name+"' OR address ='"+location.address+"'";
   
    console.log(query);
    
    db.all(query, function(err, rows) {
      if(err)
	console.log(err);
  
      console.log(rows);
      found = rows;
    });
    
    db.close;
  },
  save: function(location,res){
    var sqlite3 = require('sqlite3').verbose();
    var db = new sqlite3.Database('./test');
    var stmt = db.prepare("INSERT INTO locations(name,longitude,latitude,address,isprivate) VALUES ('"+location.name+"',"+location.longitude+","+location.latitude+",'"+location.address+"', "+location.isprivate+")");
    
    stmt.run();
    stmt.finalize();
    db.all("SELECT * FROM locations", function(err, rows) {
      if(err)
	console.log(err);
      console.log('Requete OK');
  
      console.log(rows);
  
      res.view('locations',{locations:rows});
    });    
    db.close;
  },
  updateLocation:function(location,res){
    var sqlite3 = require('sqlite3').verbose();
    var db = new sqlite3.Database('./test');
    if(location.isprivate)
      var query = "UPDATE locations SET isprivate=1 WHERE id = "+location.id;
    else
      var query = "UPDATE locations SET isprivate=0 WHERE id = "+location.id;
    var stmt = db.prepare(query);
    
    console.log(query);
    
    stmt.run();
    stmt.finalize();
    db.all("SELECT * FROM locations", function(err, rows) {
      if(err)
	console.log(err);
      console.log('Requete OK');
  
      console.log(rows);
  
      res.view('locations',{locations:rows});
    });    
    db.close;
  }
};


