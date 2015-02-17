/**
 * Created by maxime on 17/02/15.
 */
/**
 * Cleaner
 *
 */

module.exports = {

    clean: function(req, res ){

        var PythonShell = require("python-shell");
        var path = require("path");

        var start = req.query.start;
        var stop = req.query.stop;
        var options = {
            scriptPath: "assets/python/",
            args: [start, stop]
        };
        var shell = new PythonShell('clean.py', options);
        shell.on('message', function(message){
            res.json(message);
        });
    }


};


