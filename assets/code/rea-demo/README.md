# REA clipboard fixture

Original, synthetic Electron source files for the accompanying blog post.
They are an input for static analysis, not a packaged application. No npm install
or Electron installation is needed to analyze this directory with REA.

With Node.js 22.19+ in the 22.x line, 24.11+ in the 24.x line, or 26+:

```sh
npx -y rea-agents@6.5.0 analyze-javascript-application "$PWD" --json > ../demo-evidence.json
```

Run the command from this fixture's directory. Keep the output outside the input
directory. On Linux, a procps-compatible `ps` must be on PATH.

Follow the literal channel `demo:copy` between preload.js and main.js. The main
handler calls Electron's clipboard.writeText. The renderer calls desktop.copy.
Static analysis does not demonstrate that a click occurred or the clipboard
changed. This fixture is not a production Electron security template.
