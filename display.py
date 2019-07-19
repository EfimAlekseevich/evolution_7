def show_records(screen, cycle_count, settings, font, organisms):

    num_organisms = font.render('number org-s = ' + str(len(organisms)), True, settings.text_color)
    cycles = font.render('cycles = ' + str(cycle_count), True, settings.text_color)
    light = font.render('brightness_sun = ' + str(settings.environment.sun), True, settings.text_color)
    fps = font.render('max FPS = ' + str(settings.fps), True, settings.text_color)
    common = font.render('1)-common = ' + str(settings.environment.losses.common), True, settings.text_color)
    move = font.render('2)-move = ' + str(settings.environment.losses.move), True, settings.text_color)
    sleep = font.render('3)-sleep = ' + str(settings.environment.losses.sleep), True, settings.text_color)
    sun_sun = font.render('4)-sun = ' + str(settings.environment.losses.sun_sun), True, settings.text_color)
    plant = font.render('5)+plant = ' + str(settings.environment.losses.eat_plant), True, settings.text_color)
    sun = font.render('6)+sun = ' + str(settings.environment.losses.eat_sun), True, settings.text_color)

    indent = settings.environment.width + 15
    screen.blit(num_organisms, (indent, 0))
    screen.blit(cycles, [indent, 26])
    screen.blit(light, [indent, 52])
    screen.blit(fps, [indent, 78])
    screen.blit(common, [indent, 102])
    screen.blit(move, [indent, 126])
    screen.blit(sleep, [indent, 154])
    screen.blit(sun_sun, [indent, 180])
    screen.blit(plant, [indent, 206])
    screen.blit(sun, [indent, 232])
