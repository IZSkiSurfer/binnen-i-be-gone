# Binnen-I be gone

An unofficial continuation of **Binnen-I be gone**, a browser extension that converts gender-inclusive spelling on German-language websites into conventional forms.

## Project goals

- Preserve the original text-replacement functionality.
- Fix bugs and improve stability on dynamic websites.
- Maintain compatibility with Microsoft Edge and Google Chrome.
- Keep maintenance and source changes transparent.

## Project status

The upstream baseline is version 3.1.1. The source import and patched release are being prepared. This repository is not yet a verified, installable release.

## Installation

Once the extension source is published:

1. Clone this repository or download and extract a release package.
2. Disable any previously installed copy of Binnen-I be gone.
3. Open `edge://extensions/` in Microsoft Edge or `chrome://extensions/` in Google Chrome.
4. Enable **Developer mode**.
5. Select **Load unpacked** and choose the directory containing `manifest.json`.
6. Reload affected websites.

Unpacked extensions do not receive automatic browser-store updates. Update the local files and reload the extension to install a newer version.

## Known upstream bug

Version 3.1.1 can throw the following exception:

```text
Uncaught TypeError: Cannot read properties of null (reading 'getAttribute')
    at acceptNode (binnenibegone.js:29)
```

The original code assumes that `document.activeElement` is always available. The planned fix guards against a null active element before accessing its attributes or calling `contains()`, preserving the original filtering behaviour.

## Browser compatibility

| Browser | Status |
| --- | --- |
| Microsoft Edge | Primary target; runtime testing pending |
| Google Chrome | Chromium target; runtime testing pending |
| Firefox | Upstream platform; maintained compatibility not yet verified |

## Contributing

Bug reports and pull requests are welcome. Please include the browser and extension versions, steps to reproduce, the affected website if shareable, and relevant developer-console errors. Remove personal information from logs and screenshots.

Keep changes focused and document intentional changes to text-replacement behaviour.

## Upstream and licence

This project is independent and is not endorsed by the original developer.

The original Firefox extension is available from [Mozilla Add-ons](https://addons.mozilla.org/firefox/addon/binnen-i-be-gone/) under the GNU General Public License v3.0 only (GPL-3.0-only). The planned source import uses that release as its baseline and retains upstream copyright and licensing notices.

All credit for the original extension and its text-replacement logic belongs to its original authors.
