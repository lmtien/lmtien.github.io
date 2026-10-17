const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('desktop', {
  copy: (text) => ipcRenderer.invoke('demo:copy', text),
});
