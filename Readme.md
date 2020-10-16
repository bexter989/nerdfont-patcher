# NerdFont Patcher

This is a hackish wrapper for the NerdFont patcher script.

It's dumb, but it works! on Linux! "¯\\_(ツ)_/¯"

## Requirements

- [Fontforge](https://fontforge.org/en-US/downloads/) (for patching the fonts)
- Internet conection (for obvious reasons)
- curl (to download font glyphs)

## Setup

- Install fontforge
- Download and extract a [monospace font](https://rubjo.github.io/victor-mono/)
  into the cloned folder (in this case, the ```ttf``` dir)
- Run the code below. It should download the font-glyphs
  and patcher script from the NerdFonts repo and start patching.

```bash
$ sudo apt install fontforge
```

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
