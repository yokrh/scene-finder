'use strict';

const AwsHelper = require('./model/aws-helper');
const PythonExecHelper = require('./model/pythonl-exec-helper');

const express = require('express');
const cors = require('cors');
const fs = require('fs');
const ytdl = require('ytdl-core');

const app = express();
const router = express.Router();
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
router.get('/find', async (req, res) => {
  console.log("\n/find")
  const video = 'video_luna.mp4';
  const image = 'out_10001200.png';
  const bucket = 'scene-finder';
  const similarity_border = 0.995;
  const trim_scene_top = 0.33;
  const trim_scene_bottom = 0.66;
  const trim_scene_left = 0.05;
  const trim_scene_right = 0.95;
  const mask_background_color = 255;  // 0:black ([0,0,0]-[0,0,160]), 255:white ([0,0,50]-[255,255,255])
  const mask_hsv_min_h = 0;
  const mask_hsv_min_s = 0;
  const mask_hsv_min_v = 50;
  const mask_hsv_max_h = 255;
  const mask_hsv_max_s = 255;
  const mask_hsv_max_v = 255;
  const ocr_language = 'jpn';

  /*

  // Load a video
  console.log("\n### Load a video");
  {
    const s3videoObject = await AwsHelper.S3.getObject(bucket, video);
    console.log(s3videoObject, s3videoObject.Body, s3videoObject.Body.length);

    // Write a video
    const videoFilePath = `static/data/${video}`;
    fs.writeFileSync(videoFilePath, s3videoObject.Body);
  }

  // capture frame frames
  console.log("\n### capture frame");
  {
    const command = `python static/bin/opencv/capture_frame.py ${video}`;
    await PythonExecHelper.getPythonExecPromise(command)
      .catch((error) => {
        console.log('catch Error:', error);
        return res.send('catch Error');
      });
  }

  // Load an image
  console.log("\n### Load an image");
  {
    const s3imageObject = await AwsHelper.S3.getObject(bucket, image);
    console.log(s3imageObject, s3imageObject.Body, s3imageObject.Body.length);

    // Write an image
    const imageFilePath = `static/data/${image}`;
    fs.writeFileSync(imageFilePath, s3imageObject.Body);
  }

  // */

  // find similar scenes
  console.log("\n### find similar scenes");
  {
    const command = `python static/bin/opencv/find_similar_scene.py ${image} ${similarity_border}`;
    await PythonExecHelper.getPythonExecPromise(command)
      .catch((error) => {
        console.log('catch Error:', error);
        return res.send('catch Error');
      });
  }

  // trim scenes
  console.log("\n### trim scenes");
  {
    const command = `python static/bin/opencv/trim_scene.py ${trim_scene_top} ${trim_scene_bottom} ${trim_scene_left} ${trim_scene_right}`;
    await PythonExecHelper.getPythonExecPromise(command)
      .catch((error) => {
        console.log('catch Error:', error);
        return res.send('catch Error');
      });
  }

  // mask scenes
  console.log("\n### mask scenes");
  {
    const command = `python static/bin/opencv/mask_scene.py ${mask_background_color}`
      + ` ${mask_hsv_min_h} ${mask_hsv_min_s} ${mask_hsv_min_v}`
      + ` ${mask_hsv_max_h} ${mask_hsv_max_s} ${mask_hsv_max_v}`;
    await PythonExecHelper.getPythonExecPromise(command)
      .catch((error) => {
        console.log('catch Error:', error);
        return res.send('catch Error');
      });
  }

  // scene ocr
  console.log("\n### scene ocr");
  {
    const command = `python static/bin/opencv/scene_ocr.py ${ocr_language}`;
    const ocrResult = await PythonExecHelper.getPythonExecPromise(command)
      .catch((error) => {
        console.log('catch Error:', error);
        return res.send('catch Error');
      });

    const json = JSON.parse(ocrResult);
    for (let k of Object.keys(json)) {
      const v = json[k];
      console.log(k, v);
    }
  }

  // res.send('done');
});

app.use('/', router);

// Let aws-serverless-express create a server
const server = app.listen(3000, () => {
  console.log('Expressjs port:', server.address().port), "\n";
});

// Export your express server so you can import it in the lambda function.
module.exports = app
