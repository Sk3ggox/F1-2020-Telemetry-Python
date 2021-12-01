import ctypes


class Header(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('m_packetFormat', ctypes.c_uint16),            # 2020
        ('m_gameMajorVersion', ctypes.c_uint8),         # Game major version - "X.00"
        ('m_gameMinorVersion', ctypes.c_uint8),         # Game minor version - "1.XX"
        ('m_packetVersion', ctypes.c_uint8),            # Version of this packet type, all start from 1
        ('m_packetId', ctypes.c_uint8),                 # Identifier for the packet type, see below
        ('m_sessionUID', ctypes.c_uint64),              # Unique identifier for the session
        ('m_sessionTime', ctypes.c_float),              # Session timestamp
        ('m_frameIdentifier', ctypes.c_uint),           # Identifier for the frame the data was retrieved on
        ('m_playerCarIndex', ctypes.c_uint8),            # Index of player's car in the array
        ('m_secondaryPlayerCarIndex', ctypes.c_uint8)   #Index of secondary player's car in the array (splitscreen)
    ]


class CarMotionData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('m_worldPositionX', ctypes.c_float),      # World space X position
        ('m_worldPositionY', ctypes.c_float),      # World space Y position
        ('m_worldPositionZ', ctypes.c_float),      # World space Z position
        ('m_worldVelocityX', ctypes.c_float),      # Velocity in world space X
        ('m_worldVelocityY', ctypes.c_float),      # Velocity in world space Y
        ('m_worldVelocityZ', ctypes.c_float),      # Velocity in world space Z
        ('m_worldForwardDirX', ctypes.c_int16),   # World space forward X direction (normalised)
        ('m_worldForwardDirY', ctypes.c_int16),   # World space forward Y direction (normalised)
        ('m_worldForwardDirZ', ctypes.c_int16),   # World space forward Z direction (normalised)
        ('m_worldRightDirX', ctypes.c_int16),     # World space right X direction (normalised)
        ('m_worldRightDirY', ctypes.c_int16),     # World space right Y direction (normalised)
        ('m_worldRightDirZ', ctypes.c_int16),     # World space right Z direction (normalised)
        ('m_gForceLateral', ctypes.c_float),       # Lateral G-Force component
        ('m_gForceLongitudinal', ctypes.c_float),  # Longitudinal G-Force component
        ('m_gForceVertical', ctypes.c_float),      # Vertical G-Force component
        ('m_yaw', ctypes.c_float),                 # Yaw angle in radians
        ('m_pitch', ctypes.c_float),               # Pitch angle in radians
        ('m_roll', ctypes.c_float)                 # Roll angle in radians
    ]


class PacketMotionData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('m_header', Header),                                # Header
        ('m_carMotionData', CarMotionData * 22),          # Data for all cars on track
        ('m_suspensionPosition', ctypes.c_float * 4),      # Note: All wheel arrays have the following order:
        ('m_suspensionVelocity', ctypes.c_float * 4),      # RL, RR, FL, FR
        ('m_suspensionAcceleration', ctypes.c_float * 4),  # RL, RR, FL, FR
        ('m_wheelSpeed', ctypes.c_float * 4),              # Speed of each wheel
        ('m_wheelSlip', ctypes.c_float * 4),               # Slip ratio for each wheel
        ('m_localVelocityX', ctypes.c_float),              # Velocity in local space
        ('m_localVelocityY', ctypes.c_float),              # Velocity in local space
        ('m_localVelocityZ', ctypes.c_float),              # Velocity in local space
        ('m_angularVelocityX', ctypes.c_float),            # Angular velocity x-component
        ('m_angularVelocityY', ctypes.c_float),            # Angular velocity y-component
        ('m_angularVelocityZ', ctypes.c_float),            # Angular velocity z-component
        ('m_angularAccelerationX', ctypes.c_float),        # Angular velocity x-component
        ('m_angularAccelerationY', ctypes.c_float),        # Angular velocity y-component
        ('m_angularAccelerationZ', ctypes.c_float),        # Angular velocity z-component
        ('m_frontWheelsAngle', ctypes.c_float)             # Current front wheels angle in radians
    ]


class MarshalZone(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('m_zoneStart', ctypes.c_float),  # Fraction (0..1) of way through the lap the marshal zone starts
        ('m_zoneFlag', ctypes.c_int8)     # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
    ]

