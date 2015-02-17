/**
* Locations.js
*
* @description :: TODO: You might write a short summary of how this model works and what it represents here.
* @docs        :: http://sailsjs.org/#!documentation/models
*/

module.exports = {
  getAll:function(req,res){
   var sqlite3 = require('sqlite3').verbose();
   var db = new sqlite3.Database('./assets/db/test');
    db.all("SELECT * FROM locations", function(err, rows) {
      if(err)
	console.log(err);
     
      res.view('locations',{locations:rows});
    });
    db.close;
  },
  getLocation:function(location,found){
    var sqlite3 = require('sqlite3').verbose();
    var db = new sqlite3.Database('./assets/db/test');
    var query = "SELECT * FROM locations WHERE name = '"+location.name+"' OR address ='"+location.address+"'";
   
    console.log(query);
    
    db.all(query, function(err, rows) {
      if(err)
	console.log(err);

      found = rows;
    });
    
    db.close;
  },
  save: function(location,res){
    var sqlite3 = require('sqlite3').verbose();
    var db = new sqlite3.Database('./assets/db/test');
    
    //Check if location isn't already in DB
     db.all("SELECT * FROM locations WHERE name='"+location.name+"' OR address='"+location.address+"'", function(err,rows){
	if(err)
	  console.log(err);
	else if(rows.length ===0){
	  //Insert in DB
	  var stmt = db.prepare("INSERT INTO locations(name,longitude,latitude,address,isprivate) VALUES ('"+location.name+"',"+location.longitude+","+location.latitude+",'"+location.address+"', "+location.isprivate+")");
	  
	  stmt.run();
	  stmt.finalize();
	  db.all("SELECT * FROM locations", function(err, rows) {
	    if(err)
	      console.log(err);
	  
	    res.view('locations',{locations:rows});
	  }); 
	}
	else{
	  res.view('locations',{locationsErr:'Location already exists in DB, Please choose an other location name or address'});
	}
     });
     
      
    db.close;
  },
  updateLocation:function(location,res){
    var sqlite3 = require('sqlite3').verbose();
    var db = new sqlite3.Database('./assets/db/test');
    var query = "UPDATE locations SET isprivate="+location.isprivate+" WHERE id = "+location.id;    
    var stmt = db.prepare(query);
    
    stmt.run();
    stmt.finalize();
    db.all("SELECT * FROM locations", function(err, rows) {
      if(err)
	console.log(err);
  
      res.view('locations',{locations:rows});
    });    
    db.close;
  },
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
  }
};


