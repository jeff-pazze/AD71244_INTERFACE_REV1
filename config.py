# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:33:41 2020

@author: Pazze
"""

# Arquivo config.py
# Serial port (COM port)
serial_port = 'COM4' 

# Webservice endpoint
webservice = "https://webservice.mydomain.com/publicar-dados-balanca" 

# Webservice authentication token (see weighing_scale class)
webservice_token = "4ff86e02514dd8f3610b83ee6947ccf9" 

# Name of the scale
weighing_scale_identifier = "MINHA_BALANCA_1"

# Unit of the scale
unit = 'kg' 

# Interval, in seconds, for updating data into the webservice
webservice_publication_interval = 1 