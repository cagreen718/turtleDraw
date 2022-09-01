import math
def areaTriangle(base,height):
  #Copy code from part 1
  area=0.5*base*height
  return round(area,2)
  
def areaRectangle(length,width):
  #Copy code from part 1
  area=length*width
  return round(area,2)
  
def areaCircle(rad):
  #Copy code from part 1
  area= math.pi*rad**2
  return round(area,2)
def main():
  triaBase= float(input("Enter the base of the triangle:" ))
  triaHieg= float(input("Enter the height of the triangle:" ))
  rectLeng= float(input("Enter the length of the rectangle:" ))
  rectWid= float(input("Enter the width of the rectangle:" ))
  cirRad= float(input("Enter the radius of the circle:" ))
  totalArea=0
  totalArea= round(totalArea + areaTriangle(triaBase, triaHieg) + areaRectangle(rectLeng, rectWid) + areaCircle(cirRad),2)
  print ("Total area is:", totalArea)
main()