const { app, BrowserWindow, ipcMain, clipboard } = require('electron');
const path = require('node:path');

app.whenReady().then(() => {
  ipcMain.handle('demo:copy', (_event, text) => {
    if (typeof text !== 'string') throw new TypeError('Expected text');
    clipboard.writeText(text);
  });

  const window = new BrowserWindow({
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
    },
  });
  window.loadFile('index.html');
});
