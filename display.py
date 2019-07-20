def show_records(screen, cycle_count, settings, font, organisms):
    records = {
        'num_org-s': len(organisms),
        'cycles': cycle_count,
        'brightness_sun': settings.environment.sun,
        'max FPS': settings.fps,
        '+-) mutations': settings.strong_mutation,
        '1) max_health': settings.max_health,
        '2) parent_heath': settings.parent_health,
        '3) heir_heath': settings.heir_health,
        '4) -common': settings.environment.losses.common,
        '5) -move': settings.environment.losses.move,
        '6) -sleep': settings.environment.losses.sleep,
        '7)-sun': settings.environment.losses.sun_sun,
        '8) +plant': settings.environment.eat_plant,
        '9) +sun': settings.environment.eat_sun,
    }
    indent = settings.environment.width + 10

    num_string = 0

    for parameter, value in records.items():
        text = f'{parameter} = {str(round(value, 2))}'
        record = font.render(text, True, settings.text_color)
        screen.blit(record, (indent, num_string * 26))
        num_string += 1
