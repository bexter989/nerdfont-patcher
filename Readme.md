# NerdFont Patcher

This is a hackish wrapper for the NerdFont patcher script.
I dont know if there is an official way of doing this so...
Plus it now has multiprocess support to speed up font patching.

It's dumb, but it works! on Linux! and WSL for windows 10 "¯\\_(ツ)_/¯"

## Greeting and Thanks

A big hello and Thanks to the guys at [Nerdfonts.com](https://www.nerdfonts.com). They've
done a wonderful job so thanks guys.


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
$ sudo apt install fontforge python-fontforge python-configparser
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

## Watch a clip

Watch a 3 minute clip on [Youtube](https://youtu.be/ryKjZStHLtU)


> [!NOTE]
> Patched fonts are generated in the "Patched" folder under the font name you specified