class WeatherForecastSample(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
    ('m_sessionType', ctypes.c_uint8),      # 0 = unknown, 1 = P1, 2 = P2, 3 = P3, 4 = Short P, 5 = Q1
                                            # 6 = Q2, 7 = Q3, 8 = Short Q, 9 = OSQ, 10 = R, 11 = R2
                                            # 12 = Time Trial
    ('m_timeOffset', ctypes.c_uint8),       # Time in minutes the forecast is for
    ('m_weather', ctypes.c_uint8),          # Weather - 0 = clear, 1 = light cloud, 2 = overcast
                                            # 3 = light rain, 4 = heavy rain, 5 = storm
    ('m_trackTemperature', ctypes.c_int8),  # Track temp. in degrees celsius
    ('m_airTemperature', ctypes.c_int8)     # Air temp. in degrees celsius
    ]

class PacketSessionData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('m_header', Header),                         # Header
        ('m_weather', ctypes.c_uint8),              # Weather - 0 = clear, 1 = light cloud, 2 = overcast
                                                    # 3 = light rain, 4 = heavy rain, 5 = storm
        ('m_trackTemperature', ctypes.c_int8),      # Track temp. in degrees celsius
        ('m_airTemperature', ctypes.c_int8),        # Air temp. in degrees celsius
        ('m_totalLaps', ctypes.c_uint8),            # Total number of laps in this race
        ('m_trackLength', ctypes.c_uint16),         # Track length in metres
        ('m_sessionType', ctypes.c_uint8),          # 0 = unknown, 1 = P1, 2 = P2, 3 = P3, 4 = Short P,  5 = Q1, 6 = Q2
                                                    # 7 = Q3, 8 = Short Q, 9 = OSQ, 10 = R, 11 = R2, 12 = Time Trial
        ('m_trackId', ctypes.c_int8),               # -1 for unknown, 0-21 for tracks, see appendix
        ('m_formula', ctypes.c_uint8),              # Formula, 0 = F1 Modern, 1 = F1 Classic, 2 = F2, 3 = F1 Generic
        ('m_sessionTimeLeft', ctypes.c_uint16),     # Time left in session in seconds
        ('m_sessionDuration', ctypes.c_uint16),     # Session duration in seconds
        ('m_pitSpeedLimit', ctypes.c_uint8),        # Pit speed limit in kilometres per hour
        ('m_gamePaused', ctypes.c_uint8),           # Whether the game is paused
        ('m_isSpectating', ctypes.c_uint8),         # Whether the player is spectating
        ('m_spectatorCarIndex', ctypes.c_uint8),    # Index of the car being spectated
        ('m_sliProNativeSupport', ctypes.c_uint8),  # SLI Pro support, 0 = inactive, 1 = active
        ('m_numMarshalZones', ctypes.c_uint8),      # Number of marshal zones to follow
        ('m_marshalZones', MarshalZone * 21),       # List of marshal zones - max 21List of marshal zones - max 21
        ('m_safetyCarStatus', ctypes.c_uint8),      # 0 = no safety car, 1 = full safety car, 2 = virtual safety car
        ('m_networkGame', ctypes.c_uint8),          # 0 = offline, 1 = online
        ('m_numWeatherForecastSamples', ctypes.c_uint8), # Number of weather samples to follow
        ('m_weatherForecastSamples', WeatherForecastSample * 20)   # Array of weather forecast samples
    ]

