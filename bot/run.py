from booking.booking import Booking


try:
    with Booking() as bot:
        # Configuramos la url donde se ejecutara el bot
        bot.land_first_page()
        # Configuramos el tipo de moneda a usar
        # bot.change_currency(currency='EUR')
        # Configuramos el lugar(ciudad o país) de viaje
        bot.select_place_to_go(place_to_go='New Jersey')
        # - Configuramos las fechas de nuestra estadia, en este 
        #   formato: //año-mes-día//
        # - La fecha del check_in_date solo se puede configurar 
        #   desde la fecha actual(o sea la fecha de hoy de su ordenador)
        #   hacia a adelante
        bot.select_dates(check_in_date='2022-01-11', 
                        check_out_date='2022-01-26')
        # El parametro indicara el numero de adultos
        bot.select_adults(1)
        # Hace click en el boton de busqueda
        bot.click_search()
        # Aplicara la filtracion de resultados
        bot.apply_filtration()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
