# Aurora

**A simple, modern and elegant muOS theme.**

## Installation

### From the "Releases" page

1. Head over to the **Releases** page : [link](https://github.com/oiimrosabel/AuroraMuOSTheme/releases)
2. Find the most recent release
3. Download the zip with the variant you want
4. Move it to `/MUOS/theme/` (on the `SD2`, or `SD1` if you use only one card)
5. Apply the theme from the **Theme Picker**

### From source

> [!IMPORTANT]
> Before you start, bear in mind every action described here must be done on a **Linux distro** (or **WSL**) or **macOS** with a recent enough version of **Python** (>= Python 3.12).

> [!CAUTION]
> This method may produce broken themes, as this repo contains untested code. If you don't mind that, or want to tinker with the tools I made, go ahead :3.

1. Clone this repo :

```bash
git clone https://github.com/oiimrosabel/AuroraMuOSTheme.git
```

2. Change to project root :

```bash
cd ./AuroraMuOSTheme/
```

3. Execute the generation script.

```bash
python3 -m Aurora
```

4. Head over to the `build` folder at the root of the project. You should find the theme `.muxthm` files, one for each
   color variant.
5. Move the zips to the correct folder, as indicated above (from the 4th instruction onwards)

#### Script arguments

The aforementioned script can make use arguments to finetune the generation process.
Here are some examples :

```bash
# Generates zips for the Dark AND OLED variant without grid support
python3 -m Aurora -t Moon,Midnight -g off

# Generates zips for the White variant with AND without grid support (also generates the icon pack)
python3 -m Aurora -t Cloud -g both

# Cleans the build folder
python3 -m Aurora -c 

# Generates the icon pack
python3 -m Aurora -p

# Shows all the available arguments
python3 -m Aurora -h
```

#### TL;DR

For convenience, you can copy-paste the following script into a `.sh` file and execute it using `bash`, or paste it
directly in the terminal and hit <kbd>Enter</kbd>:

```bash
git clone https://github.com/oiimrosabel/AuroraMuOSTheme.git
cd ./AuroraMuOSTheme
python3 -m Aurora
cd build
ls
```

## Grid support

This theme officially support muOS's grid layout for the "Explore" page. To do so, follow those steps :

1. Obtain the icons archive, it's usually referred to as `AuroraConsoleIcons.muxzip`. You can obtain it...
    * from the **Releases** page (see above)
    * alongside the generated zips if you opted for the manual way. Note that it will only be generated if you
      answered "**Yes**" or "**Both**" to the prompt at the start of the generation script.
2. Put it into the `ARCHIVE` folder at the root of either `SD1` or `SD2`.
3. Go into `Apps` > `ArchiveManager` and select `[SDX] AuroraConsoleIcons`. Wait for the installation script to finish.
4. Make sure to select a theme variant with grid support (they usually ends with `Grid`).

## Troubleshooting

### Your screen is blank and/or your system gets bricked

> Please go into your `MUOS/theme/active` folder and remove everything in there, your system should now boot, and you
> can choose a different (not broken) theme. - [Harry](https://hmcneill46.github.io/muOS-MinUIfied-Theme-Generator/)

### An error occurred during the "generation" phase

- Make sure the version of Python you're using is recent enough. Also, make sure you're using `python3` instead of
  `python` in the command prompt.
    - If you're unsure, execute `python3 --version` (or `python --version` if the former yields an error).
- Make sure the message is an actual error. Some are just warns, meant to ease out debugging. Errors are usually
  prefixed by `⨉ ERROR` (and not `⚠ WARNING`). Note that warnings should only appear if the `-v` or `--verbose` is set.
    - Errors usually appears before the script stops. If you're using `bash`, execute `echo $?` to see the script's
      return code. If it's `0`, that means the script worked properly.
- If none of these steps solved your issue, send me a message on Discord by DMs (`@oiimrosabel`) with the error message,
  I'll help you troubleshoot the issue.

### The "Explore" menu is empty

That probably means you forgot to install the icon pack that goes alongside the themes. Refer to the **Grid support**
section above to install it.