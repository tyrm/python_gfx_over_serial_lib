import serial


class GFX:
    def __init__(self, port):
        self._port = serial.Serial(port, 115200)

        self._brightness = 32
        self._port.write(b'070000\n')

    def color888(self, r, g, b):
        new_r = self._map(r, 0, 255, 0, self._brightness - 1)
        new_g = self._map(g, 0, 255, 0, (self._brightness * 2) - 1)
        new_b = self._map(b, 0, 255, 0, self._brightness - 1)

        new_g = new_g << 5
        new_r = new_r << 11

        color = new_r | new_g | new_b

        return color

    def draw_pixel(self, x, y, r, g, b):
        color = self.color888(r, g, b)
        self._port.write("01{0:02x}{1:02x}{2:04x}\n".format(x, y, color))

    def set_brightness(self, b):
        if b < 1:
            self._brightness = 1
        elif b > 32:
            self._brightness = 32
        else:
            self._brightness = b

    def _map(self, value, fromLow, fromHigh, toLow, toHigh):
        return (((value - fromLow) * (toHigh - toLow)) / (fromHigh - fromLow)) + toLow
