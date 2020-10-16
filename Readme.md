# NerdFont Patcher

This is a hackish wrapper for the NerdFont patcher script.
It's dumb, but it works!

## Requirements

- Internet conection
- curl ```To Download font glyphs```

## Usage

- Download and extract a [monospace](https://rubjo.github.io/victor-mono/) font
  into the cloned folder (in this case, the ```ttf``` dir)
- Run the code below. It should download the font-glyphs
  and patcher script from the NerdFonts repo and start patching.

```bash
$ chmod +x nerdfont-patcher.py
$ ./nerdfont-patcher.py {font dir name} {font name}
```

Eg:

```bash
$ ./nerdfont-patcher.py ./ttf VictorMono
```

> Patched fonts are generated in the "Patched" folder under the font name you specified
