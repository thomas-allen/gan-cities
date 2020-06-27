from typing import List, Dict
import numpy as np

# Placeholder imports
import imageio

class CityGenerator():
  """
  City generator class
  """

  def train(self, folder: str) -> None:
    """
    Train the generator given a set of training maps
    Args:
      folder: Folder in which training maps are contained
    """

  def setHeightmapPng(self, map: List[int]) -> None:
    """
    Load a PNG heightmap representing terrain to generate a city on top of.
    Args:
      map: A list of integers representing a PNG heightmap in RGBA format.
    """
    pass

  def getParams(self) -> Dict[str, any]:
    """
    Get parameters currently associated with the generator
    """
    pass

  def setCountryStyle(self, country: str) -> None:
    """
    Generate a city emulating the style of cities from a given country
    Args:
      country: The country name
    """
    pass

  def getValidCountries(self) -> List[str]:
    """
    Return a list of countries whose cities the generator was trained on
    Return:
      List[str]: List of countries names
    """
    return ['USA', 'Canada', 'China'] # Placeholder

  def setCityPop(self, pop: int) -> None:
    """
    Set the population of the generated city
    Args:
      pop: The city population
    """
    pass

  def setDimensions(self, width: int, height: int) -> None:
    """
    Set the dimensions of the generated city image
    Args:
      width: The width of the generated PNG image
      height: The height of the generated PNG image
    """
    pass

  def generateMap(self) -> None:
    """
    Generate a PNG map of given size
    """
    pass

  def getGeneratedMap(self) -> List[int]:
    """
    Get the RGB map data for the previously generated map.

    Returns:
      A list of integers representing pixel values in RGB format
    """
    # Placeholder image loading
    image = imageio.imread('placeholder/placeholder_map.png')
    image = np.array(image)

    # Image is in RGBA format, strip alpha channel
    imageRgb = image[:, :, :3]
    return imageRgb

  def saveGeneratedMap(self, data, filename):
    """
    Take a numpy array previously generated and saves as a PNG file 
    to the location specified by filename. filename should expect a complete
    URI, including file:///
   """
  pass