import laspy 
import pandas as pd
# lazFile=laspy.file.File(r'D:\pensiveant\github\python-study\laspy\20120414_002130.laz', mode="r")
lazFile=laspy.file.File(r'D:\pensiveant\github\python-study\laspy\radar.las', mode="r")
scale=lazFile.header.scale
offset=lazFile.header.offset
x=lazFile.x
y=lazFile.y
z=lazFile.z
intensity=lazFile.Intensity
intensityUnique=pd.Series(intensity).unique()
classification=lazFile.Classification
classificationUnique=pd.Series(classification).unique()
# vlrs=lazFile.header.vlrs[0].to_byte_string()
point_records = lazFile.points
for point in point_records:
    print(1)