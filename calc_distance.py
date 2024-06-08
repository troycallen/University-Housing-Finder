import·math
#·Function·to·calculate·the·distance·using·the·haversine·formula
def·haversine(lat1,·lon1,·lat2,·lon2):
  lat1,·lon1,·lat2,·lon2·=·map(math.radians,·[lat1,·lon1,·lat2,·lon2])
  dlat·=·lat2·-·lat1
  dlon·=·lon2·-·lon1
  a·=·math.sin(dlat·/·2)·**·2·+·math.cos(lat1)·*·math.cos(lat2)·*·math.sin(dlon·/·2)·**·2
  c·=·2·*·math.atan2(math.sqrt(a),·math.sqrt(1·-·a))
  earth_radius·=·3958.8
  distance·=·earth_radius·*·c
  return·distance

#·Read·the·CSV·file·into·a·DataFrame
file_path·=·'CleanOutput.csv'
df·=·pd.read_csv(file_path)

#·Georgia·Tech·Student·Center·coordinates
gt_lat,·gt_lon·=·33.774981,·-84.398066

#·Calculate·the·distance·for·each·row·and·add·it·as·a·new·column
df['distance']·=·df.apply(lambda·row:·haversine(gt_lat,·gt_lon,·row['latitude'],·row['longitude']),·axis=1)

#·Save·the·updated·DataFrame·to·a·new·CSV·file
output_file_path·=·'UpdatedOutput.csv'
df.to_csv(output_file_path,·index=False)
