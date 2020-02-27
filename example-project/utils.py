import sunpy.map

def peek_aia(img):
  aia = sunpy.map.Map(img)
  aia.peek()