import codecs

from prontonet.device import ProntonetDevice
from prontonet.protocol import ProntonetProtocol
from prontonet.structures import *
from prontonet.enums import *


def connected(args):
    print("[+] Connected with {}".format(str(args[0])))


def disconnected(args):
    print("[!] Disconnected from {}".format(str(args[0])))


if __name__ == '__main__':
    pd = ProntonetDevice("193.47.151.26")
    pd.attach_on_connected(connected, pd.ip)
    pd.attach_on_status_socket_disconnected(disconnected, pd.ip)
    pd.attach_on_status_socket_reconnected(connected, pd.ip)
    pd.connect()
    print(pd.send_command(ProntonetProtocol.get_monitors()))
    print(pd.send_command(ProntonetProtocol.get_decoder_audio_mode(CommandDecoderGetAudioMode(codec=Codec.CODEC_1))))
    print(pd.send_command(ProntonetProtocol.get_encoder_audio_mode(CommandEncoderGetAudioMode(codec=Codec.CODEC_1))))
    print(pd.send_command(ProntonetProtocol.alarms_get_log()))
    pd.disconnect()
