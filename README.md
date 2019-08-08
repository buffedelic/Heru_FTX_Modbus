# Heru_FTX_Modbus

Example output:

---------------
| Coil Status |
---------------
Unit on                                 On                    
Overpressure mode                       Off     
..
...
----------------
| Input Status |
----------------
Fire alarm switch                       Off                   
Boost switch                            Off                   
Overpressure switch                     Off     
..
...
------------------
| Input Register |
------------------
Component ID                            10                    Always 10
Outdoor temperature                     7.1°C                   
Supply air temperature                  18.5°C                   
Exhaust air temperature                 19.4°C        
..
...
----------------------------------------------------
| Holding Register, this one might take a while... |
----------------------------------------------------
User fan speed                          2                    0 = Off, 1 = Min, 2 = Std, 3 = Mod, 4 = Max.
Used if no weektimer is active, AC fans only.
Temperature setpoint                    25°C                   
Supply fan speed, EC                    48%                     
Exhaust fan speed, EC                   70%     
..
...