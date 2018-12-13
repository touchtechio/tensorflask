const express = require('express');         // Express Web Server
const busboy = require('connect-busboy');   // Middleware to handle the file upload https://github.com/mscdex/connect-busboy
const path = require('path');               // Used for manipulation with path
const fs = require('fs-extra');             // Classic fs

const app = express(); // Initialize the express web server
app.use(busboy({
    highWaterMark: 2 * 1024 * 1024, // Set 2MiB buffer
})); // Insert the busboy middle-ware

const uploadPath = path.join(__dirname, 'fu/'); // Register the upload path
fs.ensureDir(uploadPath); // Make sure that he upload path exits

var Client = require('node-rest-client').Client;

var client = new Client();

//var external_baseurl = os.environ['EXT_URL_BASE']

var EXT_URL_BASE = process.env.EXT_URL_BASE || 'http://contentai.intel.com';


/**
 * Create route /upload which handles the post request
 */
app.route('/upload/new').post((req, res, next) => {

    req.pipe(req.busboy); // Pipe it trough busboy

    req.busboy.on('file', (fieldname, file, filename) => {
        console.log(`Upload of '${filename}' started`);

        // Create a write stream of the new file
        const fstream = fs.createWriteStream(path.join(uploadPath, filename));
        // Pipe it trough
        file.pipe(fstream);

        // On finish of the upload
        fstream.on('close', () => {
            console.log(`Upload of '${filename}' finished`);
            console.log(`EXT_URL_BASE of '${EXT_URL_BASE}' `);



            var args = {
                data: { filename: filename, uri: EXT_URL_BASE +'/m/'+filename},
                headers: { "Content-Type": "application/json" }
            };

            // direct way
            client.post(EXT_URL_BASE + '/media/api/media', args, function (data, response) {
                // parsed response body as js object
                console.log(data);
                // raw response
                console.log(response);
            });

            res.redirect('/media/');
        });
    });
});


/**
 * Serve the basic index.html with upload form
 */
app.route('/upload').get((req, res) => {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('<form action="/upload/new" method="post" enctype="multipart/form-data">');
    res.write('<input type="file" name="fileToUpload"><br>');
    res.write('<input type="submit">');
    res.write('</form>');
    return res.end();
});

const server = app.listen(3200, function () {
    console.log(`Listening on port ${server.address().port}`);
});