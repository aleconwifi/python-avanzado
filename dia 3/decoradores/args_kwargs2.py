class Coche:
  def __init__(self, color, marca):
    self.color = color
    self.marca = marca


class Tesla(Coche):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs):
    self.marca = 'Tesla'
    