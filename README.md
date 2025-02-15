# Rezolution
**A simple, modern and elegant muOS theme inspired by GTK4.**

## Installation
### From the "Releases" page
1. Head over to the **Releases** page : [link](https://github.com/oiimrosabel/RezolutionMuOSTheme)
2. Find the most recent release
3. Download the zip with the variant you want
4. Move it to `/MUOS/theme/` (on the `SD2`, or `SD1` if you use only one card)
5. Apply the theme from the **Theme Picker**

### From source
> **Warning** : before you start, bear in mind every action described here must be done on a **Linux distro** (or WSL) with a recent enough version of **Python** (>= Python 3.10).

> **Warning** : This method may produce broken themes, as this repo contains untested code. If you don't mind that, or want to tinker with the tools I made, go ahead :3.

1. Clone this repo :
```bash
git clone https://github.com/oiimrosabel/RezolutionMuOSTheme.git
```
2. Go into the `__factory` folder at the root of the project :
```bash
cd ./__factory
```
3. Execute the generation script. Note that it will prompt you whether you want your themes to be generated with grid support.
```bash
python3 ./generate.py
```
4. Head over to the `__build` folder at the root of the project. You should find at least 3 zips, one for each color variant.
5. (**Optional**) If you plan to tinker with the theme (for example, to create your own), make sure to clean the `__build` folder by executing :
```bash
# cd ./__factory
python3 ./clean.py
```
6. Move the zips to the correct folder, as indicated above (from the 4th instruction onwards)

#### TL;DR
For convenience, you can copy-paste the following script into a `.sh` file and execute it using `bash` :

```bash
git clone https://github.com/oiimrosabel/RezolutionMuOSTheme.git
cd ./RezolutionMuOSTheme/__factory
python3 ./generate.py
cd ../__build
ls
```

## Grid support
This theme officially support muOS's grid layout for the "Explore" page. To do so, follow those steps :

1. Obtain the icons archive, it's usually reffered to as `RezolutionIcons.zip`. You can obtain it...
    * From the **Releases** page (see above)
    * Alongside the generated zips if you opted for the manual way. Note that it will only be generated if you answered "**Yes**" or "**Both**" to the prompt at the start of the generation script.
2. Put it into the `ARCHIVE` folder at the root of either `SD1` or `SD2`.
3. Go into `Apps` > `ArchiveManager` and select `[SDX] RezolutionIcons`. Wait for the installation script to finish.
4. Make sure to select a theme variant with grid support (they usually ends with `Grid`).

## Troubleshooting
### Your screen is blank and/or your system gets bricked
> Please go into your `MUOS/theme/active` folder and remove everything in there, your system should now boot and you can choose a different (not broken) theme. - [Harry](https://hmcneill46.github.io/muOS-MinUIfied-Theme-Generator/)

### An error occurred during the "generation" phase
- Make sure the version of Python you're using is recent enough. Also, make sure you're using `python3` instead of `python` in the command prompt.
	- If you're unsure, execute `python3 --version` (or `python --version` if the former yields an error).
- Make sure the message is an actual error. Some are just warns, meant to ease out debugging. Errors are usually prefixed by `🛑 >` (and not `⚠️ >`). 
	- Errors usually appears before the script stops. If you're using `bash`, execute `echo $?` to see the script's return code. If it's `0`, that means the script worked properly.
- If none of these steps solved your issue, send me a message on Discord by DMs (`@oiimrosabel`) with the error message, I'll help you troubleshoot the issue.

### The "Explore" menu is empty
That probably means you forgot to install the icon pack that goes alongside the themes. Refer to the **Grid support** section above to install it.