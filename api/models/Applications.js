/**
* Applications.js
*
* @description :: TODO: You might write a short summary of how this model works and what it represents here.
* @docs        :: http://sailsjs.org/#!documentation/models
*/

module.exports = {
  getAll:function(req,res){
   var sqlite3 = require('sqlite3').verbose();
   var db = new sqlite3.Database('./assets/db/selfspyPublic.sqlite');
    db.all("SELECT * FROM process", function(err, rows) {
      if(err)
	console.log(err);
     
      res.view('apps',{apps:rows});
    });
    db.close;
  },
  changeState:function(app,res){
    var sqlite3 = require('sqlite3').verbose();
    var db = new sqlite3.Database('./assets/db/selfspyPublic.sqlite');
    var query = "UPDATE process SET isprivate="+app.isprivate+" WHERE id = "+app.id;  
    var stmt = db.prepare(query);
    
    stmt.run();
    stmt.finalize();
     
    db.close;
    res.status(400);
  }
};

