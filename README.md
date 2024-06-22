<p align="center">
    <img src="https://github.com/IrtsaDevelopment/conarn/assets/139963912/5b365b42-4fdd-424a-a1da-a1e9590f5819"
        height="280">
</p>
<p align="center">
<a href="https://github.com/irtsa-dev/conarn/releases/tag/v1.1.0">
        <img src="https://img.shields.io/badge/release-1.1.0-brightgreen"
            alt="release"></a>
<a href="https://github.com/irtsa-dev/conarn/issues">
        <img src="https://custom-icon-badges.demolab.com/github/issues-raw/irtsa-dev/conarn?logo=issue"
            alt="issues"></a>
<a href="https://github.com/irtsa-dev/conarn/pulls">
        <img src="https://custom-icon-badges.demolab.com/github/issues/irtsa-dev/conarn?logo=git-pull-request"
            alt="pulls"></a>
</p>
<br />
<p align="center">
    <b>Conarn</b> is a save file editor for the game <a href="https://store.steampowered.com/app/2881650/Content_Warning/">Content Warning</a> by <b>Landfall</b>. 
</p>
<p align="center">
    <b>Conarn</b> utilizes <a href="https://github.com/python/cpython/blob/3.12/Lib/tkinter/__init__.py">Tkinter</a> and <a href="https://github.com/TomSchimansky/CustomTkinter">CustomTkinter</a> for the GUI along with <a href="https://github.com/pyinstaller/pyinstaller">pyinstaller</a> to package as an executable. Each release has the source and executable versions of the program available for download.
</p>
<br />
<p align="center">
    Reference the <a href="https://github.com/irtsa-dev/conarn/releases">Releases</a> for public releases including the source-code and executable.
</p>
<br />
<br />
<br />
<br />

## Usage
Depending on if you downloaded the source code directly or the executable, you will run **conarn.pyw** or **conarn.exe** respectively. Once ran, it will recognize any current saves where **Content Warning** save files are stored. 
<br />
<br />
*(This is typically at C:/Users/[USERNAME]/AppData/LocalLow/Landfall Games/Content Warning/Saves which is where it will check)*
<br />
<br />
<br />
It will display any found files for you to edit.
<p align="left">
    <img src="https://github.com/IrtsaDevelopment/conarn/assets/139963912/a055dcdd-7b8b-4727-99ea-f13357c14ca5"
        height="200">
</p>
<br />
<br />
Selecting a file will bring up the editor for said file.
<p align="left">
    <img src="https://github.com/IrtsaDevelopment/conarn/assets/139963912/7b613928-59a5-4523-a27e-0fb50cba8c60"
        height="350">
</p>
<br />
<br />
<br />
<br />
<br />

## Notices
- If you ever get the message *"There was an error in saving"*, it means you have entered a value that cannot be accepted.
  - The **Seed** can only be **3** digits long and supprts numbers only.
  - The **Money** can only be set to values **999,999** and below.
  - The **Views** can only be set to values **300,000,000** and below.

- The ability to edit "Network Deals" will be added, hence functions and sections of codes that are there to allow for this future feature.
