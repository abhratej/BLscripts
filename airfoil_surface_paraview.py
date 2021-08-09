# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *

# create a new 'Legacy VTK Reader'
surface_flowvtk = LegacyVTKReader(FileNames=['./surface_flow.vtk'])


# save data
SaveData('./output/airfoil.tsv', proxy=surface_flowvtk, Precision=10,
    UseScientificNotation=1,
    FieldDelimiter='\t')