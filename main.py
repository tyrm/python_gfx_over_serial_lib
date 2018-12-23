from gfx import GFX

if __name__ == '__main__':
    panel = GFX("COM21")

    panel.draw_pixel(1, 1, 255, 127, 0)
