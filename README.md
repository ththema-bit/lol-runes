# lol-runes

A static web page that recreates the League of Legends rune page, so you can build a page and
read every rune's effect (German and English). It is a plain HTML/JS page with local data, no
build step.

## Features

- Primary and secondary path, keystone and rows, secondary limited to 2 runes from different rows
- Stat shards
- Detail panel on hover or tap, search (Enter jumps to the match)
- Save pages in `localStorage`, share a page through the `#hash` in the URL
- German (`de_DE`) and English (`en_US`) texts

## Run

```bash
python3 -m http.server 8094
# open http://localhost:8094/
```

Any static file server works. The page loads `data/runes_<lang>.json` with `fetch`, so it must be served over HTTP (opening the file directly will not work).

## Data

Rune data and icons come from Riot's Data Dragon (`runesReforged.json` plus images). To update after a patch:

```bash
python3 tools/fetch_data.py            # latest version
python3 tools/fetch_data.py 14.1.1     # a specific version
```

Stat shards are not part of Data Dragon, so their values are maintained by hand in the `SH` object in `index.html`. Check them after balance changes.

## Disclaimer

This is an unofficial fan project. It is not endorsed by Riot Games and does not reflect the views or
opinions of Riot Games or anyone officially involved in producing or managing Riot Games properties.
Riot Games and League of Legends are trademarks or registered trademarks of Riot Games, Inc.
Rune names, texts and icons are Riot's property. The MIT license covers only the code in this repository.

## License

MIT (code only, see disclaimer)
