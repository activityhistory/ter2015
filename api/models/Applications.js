/**
* Applications.js
*
* @description :: TODO: You might write a short summary of how this model works and what it represents here.
* @docs        :: http://sailsjs.org/#!documentation/models
*/

module.exports = {
  getAll:function(req,res){
   var sqlite3 = require('sqlite3').verbose();
   var db = new sqlite3.Database('./assets/db/selfspy.sqlite');
    db.all("SELECT  name, isprivate, id FROM (SELECT name, isprivate, id FROM process UNION SELECT keyword as name, isprivate, id FROM privacy_keywords k WHERE k.isApp = 1 ) app;", function(err, rows) {
      if(err)
	console.log(err);
     
      res.view('apps',{apps:rows});
    });
    db.close;
  },
  changeState:function(app,res){
    var sqlite3 = require('sqlite3').verbose();
    var db = new sqlite3.Database('./assets/db/selfspy.sqlite');
    var q = "SELECT * FROM process WHERE id = "+app.id+" AND name='"+app.name+"'";
      console.log("Requete "+ q);

      db.all(q, function(err, rows){
          if(err)
            console.log(err);

          else if(rows.length > 0){
              var query = "UPDATE process SET isprivate="+app.isprivate+" WHERE id = "+app.id+" AND name='"+app.name+"'";
              var stmt = db.prepare(query);

              stmt.run();
              stmt.finalize();
              //Refresh view
              db.all("SELECT  name, isprivate,id FROM (SELECT name, isprivate, id FROM process UNION SELECT keyword as name, isprivate, id FROM privacy_keywords k WHERE k.isApp = 1 ) app;", function(err, rows) {
                  if(err)
                      console.log(err);

                  res.view('apps',{apps:rows});
              });
          }

          else{

              var query = "UPDATE privacy_keywords SET isprivate="+app.isprivate+" WHERE id = "+app.id;
              var stmt = db.prepare(query);

              stmt.run();
              stmt.finalize();
              //Refresh view
              db.all("SELECT  name, isprivate,id FROM (SELECT name, isprivate, id FROM process UNION SELECT keyword as name, isprivate, id FROM privacy_keywords k WHERE k.isApp = 1 ) app;", function(err, rows) {
                  if(err)
                      console.log(err);

                  res.view('apps',{apps:rows});
              });
          }
      });
    db.close;
  },
    add: function(app,res){
        var sqlite3 = require('sqlite3').verbose();
        var db = new sqlite3.Database('./assets/db/selfspy.sqlite');

        //Check if  isn't already in DB

        db.all("SELECT keyword FROM privacy_keywords WHERE keyword ='"+app.name+"'", function(err, rows) {
            if(err)
                console.log(err);
            if(rows.length === 0){

                //Insert in DB
                var stmt = db.prepare("INSERT INTO privacy_keywords(keyword,isApp) VALUES ('" + app.name + "', 1)");
                stmt.run();
                stmt.finalize();
                //Refresh view
                db.all("SELECT  name, isprivate,id FROM (SELECT name, isprivate, id FROM process UNION SELECT keyword as name, isprivate, id FROM privacy_keywords k WHERE k.isApp = 1 ) app;", function(err, rows) {
                    if(err)
                        console.log(err);

                    res.view('apps',{apps:rows});
                });
            }
            else
                res.view('apps',{error: 'Already exists in DB'});
        });
        db.close;
    }
};

