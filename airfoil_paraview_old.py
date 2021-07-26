# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
flowvtk = LegacyVTKReader(registrationName='flow.vtk', FileNames=['/home/abhratej/github/BLscripts/flow.vtk'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
flowvtkDisplay = Show(flowvtk, renderView1)

# get color transfer function/color map for 'Pressure'
pressureLUT = GetColorTransferFunction('Pressure')

# get opacity transfer function/opacity map for 'Pressure'
pressurePWF = GetOpacityTransferFunction('Pressure')

# trace defaults for the display properties.
flowvtkDisplay.Representation = 'Surface'
flowvtkDisplay.ColorArrayName = ['POINTS', 'Pressure']
flowvtkDisplay.LookupTable = pressureLUT
flowvtkDisplay.SelectTCoordArray = 'None'
flowvtkDisplay.SelectNormalArray = 'None'
flowvtkDisplay.SelectTangentArray = 'None'
flowvtkDisplay.OSPRayScaleArray = 'Pressure'
flowvtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
flowvtkDisplay.SelectOrientationVectors = 'Velocity'
flowvtkDisplay.ScaleFactor = 101.56136474609376
flowvtkDisplay.SelectScaleArray = 'Pressure'
flowvtkDisplay.GlyphType = 'Arrow'
flowvtkDisplay.GlyphTableIndexArray = 'Pressure'
flowvtkDisplay.GaussianRadius = 5.078068237304688
flowvtkDisplay.SetScaleArray = ['POINTS', 'Pressure']
flowvtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
flowvtkDisplay.OpacityArray = ['POINTS', 'Pressure']
flowvtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
flowvtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
flowvtkDisplay.PolarAxes = 'PolarAxesRepresentation'
flowvtkDisplay.ScalarOpacityFunction = pressurePWF
flowvtkDisplay.ScalarOpacityUnitDistance = 23.117843821969718
flowvtkDisplay.OpacityArrayName = ['POINTS', 'Pressure']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
flowvtkDisplay.ScaleTransferFunction.Points = [-0.20414794981479645, 0.0, 0.5, 0.0, 0.5003162026405334, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
flowvtkDisplay.OpacityTransferFunction.Points = [-0.20414794981479645, 0.0, 0.5, 0.0, 0.5003162026405334, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [8.271697998046875, 0.0, 10000.0]
renderView1.CameraFocalPoint = [8.271697998046875, 0.0, 0.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
flowvtkDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Python Calculator'
pythonCalculator1 = PythonCalculator(registrationName='PythonCalculator1', Input=flowvtk)
pythonCalculator1.Expression = ''

# Properties modified on pythonCalculator1
pythonCalculator1.Expression = 'curl(Velocity)'
pythonCalculator1.ArrayName = 'Vorticity'

# show data in view
pythonCalculator1Display = Show(pythonCalculator1, renderView1)

# trace defaults for the display properties.
pythonCalculator1Display.Representation = 'Surface'
pythonCalculator1Display.ColorArrayName = ['POINTS', 'Pressure']
pythonCalculator1Display.LookupTable = pressureLUT
pythonCalculator1Display.SelectTCoordArray = 'None'
pythonCalculator1Display.SelectNormalArray = 'None'
pythonCalculator1Display.SelectTangentArray = 'None'
pythonCalculator1Display.OSPRayScaleArray = 'Pressure'
pythonCalculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
pythonCalculator1Display.SelectOrientationVectors = 'Velocity'
pythonCalculator1Display.ScaleFactor = 101.56136474609376
pythonCalculator1Display.SelectScaleArray = 'Pressure'
pythonCalculator1Display.GlyphType = 'Arrow'
pythonCalculator1Display.GlyphTableIndexArray = 'Pressure'
pythonCalculator1Display.GaussianRadius = 5.078068237304688
pythonCalculator1Display.SetScaleArray = ['POINTS', 'Pressure']
pythonCalculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
pythonCalculator1Display.OpacityArray = ['POINTS', 'Pressure']
pythonCalculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
pythonCalculator1Display.DataAxesGrid = 'GridAxesRepresentation'
pythonCalculator1Display.PolarAxes = 'PolarAxesRepresentation'
pythonCalculator1Display.ScalarOpacityFunction = pressurePWF
pythonCalculator1Display.ScalarOpacityUnitDistance = 23.117843821969718
pythonCalculator1Display.OpacityArrayName = ['POINTS', 'Pressure']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pythonCalculator1Display.ScaleTransferFunction.Points = [-0.20414794981479645, 0.0, 0.5, 0.0, 0.5003162026405334, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pythonCalculator1Display.OpacityTransferFunction.Points = [-0.20414794981479645, 0.0, 0.5, 0.0, 0.5003162026405334, 1.0, 0.5, 0.0]

# hide data in view
Hide(flowvtk, renderView1)

# show color bar/color legend
pythonCalculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

RenameProxy('Flowfield_with_Vorticity', 'sources', pythonCalculator1)

# rename source object
RenameSource('Flowfield_with_Vorticity', pythonCalculator1)

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=pythonCalculator1)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'Pressure']
clip1.Value = 0.1480841264128685

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [8.271697998046875, 0.0, 0.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [8.271697998046875, 0.0, 0.0]

# Properties modified on clip1
clip1.Invert = 0

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [0.0, 0.0, 0.0]
clip1.ClipType.Normal = [1.0, 5.35220011e-08, 0.0]

# show data in view
clip1Display = Show(clip1, renderView1)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'Pressure']
clip1Display.LookupTable = pressureLUT
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'None'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleArray = 'Pressure'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'Velocity'
clip1Display.ScaleFactor = 101.56136474609376
clip1Display.SelectScaleArray = 'Pressure'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'Pressure'
clip1Display.GaussianRadius = 5.078068237304688
clip1Display.SetScaleArray = ['POINTS', 'Pressure']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'Pressure']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = pressurePWF
clip1Display.ScalarOpacityUnitDistance = 20.145453241790385
clip1Display.OpacityArrayName = ['POINTS', 'Pressure']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [-0.20414794981479645, 0.0, 0.5, 0.0, 0.5003162026405334, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [-0.20414794981479645, 0.0, 0.5, 0.0, 0.5003162026405334, 1.0, 0.5, 0.0]

# hide data in view
Hide(pythonCalculator1, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on clip1.ClipType
clip1.ClipType.Normal = [5.35220011e-08, 1.0, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(pythonCalculator1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1.ClipType)

# hide data in view
Hide(clip1, renderView1)

# set active source
SetActiveSource(pythonCalculator1)

# show data in view
pythonCalculator1Display = Show(pythonCalculator1, renderView1)

# show color bar/color legend
pythonCalculator1Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# create a new 'Clip'
clip2 = Clip(registrationName='Clip2', Input=pythonCalculator1)
clip2.ClipType = 'Plane'
clip2.HyperTreeGridClipper = 'Plane'
clip2.Scalars = ['POINTS', 'Pressure']
clip2.Value = 0.1480841264128685

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [8.271697998046875, 0.0, 0.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip2.HyperTreeGridClipper.Origin = [8.271697998046875, 0.0, 0.0]

# Properties modified on clip2.ClipType
clip2.ClipType.Origin = [0.0, 0.0, 0.0]
clip2.ClipType.Normal = [5.35220011e-08, 1.0, 0.0]

# show data in view
clip2Display = Show(clip2, renderView1)

# trace defaults for the display properties.
clip2Display.Representation = 'Surface'
clip2Display.ColorArrayName = ['POINTS', 'Pressure']
clip2Display.LookupTable = pressureLUT
clip2Display.SelectTCoordArray = 'None'
clip2Display.SelectNormalArray = 'None'
clip2Display.SelectTangentArray = 'None'
clip2Display.OSPRayScaleArray = 'Pressure'
clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip2Display.SelectOrientationVectors = 'Velocity'
clip2Display.ScaleFactor = 98.54566040039063
clip2Display.SelectScaleArray = 'Pressure'
clip2Display.GlyphType = 'Arrow'
clip2Display.GlyphTableIndexArray = 'Pressure'
clip2Display.GaussianRadius = 4.927283020019531
clip2Display.SetScaleArray = ['POINTS', 'Pressure']
clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display.OpacityArray = ['POINTS', 'Pressure']
clip2Display.OpacityTransferFunction = 'PiecewiseFunction'
clip2Display.DataAxesGrid = 'GridAxesRepresentation'
clip2Display.PolarAxes = 'PolarAxesRepresentation'
clip2Display.ScalarOpacityFunction = pressurePWF
clip2Display.ScalarOpacityUnitDistance = 22.82549344865222
clip2Display.OpacityArrayName = ['POINTS', 'Pressure']

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip2Display.ScaleTransferFunction.Points = [-0.20414794981479645, 0.0, 0.5, 0.0, 0.5003162026405334, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip2Display.OpacityTransferFunction.Points = [-0.20414794981479645, 0.0, 0.5, 0.0, 0.5003162026405334, 1.0, 0.5, 0.0]

# hide data in view
Hide(pythonCalculator1, renderView1)

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(clip1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip2.ClipType)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# rename source object
RenameSource('Upper_Half', clip1)

# set active source
SetActiveSource(clip2)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1.ClipType)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip2.ClipType)

# rename source object
RenameSource('Lower_Half', clip2)

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=clip2)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [8.271697998046875, -253.90339890069117, 0.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [8.271697998046875, -253.90339890069117, 0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [1.0, 5.35220011e-08, 0.0]
slice1.SliceType.Normal = [-0.990116715, -0.140245423, 0.0]

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'Pressure']
slice1Display.LookupTable = pressureLUT
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleArray = 'Pressure'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'Velocity'
slice1Display.ScaleFactor = 50.733142084491554
slice1Display.SelectScaleArray = 'Pressure'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'Pressure'
slice1Display.GaussianRadius = 2.5366571042245774
slice1Display.SetScaleArray = ['POINTS', 'Pressure']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'Pressure']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [-0.004064088687300682, 0.0, 0.5, 0.0, 0.12231022864580154, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [-0.004064088687300682, 0.0, 0.5, 0.0, 0.12231022864580154, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip2, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=slice1)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'Velocity_Magnitude'
calculator1.Function = 'mag(Velocity)'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'Velocity_Magnitude'
velocity_MagnitudeLUT = GetColorTransferFunction('Velocity_Magnitude')

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', 'Velocity_Magnitude']
calculator1Display.LookupTable = velocity_MagnitudeLUT
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'Velocity_Magnitude'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'Velocity'
calculator1Display.ScaleFactor = 50.733142084491554
calculator1Display.SelectScaleArray = 'Velocity_Magnitude'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'Velocity_Magnitude'
calculator1Display.GaussianRadius = 2.5366571042245774
calculator1Display.SetScaleArray = ['POINTS', 'Velocity_Magnitude']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'Velocity_Magnitude']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [0.00016594625016330282, 0.0, 0.5, 0.0, 1.0040594152495343, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [0.00016594625016330282, 0.0, 0.5, 0.0, 1.0040594152495343, 1.0, 0.5, 0.0]

# hide data in view
Hide(slice1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'Velocity_Magnitude'
velocity_MagnitudePWF = GetOpacityTransferFunction('Velocity_Magnitude')

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=calculator1)
calculator2.Function = ''

# Properties modified on calculator2
calculator2.ResultArrayName = 'Vorticity_Magnitude'
calculator2.Function = 'mag(Vorticity)'

# show data in view
calculator2Display = Show(calculator2, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'Vorticity_Magnitude'
vorticity_MagnitudeLUT = GetColorTransferFunction('Vorticity_Magnitude')

# trace defaults for the display properties.
calculator2Display.Representation = 'Surface'
calculator2Display.ColorArrayName = ['POINTS', 'Vorticity_Magnitude']
calculator2Display.LookupTable = vorticity_MagnitudeLUT
calculator2Display.SelectTCoordArray = 'None'
calculator2Display.SelectNormalArray = 'None'
calculator2Display.SelectTangentArray = 'None'
calculator2Display.OSPRayScaleArray = 'Vorticity_Magnitude'
calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display.SelectOrientationVectors = 'Velocity'
calculator2Display.ScaleFactor = 50.733142084491554
calculator2Display.SelectScaleArray = 'Vorticity_Magnitude'
calculator2Display.GlyphType = 'Arrow'
calculator2Display.GlyphTableIndexArray = 'Vorticity_Magnitude'
calculator2Display.GaussianRadius = 2.5366571042245774
calculator2Display.SetScaleArray = ['POINTS', 'Vorticity_Magnitude']
calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator2Display.OpacityArray = ['POINTS', 'Vorticity_Magnitude']
calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
calculator2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator2Display.ScaleTransferFunction.Points = [8.561172153139461e-12, 0.0, 0.5, 0.0, 1496.6857159475924, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator2Display.OpacityTransferFunction.Points = [8.561172153139461e-12, 0.0, 0.5, 0.0, 1496.6857159475924, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'Vorticity_Magnitude'
vorticity_MagnitudePWF = GetOpacityTransferFunction('Vorticity_Magnitude')

# save data
SaveData('/home/abhratej/github/BLscripts/flow_along_normal.tsv', proxy=calculator2, PointDataArrays=['Density', 'Eddy_Viscosity', 'Heat_Flux', 'Laminar_Viscosity', 'Nu_Tilde', 'Pressure', 'Pressure_Coefficient', 'Skin_Friction_Coefficient', 'Velocity', 'Velocity_Magnitude', 'Vorticity', 'Vorticity_Magnitude', 'Y_Plus'],
    UseScientificNotation=1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1525, 778)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [8.271697998046875, 0.0, 2733.8231965420196]
renderView1.CameraFocalPoint = [8.271697998046875, 0.0, 0.0]
renderView1.CameraParallelScale = 707.5655092081264

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).