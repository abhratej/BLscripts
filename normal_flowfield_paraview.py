# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

# import the simple module from the paraview
from paraview.simple import *

# create a new 'Legacy VTK Reader'
flowvtk = LegacyVTKReader(FileNames=['./flow.vtk'])

# Read airfoil and normal data
with open('./output/airfoil_normals.txt') as airfoilData:
	content = airfoilData.readlines()
airfoilCoord = []
for line in content:
	temp = line.split()
	temp = list(map(float,temp))
	airfoilCoord.append(temp)

print(airfoilCoord[0][0], airfoilCoord[0][1], len(airfoilCoord), len(airfoilCoord)/2)

# create a new 'Python Calculator'
pythonCalculator1 = PythonCalculator(Input=flowvtk)
pythonCalculator1.ArrayName = 'vorticity'
pythonCalculator1.Expression = 'curl(Velocity)'


# create a new 'Clip'
clip1 = Clip(Input=pythonCalculator1)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'Pressure']
clip1.Value = 0.1480841264128685

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [8.271697998046875, 0.0, 0.0]

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [0.0, 0.0, 0.0]
clip1.ClipType.Normal = [airfoilCoord[0][1], 1.0, 0.0]

# rename source object
RenameSource('lower_half', clip1)

# create a new 'Clip'
clip1_1 = Clip(Input=pythonCalculator1)
clip1_1.ClipType = 'Plane'
clip1_1.Scalars = ['POINTS', 'Pressure']
clip1_1.Value = 0.1480841264128685

# init the 'Plane' selected for 'ClipType'
clip1_1.ClipType.Origin = [8.271697998046875, 0.0, 0.0]

# Properties modified on clip1_1.ClipType
clip1_1.ClipType.Origin = [0.0, 0.0, 0.0]
clip1_1.ClipType.Normal = [airfoilCoord[0][1], 1.0, 0.0]

# Properties modified on clip1_1
clip1_1.Invert = 0

# rename source object
RenameSource('upper_half', clip1_1)

for i in range(0, len(airfoilCoord), 1):
	p1x = airfoilCoord[i][0]
	p1y = airfoilCoord[i][1]
	n1x = airfoilCoord[i][2]
	n1y = airfoilCoord[i][3]
	if (i < len(airfoilCoord)/2):
		# create a new 'Slice'
		slice1 = Slice(Input=clip1)
		slice1.SliceType = 'Plane'
		slice1.SliceOffsetValues = [0.0]
	else:
		# create a new 'Slice'
		slice1 = Slice(Input=clip1_1)
		slice1.SliceType = 'Plane'
		slice1.SliceOffsetValues = [0.0]

	# Properties modified on slice1.SliceType
	slice1.SliceType.Origin = [p1x, p1y, 0.0]
	slice1.SliceType.Normal = [n1x, n1y, 0.0]

	# create a new 'Calculator'
	calculator1 = Calculator(Input=slice1)
	calculator1.ResultArrayName = 'velocity_magnitude'
	calculator1.Function = 'mag(Velocity)'

	# create a new 'Calculator'
	calculator2 = Calculator(Input=calculator1)
	calculator2.ResultArrayName = 'vorticity_magnitude'
	calculator2.Function = 'mag(vorticity)'

	# save data
	SaveData('./output/normalflowfields/flow_along_normal_point'+str(i+1)+'.tsv', proxy=calculator2, Precision=8,
				UseScientificNotation=1, FieldDelimiter='\t')