class LapData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('m_lastLapTime', ctypes.c_float),              # Last lap time in seconds
        ('m_currentLapTime', ctypes.c_float),           # Current time around the lap in seconds
        #updated in beta 3
        ('m_sector1TimeInMS', ctypes.c_uint16),         # Sector 1 time in milliseconds
        ('m_sector2TimeInMS', ctypes.c_uint16),         # Sector 2 time in milliseconds
        ('m_bestLapTime', ctypes.c_float),              # Best lap time of the session in seconds
        ('m_bestLapNum', ctypes.c_uint8),               # Lap number best time achieved on
        ('m_bestLapSector1TimeInMS', ctypes.c_uint16),  # Sector 1 time of best lap in the session in milliseconds
        ('m_bestLapSector2TimeInMS', ctypes.c_uint16),  # Sector 2 time of best lap in the session in milliseconds
        ('m_bestLapSector3TimeInMS', ctypes.c_uint16),  # Sector 3 time of best lap in the session in milliseconds
        ('m_bestOverallSector1TimeInMS', ctypes.c_uint16),                  # Best overall sector 1 time of the session in milliseconds
        ('m_bestOverallSector1LapNum', ctypes.c_uint8),                    # Lap number best overall sector 1 time achieved on
        ('m_bestOverallSector2TimeInMS', ctypes.c_uint16),                  # Best overall sector 2 time of the session in milliseconds
        ('m_bestOverallSector2LapNum', ctypes.c_uint8),                    # Lap number best overall sector 2 time achieved on
        ('m_bestOverallSector3TimeInMS', ctypes.c_uint16),                  # Best overall sector 3 time of the session in milliseconds
        ('m_bestOverallSector3LapNum', ctypes.c_uint8),                    # Lap number best overall sector 3 time achieved on
  
        ('m_lapDistance', ctypes.c_float),        # Distance vehicle is around current lap in metres - could be negative if line hasn't been crossed yet
        ('m_totalDistance', ctypes.c_float),      # Total distance travelled in session in metres - could be negative if line hasn't been crossed yet
        ('m_safetyCarDelta', ctypes.c_float),     # Delta in seconds for safety car
        ('m_carPosition', ctypes.c_uint8),        # Car race position
        ('m_currentLapNum', ctypes.c_uint8),      # Current lap number
        ('m_pitStatus', ctypes.c_uint8),          # 0 = none, 1 = pitting, 2 = in pit area
        ('m_sector', ctypes.c_uint8),             # 0 = sector1, 1 = sector2, 2 = sector3
        ('m_currentLapInvalid', ctypes.c_uint8),  # Current lap invalid - 0 = valid, 1 = invalid
        ('m_penalties', ctypes.c_uint8),          # Accumulated time penalties in seconds to be added
        ('m_gridPosition', ctypes.c_uint8),       # Grid position the vehicle started the race in
        ('m_driverStatus', ctypes.c_uint8),       # Status of driver - 0 = in garage, 1 = flying lap, 2 = in lap 3 = out lap, 4 = on track
        ('m_resultStatus', ctypes.c_uint8)        # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished 4 = disqualified, 5 = not classified, 6 = retired
    ]


class PacketLapData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('m_header', Header),          # Header
        ('m_lapsData', LapData * 22)  # Lap data for all cars on track
    ]

class EventDataDetails(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [

    ]


class PacketEventData(ctypes.LittleEndianStructure):
    """
    This packet gives details of events that happen during the course of the race.

    Frequency: When the event occurs
    """
    _pack_ = 1
    _fields_ = [
        ('m_header', Header),                         # Header
        ('m_eventStringCode', ctypes.c_uint8 * 4),  # Event string code, see below
        ('m_eventDetails', EventDataDetails),       # Event details - should be interpreted differently for each type
    ]


class ParticipantData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('m_aiControlled', ctypes.c_uint8),  # Whether the vehicle is AI (1) or Human (0) controlled
        ('m_driverId', ctypes.c_uint8),      # Driver id - see appendix
        ('m_teamId', ctypes.c_uint8),        # Team id - see appendix
        ('m_raceNumber', ctypes.c_uint8),    # Race number of the car
        ('m_nationality', ctypes.c_uint8),   # Nationality of the driver
        ('m_name', ctypes.c_char * 48),      # Name of participant in UTF-8 format - null terminated
                                             # Will be truncated with (U+2026) if too long
        ('m_yourTelemetry', ctypes.c_uint8)  # The player's UDP setting, 0 = restricted, 1 = public
    ]


class PacketParticipantsData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('m_header', Header),                           # Header
        ('m_numActiveCars', ctypes.c_uint8),                # Number of cars in the data
        ('m_participants', ParticipantData * 22),
    ]


