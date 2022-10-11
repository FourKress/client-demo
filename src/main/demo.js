const path = require('path');
const { spawn } = require('child_process');

function runScript() {
  return spawn('python', [
    '-u',
    path.join(__dirname, './demo.py'),
    'hello python',
  ]);
}

const subprocess = runScript();

subprocess.stdout.on('data', (data) => {
  console.log(`data:${data}`);
});
subprocess.stderr.on('data', (data) => {
  console.log(`error:${data}`);
});
subprocess.stderr.on('close', () => {
  console.log('Closed');
});
