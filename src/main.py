import codecs

from prontonet.device import ProntonetDevice
from prontonet.protocol import ProntonetProtocol
from prontonet.structures import *
from prontonet.enums import *


def connected(args):
    print("[+] Connected with {}".format(str(args[0])))


def disconnected(args):
    print("[!] Disconnected from {}".format(str(args[0])))


def alarm_status_changed(alarm_status: StatusAlarmsStatusChanged, *args):
    print("Alarm status: " + str(alarm_status))


def line_status_changed(status: StatusLineStatusChanged, *args):
    print("Line status: " + str(status))


def encoder_audio_mode_changed(status: StatusEncoderAudioModeChanged, *args):
    print("Encoder audio mode: " + str(status))


if __name__ == '__main__':
    pd = ProntonetDevice("193.47.151.26")
    pd.attach_on_connected(connected, pd.ip)
    pd.attach_on_status_socket_disconnected(disconnected, pd.ip)
    pd.attach_on_status_socket_reconnected(connected, pd.ip)
    pd.attach_on_alarm_status_changed(alarm_status_changed)
    pd.attach_on_line_status_changed(line_status_changed)
    pd.attach_on_encoder_audio_mode_changed(encoder_audio_mode_changed)
    pd.connect()

    pd.disconnect()
