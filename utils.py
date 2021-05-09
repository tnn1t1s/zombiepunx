"""Tools for working with Cryptopunk NFTs; this includes utilities for data analysis and image preparation for training machine learning models using Cryptopunks as training data. 

Functions:

    get_punk(id)
    pixel_to_img(pixel_str, dim)
    flatten(img)
    unflatten(img)
    sort_dict_by_function_of_value(d, f)
    add_index_to_colors(colors)

"""
import os
import requests
from collections import OrderedDict

__ROOT_DIR__ = os.path.dirname(os.path.abspath(__file__))
__PUNK_DIR__ = f"{__ROOT_DIR__}/data/punx/images/training";

def get_punk(id):
    '''
       Returns a ndarray with loaded image
    ''' 
    return mpimg.imread(f'''{__PUNK_DIR__}/punk{"%04d" % id}.png''')

def pixel_to_img(pixel_str, dim = (24,24)):
    '''
       Take pixel of format "[r,g,b,b]"
       and return an image of size `dim` containing 
       only the pixel's color.
    '''
    (x,y) = dim 
    c = np.fromstring(pixel_str[1:-1], float, sep=' ')
    return np.full((x, y, 4), c)

def flatten(img): 
  '''
     Convert (x,y,z) array containing a pixel in z-dimension 
     to an (x,y) array with str values for each (i,j)
     the intention is to make this easier to work with in ML
     training.
  '''
  return np.array([[str(c) for c in row] 
                   for row in img])

def unflatten(img):
  '''
     Return a flattend image to valid .png format for display
  '''  
  return np.array([[np.fromstring(c[1:-1], float, sep=' ') 
                    for c in row] for row in img])

def sort_dict_by_function_of_value(d, f = len):
  sorted_tuples = sorted(d.items(),
          key=lambda item: len(item[1]))
  return {k: v for k, v in sorted_tuples}

def add_index_to_colors(colors):
  '''
     Add a unique, sequential index to the entry for 
     each color. returned dictionary will be of form
     {`color_string`: { `"id": `int`, "punkIds" : `list[int`}}
  '''
  i=0
  d={}
  for k in colors.keys():
    d[k] = {
      'id' : i,
      'punkIds' : colors[k]
    }
    i=i+1
  return d

def get_attr_dict():
    '''
       Read the attr csv and populate a default dict
    '''
    d=OrderedDict()
    with open(f"{__ROOT_DIR__}/data/punx/list_attr_punx.csv") as f:
        for attr in f.read().split(','):
            d[attr]=-1
    return d

__ATTR_DICT__  = get_attr_dict()

def get_punk_attrs(id):
    '''
       Retrieve `id` cryptopunk from larvalabs.com,
       parse HTML to extract type and attribute list
       to return list of attributes
    '''
    typeClass="col-md-10 col-md-offset-1 col-xs-12"
    punk_html=requests.get(f"https://www.larvalabs.com/cryptopunks/details/{id}").text
    soup = BeautifulSoup(punk_html, 'html.parser')
    details = soup.find(id="punkDetails")

    punkType = camelCase(details.find(class_=typeClass).find('a').contents[0])

    attrs=[punkType]
    attrTags = details.find(class_ = "row detail-row")
    for attrTag in attrTags.find_all('a'):
        attrs.append(camelCase(attrTag.contents[0]))
    return attrs

def deepcopy(d):
    return {k:d[k] for k in d} 

def get_punk_dict(id):
   '''
      Retrieve a punk pages, pull type and attributes
      from HTML and return a dictionary of attribute to
      (-1,1) mapping where 1 is truthy for existence of 
      attribute
   '''
   od = {k:_ATTR_DICT[k] for k in __ATTR_DICT__} 
   attrs = get_punk_attrs(id)
   for attr in attrs:
      od[attr]=1
   return od

def get_punks(start, end):
    '''
      Retrieve punks in range `start` to `end`
    '''
    punks={}
    for id in range(start, end):
        punks[id] = get_punk_dict(id)
    return punks

def punks_to_csv(punks):
    '''
       Write `punks` to a csv
    '''
    return None

def punks_from_csv(fp):
    '''
       Read punks from a csv
    '''
    return {}







