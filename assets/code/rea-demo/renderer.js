document.getElementById('copy').addEventListener('click', async () => {
  await window.desktop.copy('Hello from the demo');
  document.getElementById('status').textContent = 'Copied';
});
