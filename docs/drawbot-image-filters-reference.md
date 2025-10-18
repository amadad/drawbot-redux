# DrawBot ImageObject Filters Reference

This reference covers advanced image manipulation filters available on ImageObject instances. These are specialized effects primarily for photo manipulation and creative image processing.

## Getting Started with ImageObject

```python
# Create ImageObject from file
img = db.ImageObject("path/to/image.jpg")

# Apply filters (filters chain)
img.gaussianBlur(10)
img.saturationAdjust(0.5)

# Draw the filtered image
db.image(img, (x, y))

# You can also pass an ImageObject to image()
db.image("path/to/image.jpg", (x, y))  # Direct path still works
```

## Blur Filters

```python
img.gaussianBlur(radius)               # Standard Gaussian blur
img.boxBlur(radius)                    # Box blur (faster)
img.discBlur(radius)                   # Disc-shaped blur
img.motionBlur(radius, angle)          # Motion blur effect
img.zoomBlur(center, amount)           # Radial zoom blur
img.maskedVariableBlur(mask, radius)   # Variable blur using mask
```

## Color Adjustments

```python
img.colorControls(saturation, brightness, contrast)
img.exposureAdjust(exposure)           # Exposure adjustment
img.gammaAdjust(power)                 # Gamma correction
img.hueAdjust(angle)                   # Rotate hue
img.vibrance(amount)                   # Vibrance adjustment
img.whitePointAdjust(color)            # White point adjustment
img.temperatureAndTint(temp, tint)     # Color temperature
img.highlightShadowAdjust(highlight, shadow, radius)
img.sepiaTone(intensity)               # Sepia effect
img.colorInvert()                      # Invert colors
img.colorMonochrome(color, intensity)  # Monochrome tint
img.colorPosterize(levels)             # Posterize effect
img.falseColor(color0, color1)         # False color mapping
```

## Stylize Effects

```python
img.pixellate(scale)                   # Pixelate effect
img.crystallize(radius, center)        # Crystallize effect
img.pointillize(radius, center)        # Pointillism effect
img.edges(intensity)                   # Edge detection
img.edgeWork(radius)                   # Edge highlighting
img.comicEffect()                      # Comic book style
img.bloom(radius, intensity)           # Bloom glow effect
img.gloom(radius, intensity)           # Gloom darkening effect
img.vignette(radius, intensity)        # Vignette darkening
img.vignetteEffect(center, radius, intensity, falloff)
```

## Distortion Effects

```python
img.bumpDistortion(center, radius, scale)
img.bumpDistortionLinear(center, radius, angle, scale)
img.circleSplashDistortion(center, radius)
img.circularWrap(center, radius, angle)
img.holeDistortion(center, radius)
img.pinchDistortion(center, radius, scale)
img.torusLensDistortion(center, radius, width, refraction)
img.twirlDistortion(center, radius, angle)
img.vortexDistortion(center, radius, angle)
img.displacementDistortion(displacementImage, scale)
img.glassDistortion(texture, center, scale)
img.glassLozenge(point0, point1, radius, refraction)
img.perspectiveCorrection(topLeft, topRight, bottomRight, bottomLeft)
img.perspectiveTransform(topLeft, topRight, bottomRight, bottomLeft)
img.straightenFilter(angle)
```

## Sharpen & Detail

```python
img.sharpenLuminance(sharpness, radius)
img.unsharpMask(radius, intensity)     # Unsharp mask sharpening
img.noiseReduction(level, sharpness)   # Remove noise
```

## Tile & Pattern Effects

```python
img.affineTile(transform)
img.affineClamp(transform)
img.eightfoldReflectedTile(center, angle, width)
img.fourfoldReflectedTile(center, angle, width)
img.fourfoldRotatedTile(center, angle, width)
img.fourfoldTranslatedTile(center, angle, width)
img.glideReflectedTile(center, angle, width)
img.kaleidoscope(center, count, angle)
img.opTile(center, scale, angle, width)
img.parallelogramTile(center, angle, width)
img.perspectiveTile(topLeft, topRight, bottomRight, bottomLeft)
img.sixfoldReflectedTile(center, angle)
img.sixfoldRotatedTile(center, angle, width)
img.triangleKaleidoscope(point, size, rotation, decay)
img.triangleTile(center, angle, width)
img.twelvefoldReflectedTile(center, angle, width)
```

