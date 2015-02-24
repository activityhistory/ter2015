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
   db.all("SELECT keyword FROM privacy_keywords WHERE isApp=0", function(err, rows) {
      if(err)
	console.log(err);
     
      res.view('keywords',{keywords:rows});
    });
    db.close;
  },
  save: function(keyword,res){
    var sqlite3 = require('sqlite3').verbose();
    var db = new sqlite3.Database('./assets/db/selfspy.sqlite');
    
    //Check if  isn't already in DB

    db.all("SELECT keyword FROM privacy_keywords WHERE keyword ='"+keyword.keyword+"'", function(err, rows) {
        if(err)
            console.log(err);
        if(rows.length === 0){
            if(keyword.keyword.length !== 0) {
                //Insert in DB
                var stmt = db.prepare("INSERT INTO privacy_keywords(keyword) VALUES ('" + keyword.keyword + "')");
                stmt.run();
                stmt.finalize();
                //Refresh view
                db.all("SELECT keyword FROM privacy_keywords WHERE isApp = 0", function (err, rows) {
                    if (err)
                        console.log(err);

                    res.view('keywords', {keywords: rows});
                });
            }
        }
        else
            res.view('keywords',{error: 'Already exists in DB'});
     });
    db.close;
  },
  delete:function(keyword,res){
    var sqlite3 = require('sqlite3').verbose();
    var db = new sqlite3.Database('./assets/db/selfspy.sqlite');

    //Delete in DB
    var query = "DELETE FROM privacy_keywords WHERE keyword = '"+keyword.keyword+"'";
    var stmt = db.prepare(query);
    stmt.run();
    stmt.finalize();

    //Refresh view
    db.all("SELECT keyword FROM privacy_keywords AND isApp = 0", function(err, rows) {
      if(err)
          console.log(err);

      res.view('keywords',{keywords:rows});
    });
    db.close;
  }
};

