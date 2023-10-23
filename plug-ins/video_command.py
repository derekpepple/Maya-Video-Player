import maya.api.OpenMaya as om
from maya import OpenMayaMPx as mpx
import maya.cmds as cmds
import ui.main as player

# Not sure if this is necessary
def maya_useNewAPI():
    pass

def initializePlugin(plugin):
    vendor = "Derek Pepple"
    version = "1.0.0"

    pluging_fn = om.MFnPlugin(plugin, vendor, version)

    try:
        pluging_fn.registerCommand(VideoPlayerCmd.COMMAND_NAME, VideoPlayerCmd.creator)
    except:
        om.MGlobal.displayError("Failed to register command {0}".format(VideoPlayerCmd))


def uninitializePlugin(plugin):
    plugin_fn = om.MFnPlugin(plugin)

    try:
        plugin_fn.deregisterCommand(VideoPlayerCmd.COMMAND_NAME)
    except:
        om.MGlobal.displayError("Failed to deregister command: {0}".format(VideoPlayerCmd))


class VideoPlayerCmd(mpx.MPxCommand):

    COMMAND_NAME = "videoPlayer"

    def __init__(self):
        super(VideoPlayerCmd, self).__init__()
    

    def doIt(self, args):
        print("doin it")
        projectRootDirectory = cmds.workspace(q=True, rootDirectory=True)
        firstImagePath = cmds.renderSettings(firstImageName=True, fullPath=True)[0]
        path = cmds.renderSettings(genericFrameImageName="#",fullPath=True)[0]

        
        # TODO: add params
        player.runInMaya(path, firstImagePath, projectRootDirectory)
        

    @classmethod
    def creator(cls):
        print("hello")
        return mpx.asMPxPtr(VideoPlayerCmd())