## Blend Modes (ImageObject)

```python
# Composite two images with blend modes
img.normalBlendMode(backgroundImage)
img.multiplyBlendMode(backgroundImage)
img.screenBlendMode(backgroundImage)
img.overlayBlendMode(backgroundImage)
img.darkenBlendMode(backgroundImage)
img.lightenBlendMode(backgroundImage)
img.colorDodgeBlendMode(backgroundImage)
img.colorBurnBlendMode(backgroundImage)
img.softLightBlendMode(backgroundImage)
img.hardLightBlendMode(backgroundImage)
img.differenceBlendMode(backgroundImage)
img.exclusionBlendMode(backgroundImage)
img.hueBlendMode(backgroundImage)
img.saturationBlendMode(backgroundImage)
img.colorBlendMode(backgroundImage)
img.luminosityBlendMode(backgroundImage)

# More blend modes
img.linearBurnBlendMode(backgroundImage)
img.linearDodgeBlendMode(backgroundImage)
img.linearLightBlendMode(backgroundImage)
img.pinLightBlendMode(backgroundImage)
img.vividLightBlendMode(backgroundImage)
img.divideBlendMode(backgroundImage)
img.subtractBlendMode(backgroundImage)
```

## Compositing Operations

```python
img.additionCompositing(backgroundImage)
img.maximumCompositing(backgroundImage)
img.minimumCompositing(backgroundImage)
img.multiplyCompositing(backgroundImage)
img.sourceAtopCompositing(backgroundImage)
img.sourceInCompositing(backgroundImage)
img.sourceOutCompositing(backgroundImage)
img.sourceOverCompositing(backgroundImage)
```

## Halftone & Screens

```python
img.circularScreen(center, width, sharpness)
img.CMYKHalftone(center, width, angle, sharpness, gcr, ucr)
img.dotScreen(center, angle, width)
img.hatchedScreen(center, angle, width, sharpness)
img.lineScreen(center, angle, width, sharpness)
```

## Generators (Create images from scratch)

```python
img = db.ImageObject()
img.checkerboardGenerator(center, color0, color1, width, sharpness)
img.constantColorGenerator(color)
img.lenticularHaloGenerator(center, color, striationStrength, striationContrast, time)
img.starShineGenerator(center, color, radius, crossScale, crossAngle, crossOpacity, crossWidth, epsilon)
img.stripesGenerator(center, color0, color1, width, sharpness)
img.sunbeamsGenerator(center, color, sunRadius, maxStriationRadius, striationStrength, striationContrast, time)

# Barcode generators
img.QRCodeGenerator(message, correctionLevel="M")
img.code128BarcodeGenerator(message, quietSpace, barcodeHeight)
img.PDF417BarcodeGenerator(message, minWidth, maxWidth, minHeight, maxHeight, dataColumns, rows, preferredAspectRatio, compactionMode, compactStyle, correctionLevel, alwaysSpecifyCompaction)
img.aztecCodeGenerator(message, correctionLevel, layers, compactStyle)

# Shape generators
img.randomGenerator()
img.roundedRectangleGenerator(extent, radius, color)
img.blurredRectangleGenerator(extent, sigma, color)
img.roundedRectangleStrokeGenerator(extent, radius, strokeWidth, color)

# Gradient generators
img.gaussianGradient(center, color0, color1, radius)
img.linearGradient(point0, point1, color0, color1)
img.radialGradient(center, radius, color0, color1)
img.smoothLinearGradient(point0, point1, color0, color1)
```

## Transition Effects (Between two images)

```python
img.accordionFoldTransition(targetImage, time, bottomHeight, numberOfFolds, foldShadowAmount)
img.barsSwipeTransition(targetImage, time, angle, width, barOffset)
img.copyMachineTransition(targetImage, time, extent, color, angle, width, opacity)
img.disintegrateWithMaskTransition(targetImage, time, maskImage, shadowRadius, shadowDensity, shadowOffset)
img.dissolveTransition(targetImage, time)
img.flashTransition(targetImage, time, center, extent, color, maxStriationRadius, striationStrength, striationContrast, fadeThreshold)
img.modTransition(targetImage, time, center, angle, radius, compression)
img.pageCurlTransition(targetImage, time, extent, angle, radius, shadowSize, shadowAmount, shadowExtent)
img.pageCurlWithShadowTransition(targetImage, time, extent, angle, radius, shadowSize, shadowAmount, shadowExtent)
img.rippleTransition(targetImage, time, center, extent, width, scale)
img.swipeTransition(targetImage, time, extent, color, angle, width, opacity)
```

