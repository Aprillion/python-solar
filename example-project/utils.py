import sunpy.map

def download_aia():
  from sunpy.data.sample import AIA_171_IMAGE
  return sunpy.map.Map(AIA_171_IMAGE)