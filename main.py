from gfx import GFX

if __name__ == '__main__':
    panel = GFX("COM21")

    panel.draw_pixel(0, 0, 255, 127, 0)
    panel.draw_pixel(17, 17, 255, 127, 0)

    panel.draw_fast_v_line(1, 1, 16, 0, 255, 255)
    panel.draw_fast_h_line(1, 1, 16, 0, 255, 255)
    panel.draw_fast_v_line(16, 1, 16, 0, 255, 255)
    panel.draw_fast_h_line(1, 16, 16, 0, 255, 255)

    panel.fill_rect(0, 18, 5, 5, 127, 127, 127)
    panel.draw_rect(5, 18, 5, 5, 22, 44, 66)

    panel.draw_line(3, 0, 9, 17, 255, 0, 0)