## Advanced Color Science

```python
img.colorAbsoluteDifference(targetImage)
img.colorCrossPolynomial(redCoefficients, greenCoefficients, blueCoefficients)
img.colorPolynomial(redCoefficients, greenCoefficients, blueCoefficients, alphaCoefficients)
img.colorThreshold(threshold)
img.colorThresholdOtsu()
img.labDeltaE(image2)
img.convertLabToRGB()
img.convertRGBtoLab()
img.linearToSRGBToneCurve()
img.SRGBToneCurveToLinear()
```

## Mask Operations

```python
img.blendWithAlphaMask(backgroundImage, maskImage)
img.blendWithBlueMask(backgroundImage, maskImage)
img.blendWithMask(backgroundImage, maskImage)
img.blendWithRedMask(backgroundImage, maskImage)
img.maskToAlpha()
```

## Analysis & Measurement

```python
img.areaAverage(extent)
img.areaHistogram(extent, count, scale)
img.areaLogarithmicHistogram(extent, count, scale)
img.areaMaximum(extent)
img.areaMaximumAlpha(extent)
img.areaMinimum(extent)
img.areaMinimumAlpha(extent)
img.areaMinMax(extent)
img.areaMinMaxRed(extent)
img.columnAverage(extent)
img.rowAverage(extent)
img.histogramDisplayFilter(height, highLimit, lowLimit)
img.KMeans(extent, count, passes)
img.paletteCentroid(paletteImage)
img.palettize(paletteImage, perceptual)
```

## ML & Computer Vision

```python
img.personSegmentation()
img.saliencyMapFilter()
img.depthOfField(point0, point1, saturation, radius, unsharpMaskRadius, unsharpMaskIntensity)
img.depthToDisparity()
img.disparityToDepth()
img.edgePreserveUpsampleFilter(smallImage, spatialSigma, lumaSigma)
```

## Gradient & Edge Detection

```python
img.gaborGradients(radius)
img.sobelGradients()
img.cannyEdgeDetector(sigma, low, high)
img.morphologyGradient(radius)
```

## Morphological Operations

```python
img.morphologyMaximum(radius)
img.morphologyMinimum(radius)
img.morphologyRectangleMaximum(width, height)
img.morphologyRectangleMinimum(width, height)
```

## Utility Filters

```python
img.clamp(extent)
img.colorClamp(minComponents, maxComponents)
img.crop(rectangle)
img.lanczosScaleTransform(scale, aspectRatio)
img.mix(backgroundImage, amount)
img.ninePartStretched(growthBounds, centerBounds)
img.ninePartTiled(growthBounds, centerBounds)
img.offset(offset)
img.sampleNearest()
img.stretchCrop(size, cropAmount, centerStretchAmount)

# Image info
size = img.size()                  # Get (width, height)
img.copy()                         # Create a copy
```

## Filter Management

```python
img.clearFilters()                 # Remove all filters

# Lock/unlock for drawing into ImageObject
img.lockFocus()
# ... draw with db.rect(), db.text(), etc.
img.unlockFocus()
```

## When to Use These Filters

**For Editorial/Poster Design** (common):
- Color adjustments (exposureAdjust, colorControls, hueAdjust)
- Blur effects (gaussianBlur, motionBlur)
- Stylize (pixellate, edges, bloom, vignette)

**For Photo Manipulation** (specialized):
- All the distortion effects
- Advanced color science
- Halftone screens

**For Generative Art** (creative):
- Tile & pattern effects
- Generators
- Blend modes

**For Animation** (motion):
- Transition effects between frames

## Example Usage

```python
# Load and process an image
img = db.ImageObject("photo.jpg")

# Apply filter chain
img.exposureAdjust(0.2)            # Brighten
img.colorControls(1.2, 0, 1.1)     # Increase saturation & contrast
img.gaussianBlur(2)                # Subtle blur
img.vignette(1.0, 0.5)             # Add vignette

# Draw it
db.newPage(1000, 1000)
db.image(img, (0, 0, db.width(), db.height()))
```

## Resources

- Full filter documentation: http://www.drawbot.com
- Most filters are wrappers for Core Image filters
- See Apple's Core Image Filter Reference for parameter details
