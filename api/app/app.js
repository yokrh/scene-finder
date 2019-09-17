const express = require('express');
const cors = require('cors');
const ytdl = require('ytdl-core');
const fs = require('fs');
const childProcess = ('child_process');
const AWS = require('aws-sdk');

const app = express();
const router = express.Router();
const exec = childProcess.exec;
const s3 = new AWS.S3();

// const bodyParser = require('body-parser');
// router.use(bodyParser.json())
// router.use(bodyParser.urlencoded({ extended: true }))


/**
 * Option method request handler. For cors.
 */
router.options('*', (req, res) => res.sendStatus(200));

/**
 * Health check.
 */
router.get('/health', (req, res) => res.send('OK!'));

/**
 * Use ytdl(https://github.com/fent/node-ytdl-core)
 * to download a youtube video.
 */
router.get('/ytdl/download', cors(), (req, res) => {
  // console.log('/ytdl/download', req.query);

  const url = req.query.url;
  if (!url) {
    res.send('need youtube video url.');
    return;
  }

  const name = req.query.name || 'video';
  res.header(
    'Content-Disposition',
    `attachment; filename="${name}.mp4"`
  );

  ytdl(url, { format: 'mp4' }).pipe(res);
});

/**
 * Run python script.
 */
router.get('/opencv/capture', (req, res) => {
  const COMMAND = 'python static/bin/opencv/capture.py';
  exec(COMMAND, (error, stdout, stderr) => {
    if (error) {
      res.send('Error: ' + error);
      return;
    }
    res.send(stdout);
  });
});


app.use('/', router);

// Let aws-serverless-express to create a server
const server = app.listen(3000, () => {
  console.log("Expressjs port:", server.address().port);
});

// Export your express server so you can import it in the lambda function.
module.exports = app
