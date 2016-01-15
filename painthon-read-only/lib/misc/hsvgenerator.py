import math
import pygtk
pygtk.require("2.0")
import gtk
 
class HSVGenerator:       
   def get_hsv_color(self, hue, sat, val):
      hue = hue % 360

      min = 1.0-sat
      max = val
      interval = max - min

      red = min + self.__get_red(hue) * interval
      green = min + self.__get_green(hue) * interval
      blue = min + self.__get_blue(hue) * interval

      red = '%x'%(self.__toByte(red))
      green = '%x'%(self.__toByte(green))
      blue = '%x'%(self.__toByte(blue))

      if len(red) == 1:
         red = '0'+red
      if len(green) == 1:
         green = '0'+green
      if len(blue) == 1:
         blue = '0'+blue

      return gtk.gdk.color_parse("#"+red+green+blue)


   def __get_red(self, hue):
      # 
      if 0 <= hue < 60:
         return 1.0
      # 
      if 60 <= hue < 120:
         return self.__decrease(hue%60)
      # 
      if 120 <= hue < 180:
         return 0.0
      # 
      if 180 <= hue < 240:
         return 0.0
      # 
      if 240 <= hue < 300:
         return self.__increase(hue%60)
      # 
      if 300 <= hue < 360:
         return 1.0
      # This should never happen
      return 0.0


   def __get_green(self, hue):
      # 
      if 0 <= hue < 60:
         return self.__increase(hue%60)
      # 
      if 60 <= hue < 120:
         return 1.0
      # 
      if 120 <= hue < 180:
         return 1.0
      # 
      if 180 <= hue < 240:
         return self.__decrease(hue%60)
      # 
      if 240 <= hue < 300:
         return 0.0
      # 
      if 300 <= hue < 360:
         return 0.0
      # This should never happen
      return 0.0


   def __get_blue(self, hue):
      # 
      if 0 <= hue < 60:
         return 0.0
      # 
      if 60 <= hue < 120:
         return 0.0
      # 
      if 120 <= hue < 180:
         return self.__increase(hue%60)
      # 
      if 180 <= hue < 240:
         return 1.0
      # 
      if 240 <= hue < 300:
         return 1.0
      # 
      if 300 <= hue < 360:
         return self.__decrease(hue%60)
      # This should never happen
      return 0.0


   def __increase(self, hue):
      return hue/60.0

   def __decrease(self, hue):
      return 1 - hue/60.0

   def __toByte(self, dbl, min=0.0, max=1.0):
      value = (dbl - min) / (max - min)
      value = round(value * 255)
      return math.floor(value)
