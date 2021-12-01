import socket
from f1_telemetry.f1_2019_struct import *

UDP_IP = "192.168.92.132"
UDP_PORT = 20777


def get_telemetry():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, _ = sock.recvfrom(1506)
        m_header = Header.from_buffer_copy(data[0:24])
        mad = 0
        player = 0
        if int(m_header.m_packetId) == 0:
            packet = PacketMotionData.from_buffer_copy(data[0:1464])
            theader = int(m_header.m_packetId)

        elif int(m_header.m_packetId) == 1:
            packet = PacketSessionData.from_buffer_copy(data[0:251])
            theader = int(m_header.m_packetId)

        elif int(m_header.m_packetId) == 2:
            packet = PacketLapData.from_buffer_copy(data[0:1190])
            theader = int(m_header.m_packetId)
            player = int(m_header.m_playerCarIndex)
            #mad = PacketLapData.from_buffer_copy(data[0:843])

        elif int(m_header.m_packetId) == 3:
            packet = PacketEventData.from_buffer_copy(data[0:35])
            theader = int(m_header.m_packetId)

        elif int(m_header.m_packetId) == 4:
            packet = PacketParticipantsData.from_buffer_copy(data[0:1213])
            theader = int(m_header.m_packetId)
            mad = PacketParticipantsData.from_buffer_copy(data[0:1213])

        elif int(m_header.m_packetId) == 5:
            packet = PacketCarSetupData.from_buffer_copy(data[0:1102])
            theader = int(m_header.m_packetId)

        elif int(m_header.m_packetId) == 6:
            packet = PacketCarTelemetryData.from_buffer_copy(data[0:1307])
            theader = int(m_header.m_packetId)

        elif int(m_header.m_packetId) == 7:
            packet = PacketCarStatusData.from_buffer_copy(data[0:1344])
            theader = int(m_header.m_packetId)
         
        elif int(m_header.m_packetId) == 8:
            packet = PacketFinalClassificationData.from_buffer_copy(data[0:839])
            theader = int(m_header.m_packetId)
            
        elif int(m_header.m_packetId) == 9:
            packet = PacketLobbyInfoData.from_buffer_copy(data[0:1169])
            theader = int(m_header.m_packetId)

        yield packet, theader, mad, player
