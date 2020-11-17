class Planety():
   def newWiek(self, wiek, planeta):
      earth = 31557600
      dict = {
          "Ziemia": 1,
          "Merkury": 0.2408467,
          "Wenus": 0.61519726,
          "Mars": 1.8808158,
          "Jowisz": 11.862615,
          "Saturn": 29.447498,
          "Uran": 84.016846,
          "Neptun": 164.79132
      }

      if type(wiek) == int and type(planeta) == str:
         if wiek > 0 and (planeta in dict):
            x = wiek / (dict[planeta] * earth)
            return (round(x, 2))
         else:
            raise Exception("Error in program")
      else:
         raise Exception("Error in program")
