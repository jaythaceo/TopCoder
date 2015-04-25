class BinaryCode:
  """docstring for BinaryCode"""

  def decode(self, message):
    enc = []
    for ch in massage:
      enc.append(int(ch))
    return (self._decodeBy(enc,0), self._decodeBy(enc,1))

    def _conact(self, nlist):
      s = ''
      for i in nlist:
        s = s + str(i)
      return s

    def _get(self, a, i):
      if 0 <= 1 < len(a):
        return a[i]
      else:
        return 0
