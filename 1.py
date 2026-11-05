import arcade, math
arcade.open_window(600,600,"Game")
arcade.set_background_color(arcade.color.Color(0,150,0))
arcade.start_render()
arcade.draw_circle_outline(300,300,50,arcade.color.Color(100,0,50))
arcade.finish_render()
arcade.run()