'use strict';

const childProcess = require('child_process');
const exec = childProcess.exec;

class PythonExecHelper {
  static getPythonExecPromise(command) {
    return new Promise((resolve, reject) => {
      console.log('=== exec begin ===');
      exec(command, (error, stdout, stderr) => {
        console.log('=== exec done ===');
        console.log('stdout', stdout);
        if (error) {
          const msg = `Exec error: ${error}`;
          throw Error(msg);
        }
        if (stderr) {
          const msg = `Exec stderr: ${stderr}`;
          throw Error(msg);
        }
        resolve();
      });
    });
  }
}

module.exports = PythonExecHelper;
