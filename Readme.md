# NerdFont Patcher

This is a hackish wrapper for the NerdFont patcher script.
I dont know if there is an official way of doing this so...
Plus it now has multiprocess support to speed up font patching.

It's dumb, but it works! on Linux! and WSL for windows 10 "¯\\_(ツ)_/¯"

## Requirements

- [Fontforge](https://fontforge.org/en-US/downloads/) (for patching the fonts)
- configparser
- Internet connection (for obvious reasons)
- curl (to download font glyphs)

## Setup

- Install fontforge
- Download and extract a [monospace font](https://rubjo.github.io/victor-mono/)
  into the cloned folder (in this case, the ```ttf``` dir)
- Run the code below. It should download the font-glyphs
  and patcher script from the NerdFonts repo and start patching.

```bash
$ sudo apt install fontforge (python-fontforge python-configparser)
```

Python bindings

```bash
pip install --user fontforge configparser
```

Then:

```bash
git clone https://github.com/bexter989/nerdfont-patcher.git
cd nerdfont-patcher
chmod +x nerdfont-patcher.py
./nerdfont-patcher.py {font dir name} {font name}
```

## Running

```bash
./nerdfont-patcher.py ./ttf VictorMono
```

> [!NOTE]
> Patched fonts are generated in the "Patched" folder under the font name you specified
