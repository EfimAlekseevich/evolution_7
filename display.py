from constantes import control_parameters


def show_records(screen, cycle_count, settings, font, organisms):
    display_records = dict()
    display_records['cycle'] = cycle_count
    display_records['num org-s'] = len(organisms)
    parameters = settings.get_dict_parameters()

    display_records = {**display_records, **parameters}

    indent = settings.environment.width + 10
    num_string = 0
    for parameter, value in display_records.items():
        text = f'{parameter} = {str(round(value, 2))}'
        if parameter in control_parameters.keys():
            text = f'{control_parameters[parameter]}) {text}'
        record = font.render(text, True, settings.text_color)
        screen.blit(record, (indent, num_string * 24))
        num_string += 1
