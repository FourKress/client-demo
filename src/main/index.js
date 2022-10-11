// import fs from 'fs';
import path from 'path';
import childProcess from 'child_process';
import { decode } from 'iconv-lite';
import { app, BrowserWindow, ipcMain } from 'electron';
import '../renderer/store';

// const tempPath = path.join(app.getPath('userData'), '/_temp');
// if (!fs.existsSync(tempPath)) {
//   fs.mkdirSync(tempPath);
// }

const PROTOCOL = 'client-demo';
const args = [];
if (!app.isPackaged) {
  // 如果是开发阶段，需要把我们的脚本的绝对路径加入参数中
  args.push(path.resolve('./urlProtoco.nsh'));
}
// 加一个 `--` 以确保后面的参数不被 Electron 处理
args.push('--');
// 注册协议
app.setAsDefaultProtocolClient(PROTOCOL, process.execPath, args);

/**
 * Set `__static` path to static files in production
 * https://simulatedgreg.gitbooks.io/electron-vue/content/en/using-static-assets.html
 */
if (process.env.NODE_ENV !== 'development') {
  global.__static = require('path')
    .join(__dirname, '/static')
    .replace(/\\/g, '\\\\'); // eslint-disable-line
}

let mainWindow;
const winURL =
  process.env.NODE_ENV === 'development'
    ? 'http://localhost:9080'
    : `file://${__dirname}/index.html`;

ipcMain.on('start', (event) => {
  console.log('————————开始PY进程————————');
  event.sender.send('start', '————————开始PY进程————————');

  // let pyPath = `${path.join(__static, './demo.py')}`;
  // if (process.env.NODE_ENV !== 'development') {
  //   pyPath = path.join(__static, '/demo.py')
  //     .replace('\\app.asar\\dist\\electron', '');
  // }
  // const workerProcess = childProcess.spawn('python', [
  //   '-u',
  //   `${pyPath}`,
  //   'hello python',
  // ]);

  let pyPath = `${path.join(__static, './demo.exe')}`;
  if (process.env.NODE_ENV !== 'development') {
    pyPath = path.join(__static, '/demo.exe')
      .replace('\\app.asar\\dist\\electron', '');
  }
  const workerProcess = childProcess.spawn(`${pyPath}`, [
    'hello python',
  ]);

  const encoding = 'cp936';
  const binaryEncoding = 'binary';

  workerProcess.stdout.on('data', (data) => {
    const result = decode(Buffer.from(data, binaryEncoding), encoding);
    console.log(`stdout: ${result}`);
    event.sender.send('start', result);
  });
  workerProcess.stderr.on('data', (data) => {
    const result = decode(Buffer.from(data, binaryEncoding), encoding);
    console.log(`stderr: ${result}`);
    event.sender.send('start', result);
  });
  workerProcess.on('close', (code) => {
    console.log(`PY子进程已退出，退出码 ${code}`);
    event.sender.send('start', `PY子进程已退出，退出码 ${code}`);
  });
});

function createWindow() {
  /**
   * Initial window options
   */
  mainWindow = new BrowserWindow({
    height: 768,
    useContentSize: true,
    width: 1600,
    webPreferences: {
      nodeIntegration: true,
    },
    show: false,
    icon: 'src/logo.ico',
  });

  mainWindow.loadURL(winURL);
  global.mainWindow = mainWindow;

  mainWindow.on('closed', () => {
    mainWindow = null;
  });

  mainWindow.on('ready-to-show', () => {
    mainWindow.maximize();
    mainWindow.show();
  });
}

const gotTheLock = app.requestSingleInstanceLock();
if (!gotTheLock) {
  app.quit();
} else {
  app.on('second-instance', () => {
    // 当运行第二个实例时,将会聚焦到myWindow这个窗口
    if (mainWindow) {
      mainWindow.show();
      if (mainWindow.isMinimized()) {
        mainWindow.restore();
      }
      mainWindow.focus();
    }
  });

  // 创建 myWindow, 加载应用的其余部分, etc...
  app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
      app.quit();
    }
  });

  app.on('before-quit', () => {
    if (global.server) {
      global.server.close();
    }
  });

  app.on('activate', () => {
    if (mainWindow === null) {
      createWindow();
    }
  });

  app.on('ready', async () => {
    createWindow();
  });
}