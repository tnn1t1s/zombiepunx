
__DATA_DIR__ = "/home/david/artwork/zombiepunx/data"
__PUNK_DIR__ = f"{__DATA_DIR__}/punx/images/training";

def get_punk(id):
    """ returns a ndarray with loaded image
    """
    return mpimg.imread(f"""{__PUNK_DIR__}/punk{"%04d" % id}.png""")

def pixel_to_img(key, dim = (24,24)):
    """take pixel of format
       ""[0.37254903 0.11372549 0.03529412 1.0]"
       and return an image of size `dim` containing 
       only the pixel's color.
    """
    (x,y) = dim 
    c = np.fromstring(key[1:-1], float, sep=' ')
    return np.full((x, y, 4), c)

def flatten(img): 
  """convert (x,y,z) array containing a pixel in z-dimension 
     to an (x,y) array with str values for each (i,j)
     the intention is to make this easier to work with in ML
     training.
  """
  return np.array([[str(c) for c in row] 
                   for row in img])

def unflatten(img):
  """return a flattend image to valid .png format for display
  """  
  return np.array([[np.fromstring(c[1:-1], float, sep=' ') 
                    for c in row] for row in img])

def sort_dict_by_function_of_value(d, f = len):
  sorted_tuples = sorted(d.items(),
          key=lambda item: len(item[1]))
  return {k: v for k, v in sorted_tuples}

def add_index_to_colors(colors):
  """add a unique, sequential index to the entry for 
     each color. returned dictionary will be of form
     {`color_string`: { `"id": `int`, "punkIds" : `list[int`}}
  """
  i=0
  d={}
  for k in colors.keys():
    d[k] = {
      'id' : i,
      'punkIds' : colors[k]
    }
    i=i+1
  return d


