import AppKit
import shutil
import os
import tempfile

from drawBot.misc import executeExternalProcess, getExternalToolPath


def generateGif(inputPaths, outputPath, delays, loop=True):
    # Try to find gifsicle in system path first
    gifsicle = shutil.which('gifsicle')
    if not gifsicle:
        # Fallback to DrawBot's bundled gifsicle
        from drawBot.misc import getExternalToolPath
        root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        gifsicle = getExternalToolPath(root, "gifsicle")
    
    print(f"Using gifsicle at: {gifsicle}")
    
    cmds = [gifsicle, "--no-warnings", "--disposal=none"]
    if loop:
        cmds.extend(["--loopcount=forever"])
    for inputPath, delay in zip(inputPaths, delays):
        cmds.extend(["--delay", "%i" % delay, inputPath])
    cmds.append("--output")
    cmds.append(outputPath)
    print(f"Running command: {' '.join(cmds)}")
    executeExternalProcess(cmds)


_explodedGifCache = {}


def _explodeGif(path):
    gifsiclePath = getExternalToolPath(os.path.dirname(__file__), "gifsicle")
    if isinstance(path, AppKit.NSURL):
        path = path.path()
    destRoot = tempfile.mkdtemp()
    cmds = [
        gifsiclePath,
        # explode
        "--explode",
        # source path
        path
    ]
    executeExternalProcess(cmds, cwd=destRoot)
    files = os.listdir(destRoot)
    _explodedGifCache[path] = dict(
        source=destRoot,
        fileNames=sorted(files),
    )


def clearExplodedGifCache():
    for path, info in _explodedGifCache.items():
        shutil.rmtree(info["source"])
    _explodedGifCache.clear()


def gifFrameCount(path):
    if isinstance(path, AppKit.NSURL):
        path = path.path()
    if path not in _explodedGifCache:
        _explodeGif(path)
    frameCount = len(_explodedGifCache[path]["fileNames"])
    if frameCount == 0:
        return None
    return frameCount


def gifFrameAtIndex(path, index):
    if isinstance(path, AppKit.NSURL):
        path = path.path()
    if path not in _explodedGifCache:
        _explodeGif(path)
    source = _explodedGifCache[path]["source"]
    fileNames = _explodedGifCache[path]["fileNames"]
    fileName = os.path.join(source, fileNames[index])
    url = AppKit.NSURL.fileURLWithPath_(fileName)
    return AppKit.NSImage.alloc().initByReferencingURL_(url)
