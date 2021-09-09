# NerdFont Patcher

This is a hackish wrapper for the NerdFont patcher script.
I don't know if there is an official way of doing this so...
Plus it now has multiprocessing support to speed up font patching.

It's dumb, but it works! on Linux! and WSL for windows 10 "¯\\_(ツ)_/¯"

## Greeting and Thanks

A big hello and Thanks to the guys at [Nerdfonts.com](https://www.nerdfonts.com). They've
done a wonderful job so thanks, guys.

## Requirements

-   [Fontforge](https://fontforge.org/en-US/downloads/) (for patching the fonts)
-   configparser
-   Internet connection (for obvious reasons)
-   curl (to download font glyphs)

## Setup

-   Install fontforge:
    ```bash
    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:fontforge/fontforge -y
    sudo apt-get update
    sudo apt-get install fontforge
    ```
-   Install other dependencies:
    ```bash
    sudo apt-get install python3-fontforge python-configparser
    ```
    It will download the font-glyphs and patcher script from the nerdfonts repo.
-   Clone and cd into this repo
    ```bash
    git clone https://github.com/bexter989/nerdfont-patcher.git; cd nerdfont-patcher
    ```
-   Run the script:
    ```bash
    python3 ./nerdfont-patcher.py {font dir name} {font name}
    ```
    Patched fonts are generated in the "Patched" folder with the specified font name.

## Usage

-   Download and extract any monospace font (e.g., [VictorMono](https://rubjo.github.io/victor-mono/)) into the cloned folder (in this case, the `TTF` dir).
-   Run the script as follows:
    ```bash
    python3 ./nerdfont-patcher.py ./TTF VictorMono
    ```

## Demonstration

Watch a 3-minute clip on [Youtube](https://youtu.be/ryKjZStHLtU)
