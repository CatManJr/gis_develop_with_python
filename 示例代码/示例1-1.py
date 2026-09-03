from arcpy import *
in_workspace = GetParameterAsText(0)
clipFeature = GetParameterAsText(1)
out_workspace = GetParameterAsText(2)
env.workspace = in_workspace
fcs = ListFeatureClasses()
for fc in fcs:
    outFeatureClass = out_workspace + "/clip_" + fc
    Clip_analysis(fc, clipFeature, outFeatureClass)