class CarSetupData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('m_frontWing', ctypes.c_uint8),              # Front wing aero
        ('m_rearWing', ctypes.c_uint8),               # Rear wing aero
        ('m_onThrottle', ctypes.c_uint8),             # Differential adjustment on throttle (percentage)
        ('m_offThrottle', ctypes.c_uint8),            # Differential adjustment off throttle (percentage)
        ('m_frontCamber', ctypes.c_float),            # Front camber angle (suspension geometry)
        ('m_rearCamber', ctypes.c_float),             # Rear camber angle (suspension geometry)
        ('m_frontToe', ctypes.c_float),               # Front toe angle (suspension geometry)
        ('m_rearToe', ctypes.c_float),                # Rear toe angle (suspension geometry)
        ('m_frontSuspension', ctypes.c_uint8),        # Front suspension
        ('m_rearSuspension', ctypes.c_uint8),         # Rear suspension
        ('m_frontAntiRollBar', ctypes.c_uint8),       # Front anti-roll bar
        ('m_rearAntiRollBar', ctypes.c_uint8),        # Front anti-roll bar
        ('m_frontSuspensionHeight', ctypes.c_uint8),  # Front ride height
        ('m_rearSuspensionHeight', ctypes.c_uint8),   # Rear ride height
        ('m_brakePressure', ctypes.c_uint8),          # Brake pressure (percentage)
        ('m_brakeBias', ctypes.c_uint8),              # Brake bias (percentage)
        ('m_rearLeftTyrePressure', ctypes.c_float),   # Rear left tyre pressure (PSI)
        ('m_rearRightTyrePressure', ctypes.c_float),  # Rear right tyre pressure (PSI)
        ('m_frontLeftTyrePressure', ctypes.c_float),  # Front left tyre pressure (PSI)
        ('m_frontRightTyrePressure', ctypes.c_float),  # Front right tyre pressure (PSI)
        ('m_ballast', ctypes.c_uint8),                # Ballast
        ('m_fuelLoad', ctypes.c_float),               # Fuel load
    ]


class PacketCarSetupData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('m_header', Header),  # Header
        ('m_carSetups', CarSetupData * 22)
    ]


class CarTelemetryData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('m_speed', ctypes.c_uint16),                        # Speed of car in kilometres per hour
        ('m_throttle', ctypes.c_float),                      # Amount of throttle applied (0 to 100)
        ('m_steer', ctypes.c_float),                         # Steering (-100 (full lock left) to 100 (full lock right))
        ('m_brake', ctypes.c_float),                         # Amount of brake applied (0 to 100)
        ('m_clutch', ctypes.c_uint8),                        # Amount of clutch applied (0 to 100)
        ('m_gear', ctypes.c_int8),                           # Gear selected (1-8, N=0, R=-1)
        ('m_engineRPM', ctypes.c_uint16),                    # Engine RPM
        ('m_drs', ctypes.c_uint8),                           # 0 = off, 1 = on
        ('m_revLightsPercent', ctypes.c_uint8),              # Rev lights indicator (percentage)
        ('m_brakesTemperature', ctypes.c_uint16 * 4),        # Brakes temperature (celsius)
        ('m_tyresSurfaceTemperature', ctypes.c_uint8 * 4),   # Tyres surface temperature (celsius)
        ('m_tyresInnerTemperature', ctypes.c_uint8 * 4),     # Tyres inner temperature (celsius)
        ('m_engineTemperature', ctypes.c_uint16),            # Engine temperature (celsius)
        ('m_tyresPressure', ctypes.c_float * 4),             # Tyres pressure (PSI)
        ('m_surfaceType', ctypes.c_uint8 * 4),               # Driving surface, see appendices
    ]


class PacketCarTelemetryData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('m_header', Header),                               # Header
        ('m_carTelemetryData', CarTelemetryData * 22),
        ('m_buttonStatus', ctypes.c_uint32),                # Bit flags specifying which buttons are being pressed currently - see appendices
        ('m_mfdPanelIndex', ctypes.c_uint8),                # Index of MFD panel open - 255 = MFD closed Single player, race – 0 = Car setup, 1 = Pits 2 = Damage, 3 =  Engine, 4 =     
                                                            # Temperatures May vary depending on game mode
        ('m_mfdPanelIndexSecondaryPlayer', ctypes.c_uint8), # See above
        ('m_suggestedGear', ctypes.c_int8)                  # Suggested gear for the player (1-8) 0 if no gear suggested
    ]


