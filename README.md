# Maya-Video-Player  
A plugin for Autodesk Maya that adds a video player to play back rendered animations.  
![image](https://github.com/hannesdelbeke/Maya-Video-Player/assets/3758308/406feefd-7a98-4910-b90a-30a20eed066a)

## Installation

### plugget install
1. install [plugget for maya](https://github.com/plugget/plugget-qt-maya-plugin)
2. search for `video-player` and click install

### Manual install
<details>
<summary>Show instructions</summary>
  
### Modify install.mel  
1. Change the $VERSION variable to be the year version of your Maya install.  
2. Change the $INSTALL_LOCATION variable to be the path to the downloaded repository.  

### Install and Activate Plugin
1. Drag ths install.mel file into your Maya viewport to begin installation.  
2. Go to **Windows** > **Settings/Preferences** > **Plug-in Manager**  
3. Find the video_command.py plugin and load it. 

</details>



## Usage:  
Run the ```videoPlayer;``` MEL command in the script editor after rendering an animation.  
The player will detect the images based on your scenes render output settings. 

## references
- plugget manifest https://github.com/plugget/plugget-pkgs/tree/main/maya/video-player
