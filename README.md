# Maya-Video-Player  
A plugin for Autodesk Maya that adds a video player to play back rendered animations.  

## Installation Instructions:  
### Modify install.mel  
1. Change the $VERSION variable to be the year version of your Maya install.  
2. Change the $INSTALL_LOCATION variable to be the path to the downloaded repository.  

### Install and Activate Plugin
1. Drag ths install.mel file into your Maya viewport to begin installation.  
2. Go to **Windows** > **Settings/Preferences** > **Plug-in Manager**  
3. Find the video_command.py plugin and load it. 

## Usage:  
1. To use the video player, run the ```videoPlayer;``` MEL command in the script editor after rendering an animation. The player will detect the images based on your scenes render output settings. 