class CarStatusData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('m_tractionControl', ctypes.c_uint8),          # 0 (off) - 2 (high)
        ('m_antiLockBrakes', ctypes.c_uint8),           # 0 (off) - 1 (on)
        ('m_fuelMix', ctypes.c_uint8),                  # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
        ('m_frontBrakeBias', ctypes.c_uint8),           # Front brake bias (percentage)
        ('m_pitLimiterStatus', ctypes.c_uint8),         # Pit limiter status - 0 = off, 1 = on
        ('m_fuelInTank', ctypes.c_float),               # Current fuel mass
        ('m_fuelCapacity', ctypes.c_float),             # Fuel capacity
        ('m_fuelRemainingLaps', ctypes.c_float),        # Fuel remaining in terms of laps (value on MFD)
        ('m_maxRPM', ctypes.c_uint16),                    # Cars max RPM, point of rev limiter
        ('m_idleRPM', ctypes.c_uint16),                   # Cars idle RPM
        ('m_maxGears', ctypes.c_uint8),                 # Maximum number of gears
        ('m_drsAllowed', ctypes.c_uint8),               # 0 = not allowed, 1 = allowed, -1 = unknown
        ('m_drsActivationDistance', ctypes.c_uint16),   # 0 = DRS not available, non-zero - DRS will be available in [X] metres
        ('m_tyresWear', ctypes.c_uint8 * 4),            # Tyre wear percentage
        ('m_actualTyreCompound', ctypes.c_uint8),       # F1 Modern - 16 = C5, 17 = C4, 18 = C3, 19 = C2, 20 = C1
   					                                    # 7 = inter, 8 = wet
   					                                    # F1 Classic - 9 = dry, 10 = wet
   					                                    # F2 - 11 = super soft, 12 = soft, 13 = medium, 14 = hard
   					                                    # 15 = wet
        ('m_tyreVisualCompound', ctypes.c_uint8),       # F1 visual (can be different from actual compound
                                                        # 16 = soft, 17 = medium, 18 = hard, 7 = inter, 8 = wet
                                                        # F1 Classic - same as above
                                                        # F2 - same as above
        ('m_tyresAgeLaps', ctypes.c_uint8),             # Age in laps of the current set of tyres
        ('m_tyresDamage', ctypes.c_uint8 * 4),          # Tyre damage (percentage)
        ('m_frontLeftWingDamage', ctypes.c_uint8),      # Front left wing damage (percentage)
        ('m_frontRightWingDamage', ctypes.c_uint8),     # Front right wing damage (percentage)
        ('m_rearWingDamage', ctypes.c_uint8),           # Rear wing damage (percentage)
        ('m_drsFault', ctypes.c_uint8),                 # Indicator for DRS fault, 0 = OK, 1 = fault
        ('m_engineDamage', ctypes.c_uint8),             # Engine damage (percentage)
        ('m_gearBoxDamage', ctypes.c_uint8),            # Gear box damage (percentage)
        ('m_vehicleFiaFlags', ctypes.c_int8),           # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue
                                                        #  3 = yellow, 4 = red
        ('m_ersStoreEnergy', ctypes.c_float),           # ERS energy store in Joules
        ('m_ersDeployMode', ctypes.c_uint8),            # ERS deployment mode, 0 = none, 1 = low, 2 = medium, 3 = high
                                                        #  4 = overtake, 5 = hotlap
        ('m_ersHarvestedThisLapMGUK', ctypes.c_float),  # ERS energy harvested this lap by MGU-K
        ('m_ersHarvestedThisLapMGUH', ctypes.c_float),  # ERS energy harvested this lap by MGU-H
        ('m_ersDeployedThisLap', ctypes.c_float),       # ERS energy deployed this lap
    ]


class PacketCarStatusData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('m_header', Header),                              # Header
        ('m_carStatusData', CarStatusData * 22)
    ]
    
class FinalClassificationData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
    ('m_position', ctypes.c_uint8),
    ('m_numLaps', ctypes.c_uint8),
    ('m_gridPosition', ctypes.c_uint8),
    ('m_points', ctypes.c_uint8),
    ('m_numPitStops', ctypes.c_uint8),
    ('m_resultStatus', ctypes.c_uint8),
    
    ('m_bestLapTime', ctypes.c_float),
    ('m_totalRaceTime', ctypes.c_double),
    ('m_penaltiesTime', ctypes.c_uint8),
    ('m_numPenalties', ctypes.c_uint8),
    ('m_numTyreStints', ctypes.c_uint8),
    ('m_tyreStintsActual', ctypes.c_uint8 * 8),
    ('m_tyreStintsVisual', ctypes.c_uint8 * 8)
    ]
    
class PacketFinalClassificationData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('m_header', Header),                       # Header
        ('m_numCars', ctypes.c_uint8),
        ('m_carStatusData', CarStatusData * 22)
    ]
    
class LobbyInfoData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
    ('m_aiControlled', ctypes.c_uint8),
    ('m_teamId', ctypes.c_uint8),
    ('m_nationality', ctypes.c_uint8),
    ('m_name', ctypes.c_char * 48),
    ('m_readyStatus', ctypes.c_uint8)
    ]
    
class PacketLobbyInfoData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('m_header', Header),                       # Header
        ('m_numPlayers', ctypes.c_uint8),
        ('m_lobbyPlayers', LobbyInfoData * 22)
    ]