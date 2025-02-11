# Rezolution
**A simple, modern and elegant muOS theme inspired by GTK4.**

## Installation
### From the "Releases" page
1. Head over to the **Releases** page : [link](https://github.com/oiimrosabel/RezolutionMuOSTheme)
2. Find the most recent release
3. Download the zip with the variant you want
4. Move it to `/MUOS/theme/` (on the SD2, or SD1 if you use only one card)
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
3. Execute the "generators" script (important) :
```bash
bash ./generate.sh && bash ./zip.sh
```
4. Head over to the `__build` folder at the root of the project. You should find at least 3 zips, one for each color variant.
5. (**Optional**) If you plan to tinker with the theme (for example, to create your own), make sure to clean the `__build` folder by executing :
```bash
# cd ./__factory
bash ./clean.sh
```
6. Move the zips to the correct folder, as indicated above (from the 4th instruction onwards)

#### TL;DR
For convenience, you can copy-paste the following script into a `.sh` file and execute it using `bash` :

```bash
git clone https://github.com/oiimrosabel/RezolutionMuOSTheme.git
cd ./RezolutionMuOSTheme/__factory
bash ./generate.sh && bash ./zip.sh
cd ../__build
ls
```

## Troubleshooting
### Your screen is blank and/or your system gets bricked
> Please go into your `MUOS/theme/active` folder and remove everything in there, your system should now boot and you can choose a different (not broken) theme. - [Harry](https://hmcneill46.github.io/muOS-MinUIfied-Theme-Generator/)
### An error occurred during the "generation" phase
Send me a message on Discord by DMs (`@oiimrosabel`) with the error message, I'll help you troubleshoot the issue.

## Grid support
Grid support is still in development. For now, only the system icons are available (in the `__icons` folder), alongside the script to install them.

The "generators" script (specifically `zip.sh`) will generate an archive named `SystemIcons.zip`, similar to the one used for the **MinUIfied** theme. You'll only have to follow the steps described above to generate it. Then, you'll just have to follow the steps indicated [here](https://hmcneill46.github.io/muOS-MinUIfied-Theme-Generator/Grid-Theme-Gallery/) to install the icons, and use them with the **MinUIfied** theme.