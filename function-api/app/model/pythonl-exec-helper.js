'use strict';

const childProcess = require('child_process');
const exec = childProcess.exec;

/**
 * Python script execution process helper.
 */
class PythonExecHelper {
  static getPythonExecPromise(command) {
    return new Promise((resolve, reject) => {
      exec(command, (error, stdout, stderr) => {
        console.log('stdout', stdout);
        if (error) {
          throw Error(`Exec error: ${error}`);
        }
        if (stderr) {
          throw Error(`Exec stderr: ${stderr}`);
        }
        resolve(stdout);
      });
    });
  }
}

module.exports = PythonExecHelper;
