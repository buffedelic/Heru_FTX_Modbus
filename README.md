# Heru FTX Modbus

### Description

Used in conjunction with a RPI to monitor Östberg Heru FTX with enabled modbus. Modbus is enabled with a custom remote bought from various Östberg supplyers.

### Requirements

minimalmodbus

### Usage

ftx_away_switch 
*used to put the ventlation system to minimum/vacation mode*
ftx_printout 
*will dump entire register to stdout*
get_ftx_temp 
*is used with rrdtool, needs editing for your needs*

### Example output:

```
HERU FTX MODBUS REGISTER
---------------
| Coil Status |
---------------
Register name                           Value               Description

Unit on                                 On                    
Overpressure mode                       Off                   
Boost mode                              Off                   
Away mode                               Off                   
Clear Alarms                            Off                 Write 1 to clear alarm, reads always 0
Reset filter timer                      Off                 Write 1 to reset filter timer, reads always 0
----------------
| Input Status |
----------------
Register name                           Value               Description

Fire alarm switch                       Off                   
Boost switch                            Off                   
Overpressure switch                     Off                   
Aux switch                              On                    
Fire alarm                              Off                   
Rotor alarm                             Off                   
RFU                                     Off                 Readable, value has no meaning
Freeze alarm                            Off                   
Low supply alarm                        Off                   
Low rotor temperature alarm             Off                   
RFU                                     Off                 Readable, value has no meaning
RFU                                     Off                 Readable, value has no meaning
Temp. sensor open circuit alarm         Off                   
Temp. sensor short circuit alarm        Off                   
Pulser alarm                            Off                   
Supply fan alarm                        Off                   
Exhaust fan alarm                       Off                   
Supply filter alarm                     Off                   
Exhaust filter alarm                    Off                   
Filter timer alarm                      Off                   
Freeze protection B level               Off                   
Freeze protection A level               Off                   
Startup 1st phase                       Off                 Supply fan stopped.
Startup 2nd phase                       Off                 No heating or cooling allowed.
Heating                                 Off                   
Recovering heat/cold                    On                    
Cooling                                 Off                   
CO2 boost                               Off                   
RH boost                                Off                   
------------------
| Input Register |
------------------
Register name                           Value               Description

Component ID                            10                    Always 10
Outdoor temperature                     6545.4°C                   
Supply air temperature                  18.5°C                   
Exhaust air temperature                 18.6°C                   
Waste air temperature                   7.3°C                   
Water temperature                       58.9°C                   
Heat Recovery Wheel temperature         17.0°C                   
Room temperature                        59.0°C                   
RFU                                     0                      
RFU                                     0                      
RFU                                     0                      
Supply pressure                         29.9 Pa                   
Exhaust pressure                        59.2 Pa                   
Relative humidity                       0 RH                   
Carbon dioxide                          0 CO2                  
RFU                                     0                      
RFU                                     0                      
Sensors open                            0                      
Sensors shorted                         0                      
Filter days left                        106 days               Number of days to filter change.
Current weektimer program               0                    0 = none, 1-5 = program 1-5
Current fan speed                       2                    0 = Off, 1 = Min, 2 = Std, 3 = Mod, 4 = Max.
Current supply fan step                 2                    0 = Off, 1 = Min, 2 = Std, 3 = Mod, 4 = Max
Current exhaust fan step                2                    0 = Off, 1 = Min, 2 = Std, 3 = Mod, 4 = Max
Current supply fan power                39%                     
Current exhaust fan power               68%                     
Current supply fan speed                1380 rpm                  
Current exhaust fan speed               2360 rpm                  
Current heating power                   0                    In range 0-255
Current heat/cold recovery power        255                    In range 0-255
Current cooling power                   0                    In range 0-255
Supply fan control voltage              38 x 0.1V               
Exhaust fan control voltage             67 x 0.1V               
----------------------------------------------------
| Holding Register, this one might take a while... |
----------------------------------------------------
Register name                           Value               Description

User fan speed                          2                    0 = Off, 1 = Min, 2 = Std, 3 = Mod, 4 = Max. Used if no weektimer is active, AC fans only.
Temperature setpoint                    22°C                   
Supply fan speed, EC                    50%                     
Exhaust fan speed, EC                   65%                     
Min exhaust fan speed, EC               20%                   Fan speed when min speed used, for example away-mode
Mod exhaust fan speed, EC               80%                   Fan speed when mod speed used, for example boost
Max exhaust fan speed, EC               90%                   Fan speed when max speed used, for example boost
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
Min supply temperature                  15°C                   
Max supply temperature                  26°C                   
Regulation mode                         0                    0 = supply, 1 = exhaust, 2 = room.
SNC indoor-outdoor diff. Limit          300.1°C                
SNC exhaust low limit                   20°C                   
SNC exhaust high limit                  22°C                   
SNC enable                              0                    0 = no, 1 = yes
Freeze protection limit temperature     7°C                   
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
CO2 limit                               90 x 10 PPM CO2       Carbon dioxide level limit.
CO2 interval                            5 min                Boosting interval, AC fans only.
CO2 ramp                                50% points / hour     Boosting ramp, EC fans only.
RH limit                                70                    Relative humidity limit, in % RH units.
RH interval                             5                    Boosting interval in minutes, AC fans only.
RH ramp                                 50% points / hour     Boosting ramp, EC fans only.
Boost speed                             4                    3 = Mod, 4 = Max.
Boost duration                          240 min                  
Overpressure duration                   15 min                  
Supply cold limit A                     2°C                   
Supply cold limit B                     9°C                 Must be greater than limit A above.
Fire sensor type                        0                    0 = none, 1 = normally open, 2 = normally closed
RFU                                     0                    Readable, value has no meaning
Supply pressure sensor type             4                    0 = switch, 1 = -50..50 Pa, 2 = 0..100 Pa, 3 = 0..150 Pa, 4 = 0..300 Pa, 5 = 0..500 Pa, 6 =
Exhaust pressure sensor type            4                    0..1000 Pa, 7 = 0..1600 Pa, 8 = 0..2500 Pa
Supply pressure switch present          0                    0 = no, 1 = yes
Exhaust pressure switch present         0                    0 = no, 1 = yes
Filter measurement, weekday             0                    0 = Monday, 1 = Tuesday … 6 = Sunday.
Filter measurement, hour                0                      
Filter measurement, minute              0                      
Filter speed increase                   10% points            0 = off, 5 to 50 = allowed power increase in %-units. Writing 5 or less equals 0.
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
Filter change period                    6 months             Filter timer in months. 0 = off, 6-12 time in months (30 days). Writing 5 or less equals 0.
Alarm relay option 1                    0                    Bit mask: bit 0 = Fire, bit 1 = Rotor, bit 2 = 0, bit 3 = Freeze, bit 4 = Low supply temperature, bit 5 = Low rotor temperature, bit 6 = 0,bit 7 = 0
Alarm relay option 2                    122                    Bit mask: bit 0 = Sensor open, bit 1 = Sensor shorted, bit 2 = Pulser, bit 3 = Supply fan, bit 4 = Exhaust fan, bit 5 = Supply filter, bit 6 = Exhaust filter, bit 7 = Filter timer
RFU                                     0                    Readable, value has no meaning
RFU                                     30                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
Water heater connected                  0                    0 = no, 1 = yes
Electric heater connected               0                    0 = no, 1 = yes
Cooler connected                        0                    0 = no, 1 = yes
Flow direction                          1                    0 = right, 1 = left
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
Clock, Weekday                          0                    0 = Monday, 1 = Tuesday ... 6 = Sunday. Reading this copies time to read/write buffer.
Clock, Hours                            9                      
Clock, Minutes                          59                      
Clock, Seconds                          49                    Writing this writes time from read/write buffer
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
Weektimer enable                        0                    0 = no, 1 = yes
WT1 on hour                             22                      
WT1 on minute                           0                      
WT1 off hour                            6                      
WT1 off minute                          0                      
WT1 weekdays                            0                    Bit mask: bit 0 = Monday, bit 6 = Sunday.
WT1 temperature setpoint                19°C                   
WT1 fan speed                           2                    1 = Min, 2 = Std, 3 = Mod, 4 = Max.
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
WT2 on hour                             8                      
WT2 on minute                           0                      
WT2 off hour                            14                      
WT2 off minute                          30                      
WT2 weekdays                            0                    Bit mask: bit 0 = Monday, bit 6 = Sunday.
WT2 temperature setpoint                17°C                   
WT2 fan speed                           1                    1 = Min, 2 = Std, 3 = Mod, 4 = Max.
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
WT3 on hour                             0                      
WT3 on minute                           0                      
WT3 off hour                            0                      
WT3 off minute                          0                      
WT3 weekdays                            0                    Bit mask: bit 0 = Monday, bit 6 = Sunday.
WT3 temperature setpoint                21°C                 1 = Min, 2 = Std, 3 = Mod, 4 = Max.
WT3 fan speed                           2                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
RFU                                     0                      
WT4 on hour                             0                      
WT4 on minute                           0                      
WT4 off hour                            0                      
WT4 off minute                          0                      
WT4 weekdays                            0                    Bit mask: bit 0 = Monday, bit 6 = Sunday.
WT4 temperature setpoint                21°C                   
WT4 fan speed                           2                    1 = Min, 2 = Std, 3 = Mod, 4 = Max.
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
RFU                                     0                    Readable, value has no meaning
WT5 on hour                             0                      
WT5 on minute                           0                      
WT5 off hour                            0                      
WT5 off minute                          0                      
WT5 weekdays                            0                    Bit mask: bit 0 = Monday, bit 6 = Sunday.
WT5 temperature setpoint                21°C                   
WT5 fan speed                           2                    1 = Min, 2 = Std, 3 = Mod, 4 = Max.
Fan type                                1                    0 = AC fans, 1 = EC fans with tacho, 2 = EC fans with alarm output
EC fan max speed                        100 x 0.1V             Voltage on fan when 100% power is applied.
Rotor pulsing period                    60 s                  Rotor pulsing period.

```
