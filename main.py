from gfx import GFX

if __name__ == '__main__':
    panel = GFX("COM21")

    panel.set_brightness(8)

    panel.draw_pixel(0, 0, 255, 127, 0)
    panel.draw_pixel(17, 17, 255, 127, 0)

    panel.draw_fast_v_line(1, 1, 16, 0, 255, 255)
    panel.draw_fast_h_line(1, 1, 16, 0, 255, 255)
    panel.draw_fast_v_line(16, 1, 16, 0, 255, 255)
    panel.draw_fast_h_line(1, 16, 16, 0, 255, 255)

    panel.fill_rect(0, 18, 5, 5, 127, 127, 127)
    panel.draw_rect(5, 18, 5, 5, 22, 44, 66)

    panel.draw_line(3, 0, 9, 17, 255, 0, 0)

    panel.draw_circle(24, 8, 4, 0, 255, 0)
    panel.fill_circle(26, 10, 4, 127, 0, 255)

    panel.fill_triangle(18, 18, 26, 18, 22, 24, 0, 127, 127)
    panel.draw_triangle(21, 20, 29, 20, 25, 26, 255, 127, 127)

    panel.set_font(0x00)
    panel.draw_char(8, 3, 0, 255, 0, 0, 0, 127, 1, "B")

    panel.set_text_color(0, 127, 255)
    panel.set_cursor(0, 27)

    panel.set_font(0x33)
    panel.text_println("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    panel.set_text_color(127, 0, 255)
    panel.set_cursor(0, 52)
    panel.text_println("abcdefghijklmnopqrstuvwxyz")

