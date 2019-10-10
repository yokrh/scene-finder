'use strict';

//const AWS = require('aws-sdk');
//const cognitoidentity = require('aws-sdk/clients/cognitoidentity');
const awsSdkClientS3 = require('aws-sdk/clients/s3');  // https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#getObject-property

const accessKeyId = 'AKIARS7BSK624CSFS6FR';  // new IAM one. Need to move in prod
const secretAccessKey = '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'; // new IAM one. Need to move in prod
const region = 'ap-northeast-1';
const bucket = 'scene-finder';
const s3 = new awsSdkClientS3({
  accessKeyId,
  secretAccessKey,
  region,
});

/**
 * S3 Helper.
 */
class S3 {
  static getObject(key) {
    return s3.getObject({
      Bucket: bucket,
      Key: key,
    })
    .promise()
    .catch((error) => {
      console.log('catch Error:', error);
      return res.send('catch Error');
    });
  }
}

const AwsHelper = {
  S3,
};
module.exports = AwsHelper;
