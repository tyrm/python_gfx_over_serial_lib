import serial


class GFX:
    def __init__(self, port):
        self._port = serial.Serial(port, 115200)

        self._brightness = 32
        self.fill_screen(0, 0, 0)

    def draw_char(self, x, y, fr, fg, fb, br, bg, bb, s, c):
        foreground = self._color888(fr, fg, fb)
        background = self._color888(br, bg, bb)

        char = ord(c)

        self._port.write("10{0:02x}{1:02x}{2:04x}{3:04x}{4:02x}{5:02x}\n".format(x, y, foreground, background, s, char))

    def draw_circle(self, x, y, rad, r, g, b):
        color = self._color888(r, g, b)
        self._port.write("0a{0:02x}{1:02x}{2:02x}{3:04x}\n".format(x, y, rad, color))

    def draw_fast_h_line(self, x, y, w, r, g, b):
        color = self._color888(r, g, b)
        self._port.write("05{0:02x}{1:02x}{2:02x}{3:04x}\n".format(x, y, w, color))

    def draw_fast_v_line(self, x, y, h, r, g, b):
        color = self._color888(r, g, b)
        self._port.write("04{0:02x}{1:02x}{2:02x}{3:04x}\n".format(x, y, h, color))

    def draw_line(self, x0, y0, y1, x1, r, g, b):
        color = self._color888(r, g, b)
        self._port.write("08{0:02x}{1:02x}{2:02x}{3:02x}{4:04x}\n".format(x0, y0, y1, x1, color))

    def draw_pixel(self, x, y, r, g, b):
        color = self._color888(r, g, b)
        self._port.write("01{0:02x}{1:02x}{2:04x}\n".format(x, y, color))

    def draw_rect(self, x, y, w, h, r, g, b):
        color = self._color888(r, g, b)
        self._port.write("09{0:02x}{1:02x}{2:02x}{3:02x}{4:04x}\n".format(x, y, w, h, color))

    def draw_triangle(self, x0, y0, y1, x1, y2, x2, r, g, b):
        color = self._color888(r, g, b)
        self._port.write("0e{0:02x}{1:02x}{2:02x}{3:02x}{4:02x}{5:02x}{6:04x}\n".format(x0, y0, y1, x1, y2, x2, color))

    def fill_circle(self, x, y, rad, r, g, b):
        color = self._color888(r, g, b)
        self._port.write("0c{0:02x}{1:02x}{2:02x}{3:04x}\n".format(x, y, rad, color))

    def fill_rect(self, x, y, w, h, r, g, b):
        color = self._color888(r, g, b)
        self._port.write("06{0:02x}{1:02x}{2:02x}{3:02x}{4:04x}\n".format(x, y, w, h, color))

    def fill_screen(self, r, g, b):
        color = self._color888(r, g, b)
        self._port.write("07{0:04x}\n".format(color))

    def fill_triangle(self, x0, y0, y1, x1, y2, x2, r, g, b):
        color = self._color888(r, g, b)
        self._port.write("0f{0:02x}{1:02x}{2:02x}{3:02x}{4:02x}{5:02x}{6:04x}\n".format(x0, y0, y1, x1, y2, x2, color))

    def set_brightness(self, b):
        if b < 1:
            self._brightness = 1
        elif b > 32:
            self._brightness = 32
        else:
            self._brightness = b

    def set_cursor(self, x, y):
        self._port.write("11{0:02x}{1:02x}\n".format(x, y))

    def set_font(self, f):
        self._port.write("19{0:02x}\n".format(f))

    def set_text_color(self, r, g, b):
        color = self._color888(r, g, b)
        self._port.write("12{0:04x}\n".format(color))

    def set_text_color_wbg(self, fr, fg, fb, br, bg, bb, s, c):
        foreground = self._color888(fr, fg, fb)
        background = self._color888(br, bg, bb)

        self._port.write("13{0:04x}{1:04x}\n".format(foreground, background))

    def text_print(self, str):
        self._port.write("17{0:02x}".format(len(str)))

        for x in range(0, len(str)):
            chr = ord(str[x])
            self._port.write("{0:02x}".format(chr))
            print(chr)

        self._port.write("\n")

    def text_println(self, str):
        self._port.write("18{0:02x}".format(len(str)))

        for x in range(0, len(str)):
            chr = ord(str[x])
            self._port.write("{0:02x}".format(chr))
            print(chr)

        self._port.write("\n")


    def _color888(self, r, g, b):
        new_r = self._map(r, 0, 255, 0, self._brightness - 1)
        new_g = self._map(g, 0, 255, 0, (self._brightness * 2) - 1)
        new_b = self._map(b, 0, 255, 0, self._brightness - 1)

        new_g = new_g << 5
        new_r = new_r << 11

        color = new_r | new_g | new_b

        return color

    def _map(self, value, fromLow, fromHigh, toLow, toHigh):
        return (((value - fromLow) * (toHigh - toLow)) / (fromHigh - fromLow)) + toLow
