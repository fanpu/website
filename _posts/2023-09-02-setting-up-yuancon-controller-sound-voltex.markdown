---
title: "Playing Sound Voltex at Home: Setting Up Unnamed SDVX Clone with the Yuancon SDVX Controller"
layout: post
tags: [general]
cover: fuji_ascent_1.webp
cover_preview: fuji_ascent_1.webp
caption: Yoshida Trail ascent on Mt Fuji, Shizuoka Prefecture, Japan
class: post-template
author: fanpu
toc:
  sidebar: left
giscus_comments: true
description: >
  UPDATE ME
published: true
---

My foray into rhythm games started way
back with [Love Live! School Idol Festival](https://lovelive-sif-global.bushimo.jp/).
While the game has sadly since shut down, other
titles that I've played
included [BanG Dream!](https://bang-dream-gbp-en.bushiroad.com/)
and [Project SEKAI](https://projectsekai.fandom.com/wiki/Project_SEKAI_COLORFUL_STAGE!).

When I visited Japan a few months ago in the summer, I discovered [Sound Voltex](https://p.eagate.573.jp/game/sdvx/sv/p/index.html), and instantly
fell in love with its unique control system and beautiful flashy graphics:

{% include figure.html 
    path="/assets/img/posts/sdvx/sdvx_and_me.webp"
    width="400px"
    class="z-depth-1"
%}

In Japan, you pay 100 yen (~$0.68 USD) to play two to three songs. You get to
play three songs if you don't crash (i.e fail) any tracks, and two if you fail
on either of the first two guaranteed plays.

Rhythm games in general are sadly not as mainstream outside of Japan.
For instance, in Singapore I was only aware of a single arcade that had Sound Voltex cabs,
even though arcades are quite popular in general. Similarly, in NYC, there's only a single 
small arcade called [Chinatown Fair](http://www.chinatownfair.biz/) that has Sound Voltex.
So naturally I wanted to see if I could set it up myself at home.

(Apparently, if you have a lot of disposable income and space in your living
room, you can also just buy an entire [previous-generation Sound Voltex
cabinet](https://www.hadouken-arcade.com/products/sound-voltex-vivid-wave) for a
few thousand dollars)

## Why This Guide
I decided to write this guide since the setup process could seem somewhat daunting for
people who are interested in rhythm games but are not developers. Hopefully with
this guide more people will also be able to play and enjoy this game.

The setup process is very straightforward on Windows, but has a few subtle
points on macOS and Linux that I'll point out.

## Setup Used
This guide will use the following setup:

- Game: [unnamed-sdvx-clone](https://github.com/Drewol/unnamed-sdvx-clone)
- Controller: [Yuancon SDVX controller](https://yuancon.store/controller/sdvxblack).

While I performed the setup on macOS, the instructions are largely the same
for Linux based systems as well. In fact, if you are already 
regardless of which controller or OS you use.

## Installing Unnamed SDVX Clone

### Windows
The setup process for Windows is very straightforward.
You should just download the [latest Windows build](https://drewol.me/Downloads/Game.zip) as linked on the [Github page](https://drewol.me/Downloads/Game.zip), and run `usc-game.exe` to start the game.

### macOS

This is mostly just from the [official instructions](https://github.com/Drewol/unnamed-sdvx-clone#macos),
but with implicit points made explicit:

1.  If you don't have [Homebrew](https://docs.brew.sh/) on your machine yet, install it by 
[following the instructions here](https://brew.sh/). Homebrew is a package management software.
2.  If you don't have [git](https://git-scm.com/) yet, install it with Homebrew:

    ```bash
    $ brew install git
    ```

    Git is a version control system (normally used for code). In our case, we use it mainly to obtain
    the project dependencies.
3.  Clone the `unnamed-sdvx-clone` with `git`:

    ```bash
    $ git clone https://github.com/Drewol/unnamed-sdvx-clone
    ```

    This will result in the game being downloaded to a `unnamed-sdvx-clone` folder
    in your current working directory.

4.  Navigate into the new folder, and download the submodules of the project:

    ```bash
    $ cd unnamed-sdvx-clone
    $ git submodule update --init --recursive
    ```

    This is necessary because the game has third-party dependencies, which are
    tracked as [other Github repositories](https://github.com/Drewol/unnamed-sdvx-clone/blob/develop/.gitmodules).

5.  Install more dependencies required to build the project with Homebrew:

    ```bash
    $ brew install cmake freetype libvorbis sdl2 libpng jpeg libarchive libiconv
    ```

    These are all open source libraries required for the following reasons:
    - [`cmake`](https://cmake.org/): a popular build system used to compile the project
    - [`freetype`](https://freetype.org/): for rendering fonts
    - [`libvorbis`](https://xiph.org/vorbis/): audio compression
    - [`sdl2`](https://www.libsdl.org/): get access to hardware inputs like keyboard, mouse, controller, etc
    - [`libpng`](https://github.com/glennrp/libpng): for using/manipulating PNG images
    - [`jpeg`](https://www.ijg.org/): for using/manipulating JPEG images
    - [`libarchive`](https://www.libarchive.org/): compression library
    - [`libiconv`](https://www.gnu.org/software/libiconv/): convert between different character encodings (i.e [ISO-8859-1](https://en.wikipedia.org/wiki/ISO/IEC_8859-1) to [UTF-8](https://en.wikipedia.org/wiki/UTF-8))

6.  Configure the project using `cmake`. In this case, the project author
    already kindly wrapped a script around this command, so we only have to run the
    script:

    ```bash
    $ ./mac-cmake.sh
    ```

7.  Compile and build the project:

    ```bash
    $ make
    ```

    This step could take a while. If you want to speed it up, you can run it and
    specify the `-j` argument parallelize the compilation based on the number of
    cores you have (use one less than your total number of cores):

    ```bash
    $ make -j 9
    ```
  
8.  Run the game from the `bin` folder:

    ```bash
    $ cd bin
    $ ./usc-game
    ```

    It is important to run it from the `./bin` folder and not the root of the
    project directory, as some skins search for file dependencies in a relative
    manner and will hence not be able to find it.

### Linux
Honestly if you're on Linux, you should be able to figure it out by yourself 😊

## First Startup

On first startup, you should see this:

{% include figure.html 
    path="/assets/img/posts/sdvx/sdvx_initial.gif"
    width="400px"
    class="z-depth-1"
%}

For now, you can just use your mouse to interface with the game.

## Configuring The Controller

Let's now setup our Yuancon controller!

1. 
    Quit the game, and unplug your SDVX controller if it is plugged in

2. 
    Hold the `START` and `BT-C` button simultaneously. The `START` button is the
    diamond-shaped button at the top, while the BT-C is the third white button from
    the left (it should also be labelled on the controller board). 

    Then while still holding down both buttons, connect it to your computer.
    This will put it in [Controller HID Mode](https://oniichan.wtf/help/index.html),
    where the controller inputs as a gamepad.

3. 
    Start up the game again, and navigate to the `Settings` page.
    Here, you want to do the following:

    - Set `Button input mode` to `Controller`
    - Set `Laser input mode` to `Controller`
    - Adjust laser sensitivity accordingly (I like `1.875`)
    - Click on each of the key bindings, and hit the corresponding
    keys on your controller. I used the button on the
    right side of the controller panel as my back button.

    You should have something that looks similar to this:

    {% include figure_simple.html 
        path="/assets/img/posts/sdvx/sdvx-settings.webp"
        width="600px"
        class="z-depth-1"
    %}

4. 
    Restart the game. You should now be able to use the knobs to cycle through
    the menus, and the buttons to activate them!

## Getting Songs
Right after setup, there are no songs to play yet.

There are a few places you can get songs:

- [Ripped songs from SDVX](https://oniichan.wtf/help/songs.html), probably questionable legality but almost everyone recommends and uses it





## Skinning The Game

The default skin is 
{% include figure.html 
    path="/assets/img/posts/sdvx/sdvx-default-480.gif"
    width="400px"
    class="z-depth-1"
%}
You can get skins from the game [here](https://oniichan.wtf/help/skins.html).


Choose 

### ExperimentalGear

Of all the skins I've tried, I like ExperimentalGear the most as it
has essentially the same UI and UX as the most recent Sound Voltex Exceed Gear
cabinet.

skins/ExperimentalGear/scripts/language/EN.lua

## Some additional 

### Aside: KSM Chart Formats
KSM charts have a `.ksh` extensions. This can be a useful check to ensure
that any charts that you download are actually for this game.

The following is a snippet of the `ADV.ksh` (i.e advanced beatmap)
file for YOASOBI's Idol (アイドル):

```bash
title=アイドル
artist=YOASOBI /「推しの子」より
effect=AS
jacket=jk.jpg
illustrator=-
difficulty=challenge
level=10
t=166
m=music.ogg
o=0
bg=desert
layer=smoke
po=56024
plength=15000
pfiltergain=50
filtertype=peak
chokkakuautovol=0
chokkakuvol=50
ver=171
--
beat=4/4
0000|00|--
--
0000|00|0-
0000|00|:-
0000|00|o-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|o-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|P-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|P-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
0000|00|:-
--
0000|00|0-
0000|00|:-
filtertype=lpf1
0000|00|0o
0000|00|::
0000|00|o0
0000|00|::
```