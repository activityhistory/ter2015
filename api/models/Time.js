/**
* Time.js
*
* @description :: TODO: You might write a short summary of how this model works and what it represents here.
* @docs        :: http://sailsjs.org/#!documentation/models
*/

module.exports = {
  getAll:function(req,res){
    var sqlite3 = require('sqlite3').verbose();
    var db = new sqlite3.Database('./assets/db/test');
    db.all("SELECT * FROM time", function(err, rows) {
      if(err)
	console.log(err);
      res.view('time',{time:rows,layout: null});
    });
    db.close;
  },
  save:function(time,res){
    var sqlite3 = require('sqlite3').verbose();
    var db = new sqlite3.Database('./assets/db/test');
    var query = "INSERT INTO time(weekEnd,week,fromHour,toHour) VALUES ("+time.weekEnd+", "+time.week+",'"+time.hourStart+"','"+time.hourStop+"')";
    var stmt = db.prepare(query);
 
    stmt.run();
    stmt.finalize();
    db.all("SELECT * FROM time", function(err, rows) {
      if(err)
	console.log(err);
      res.view('time',{time:rows,layout: null});
    }); 
    db.close; 
  },
  remove:function(time,res){
    var sqlite3 = require('sqlite3').verbose();
    var db = new sqlite3.Database('./assets/db/test');
    var query = "DELETE FROM time WHERE id = "+time.id;    
    var stmt = db.prepare(query);
    
    stmt.run();
    stmt.finalize();
    db.all("SELECT * FROM time", function(err, rows) {
      if(err)
	console.log(err);
      res.view('time',{time:rows,layout: null});
    });  
    db.close;
  }
};

