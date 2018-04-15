"""
This program did the function of Covert RGB valus to Hexadeciaml(hex) values,and vice-versa.

Author: Jack Lee
"""

def rgb_hex():
  invalid_msg = "Some error message goes here..."
  red = int(raw_input("Enter red(R) value: "))
  if red < 0 or red > 255:
    print(invalid_msg)
    return #exit the function
  green = int(raw_input("Enter green(G) value: "))
  if green < 0 or green > 255:
    print(invalid_msg)
    return
  blue = int(raw_input("Enter blue(G) value: "))
  if blue < 0 or blue > 255:
    print(invalid_msg)
    return
#the final hexadeciaml numbers has 6 character,6 nibble,3 bytes, a byte composed of 8 bit.
  val = (red << 16) + (green << 8) + blue 
  print("%s" % hex(val)[2:].upper())
  
def hex_rgb():
    hex_val = raw_input("Enter the color(six hexadeciaml digits): ")
    if len(hex_val) != 6:
      print("Invalid hexadecimal value. Try again.")
      return
    else:
      hex_val = int(hex_val, 16)
      two_hex_digits = 2 ** 8
      blue = hex_val % two_hex_digits
      hex_val = hex_val >> 8
      green = hex_val % two_hex_digits
      hex_val = hex_val >> 8
      red = hex_val % two_hex_digits
      print("Red: %s Green: %s Blue: %s" % (red, green, blue))
     
def convert():
  while True:
    option = raw_input("Enter 1 to convert RGB to HEX.Enter 2 to convert HEX to RGB. Enter X to Exit:")
    if option == "1":
      print("RGB to HEX...")
      rgb_hex()
    elif option == "2":
      print("HEX to RGB...")
      hex_rgb()
    elif option == "X":
      print("Exit...")
      break
    else:
      print("ERROR!")
      
convert()
      










