import AppKit
import shutil
import os
import tempfile

from drawBot.misc import executeExternalProcess, getExternalToolPath
from pygifsicle import gifsicle

def generateGif(sourcePaths, destPath, delays, loop=True):
    options = ["--colors", "256"]
    if loop:
        options.append("--loop")
    
    for i, delay in enumerate(delays):
        options.extend(["--delay", str(delay)])
    
    gifsicle(
        sources=sourcePaths,
        destination=destPath,
        optimize=False,
        colors=256,
        options=options
    )
    
    # remove the temp input gifs
    for inputPath in sourcePaths:
        os.remove(inputPath)


_explodedGifCache = {}


def _explodeGif(path):
    if isinstance(path, AppKit.NSURL):
        path = path.path()
    destRoot = tempfile.mkdtemp()
    
    gifsicle(
        sources=[path],
        destination=destRoot,
        explode=True
    )
    
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
