# NerdFont Patcher

This is a hackish wrapper for the NerdFont patcher script.
It's dumb, but it works!

## Requirements

- [Fontforge](https://fontforge.org/en-US/downloads/) (for patching the fonts)
- Internet conection (for obvious reasons)
- curl (to download font glyphs)

## Usage

- Install fontforge
- Download and extract a [monospace font](https://rubjo.github.io/victor-mono/)
  into the cloned folder (in this case, the ```ttf``` dir)
- Run the code below. It should download the font-glyphs
  and patcher script from the NerdFonts repo and start patching.

### Linux

```bash
$ sudo apt install fontforge
```

### Windows

> Download fontforge from [this link](https://fontforge.org/en-US/downloads/) and install it.
> make sure the exe is in your user or system path.

```bash
git clone https://github.com/bexter989/nerdfont-patcher.git
cd nerdfont-patcher
chmod +x nerdfont-patcher.py
./nerdfont-patcher.py {font dir name} {font name}
```

Eg:

```bash
./nerdfont-patcher.py ./ttf VictorMono
```

> Patched fonts are generated in the "Patched" folder under the font name you specified
