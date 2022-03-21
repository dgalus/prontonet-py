from enum import IntEnum


class Command(IntEnum):
    ALIVE = 0
    CONNECT = 1
    COMMAND_RESPONSE = 3

    STATUS_DEVICE_NET_CHANGED = 10
    STATUS_LINE_STATUS_CHANGED = 11
    STATUS_ALARMS_STATUS_CHANGED = 12
    STATUS_DECODER_AUDIO_MODE_CHANGED = 13
    STATUS_ENCODER_AUDIO_MODE_CHANGED = 14

    COMMAND_GET_DEVICE_NET = 100
    COMMAND_SET_DEVICE_NET = 101
    COMMAND_CALL = 102
    COMMAND_HANG_UP = 103
    COMMAND_GET_LINE_STATUS = 104
    COMMAND_GET_VU_METERS = 105
    COMMAND_GET_MONITORS = 106
    COMMAND_ALARMS_GET_STATUS = 107
    COMMAND_DECODER_GET_AUDIO_MODE = 108
    COMMAND_ENCODER_GET_AUDIO_MODE = 109
    COMMAND_ENCODER_SET_AUDIO_MODE_PCM = 110
    COMMAND_ENCODER_SET_AUDIO_MODE_MPEG = 111
    COMMAND_ENCODER_SET_AUDIO_MODE_AAC = 112
    COMMAND_ENCODER_SET_AUDIO_MODE_G711 = 113
    COMMAND_ENCODER_SET_AUDIO_MODE_G722 = 114
    COMMAND_ENCODER_SET_AUDIO_MODE_AUTO = 115
    COMMAND_ENCODER_SET_AUDIO_MODE_APTX = 116
    COMMAND_GET_LINE_STATUS_DETAILS = 117
    COMMAND_ANSWER = 118
    COMMAND_ENCODER_SET_AUDIO_MODE_G711_V2 = 119
    COMMAND_ENCODER_SET_AUDIO_MODE_G722_V2 = 120
    COMMAND_ENCODER_SET_AUDIO_MODE_MPEG_V2 = 121
    COMMAND_IP_GET_STREAMING_PROTOCOL = 122
    COMMAND_IP_SET_STREAMING_PROTOCOL = 123
    COMMAND_X21_ENABLE_TX = 124
    COMMAND_LOAD_PRESET = 125
    COMMAND_CALL_FROM_BOOK = 126
    COMMAND_ALARMS_ACK = 127
    COMMAND_ALARMS_DELETE = 128
    COMMAND_CALL_FROM_BOOK_ALL_LINES = 129
    COMMAND_GET_DEVICE_NET_V2 = 130
    COMMAND_SET_DEVICE_NET_V2 = 131
    COMMAND_CALL_V2 = 132
    COMMAND_GET_LOADED_PRESET_INDEX = 133
    COMMAND_RUN_GPI_ACTION = 134
    COMMAND_ENABLE_NET_BACKUP = 135
    COMMAND_RESET_DEVICE = 136
    COMMAND_GET_LOADED_PRESET_NAME = 137
    COMMAND_GET_STREAMING_STATS = 138
    COMMAND_GET_SIP_SERVER_REGISTER_STATUS = 139
    COMMAND_GET_STUN_SERVER_REGISTER_STATUS = 140
    COMMAND_GET_CALL_DURATION = 141
    COMMAND_ALARMS_GET_LOG = 142
    COMMAND_AUDIO_GET_CONFIGURATION = 143
    COMMAND_AUDIO_SET_CONFIGURATION = 144
    COMMAND_SYS_GET_DEVICE_NAME = 145
    COMMAND_SYS_SET_DEVICE_NAME = 146
    COMMAND_SYS_BLINK_DEVICE = 147
    COMMAND_SYS_GET_VERSION_INFO = 148
    COMMAND_SIP_GET_CONFIGURATION = 149
    COMMAND_SIP_SET_CONFIGURATION = 150
    COMMAND_PRODYS_V4_GET_CONFIGURATION = 151
    COMMAND_PRODYS_V4_SET_CONFIGURATION = 152
    COMMAND_STREAMING_TX_GET_CODEC_CONFIGURATION = 153
    COMMAND_STREAMING_TX_SET_CODEC_CONFIGURATION = 154
    COMMAND_STREAMING_RX_GET_CODEC_CONFIGURATION = 155
    COMMAND_STREAMING_RX_SET_CODEC_CONFIGURATION = 156
    COMMAND_GET_STREAMING_STATS_V2 = 157
    COMMAND_ETHERNET_GET_SPEED = 158
    COMMAND_STREAMING_STATS_RESET = 159
    COMMAND_ENCODER_SET_AUDIO_MODE_PCM_V2 = 160
    COMMAND_ENCODER_SET_AUDIO_MODE_G711_V3 = 161
    COMMAND_ENCODER_SET_AUDIO_MODE_G722_V3 = 162
    COMMAND_ENCODER_SET_AUDIO_MODE_APTX_V2 = 163
    COMMAND_ENCODER_GET_AUDIO_MODE_ALGORITHM = 164
    COMMAND_DECODER_GET_AUDIO_MODE_ALGORITHM = 165
    COMMAND_ENCODER_GET_AUDIO_MODE_AUTO = 166
    COMMAND_ENCODER_GET_AUDIO_MODE_PCM = 167
    COMMAND_ENCODER_GET_AUDIO_MODE_G711 = 168
    COMMAND_ENCODER_GET_AUDIO_MODE_G722 = 169
    COMMAND_ENCODER_GET_AUDIO_MODE_MPEG = 170
    COMMAND_ENCODER_GET_AUDIO_MODE_AAC = 171
    COMMAND_ENCODER_GET_AUDIO_MODE_APTX = 172
    COMMAND_DECODER_GET_AUDIO_MODE_PCM = 173
    COMMAND_DECODER_GET_AUDIO_MODE_G711 = 174
    COMMAND_DECODER_GET_AUDIO_MODE_G722 = 175
    COMMAND_DECODER_GET_AUDIO_MODE_MPEG = 176
    COMMAND_DECODER_GET_AUDIO_MODE_AAC = 177
    COMMAND_DECODER_GET_AUDIO_MODE_APTX = 178
    COMMAND_ENCODER_SET_AUDIO_MODE_OPUS = 179
    COMMAND_ENCODER_GET_AUDIO_MODE_OPUS = 180
    COMMAND_DECODER_GET_AUDIO_MODE_OPUS = 181


class AudioMode(IntEnum):
    MONO = 1
    STEREO = 2
    JOINT = 3
    DUAL = 4


class BitsSample(IntEnum):
    BITS_SAMPLE_16 = 16
    BITS_SAMPLE_20 = 20
    BITS_SAMPLE_24 = 24


class EncoderMix(IntEnum):
    NONE = 0
    LR = 1
    LR_3_DB = 2
    LR_6_DB = 3


class IPCallType(IntEnum):
    UNICAST_BIDIRECTIONAL = 0
    UNICAST_UNIDIRECTIONAL_TX = 1
    MULTICAST_TX = 2
    MULTICAST_RX = 3
    UNICAST_UNIDIRECTIONAL_RX = 4


class LineStatus(IntEnum):
    NO_PHYSICAL_LINE = 0
    DISCONNECTED = 1
    DISCONNECTING = 2
    CALLING = 3
    RECEIVING_CALL = 4
    CONNECTED_CALLED = 5
    CONNECTED_RECEIVED = 6
    CALL_REJECTED = 7
    NOT_AVAILABLE = 8


class BitRate(IntEnum):
    BITRATE_FREE = 0
    BITRATE_8_KBPS = 1000
    BITRATE_16_KBPS = 2000
    BITRATE_24_KBPS = 3000
    BITRATE_32_KBPS = 4000
    BITRATE_40_KBPS = 5000
    BITRATE_48_KBPS = 6000
    BITRATE_56_KBPS = 7000
    BITRATE_64_KBPS = 8000
    BITRATE_72_KBPS = 9000
    BITRATE_80_KBPS = 10000
    BITRATE_88_KBPS = 11000
    BITRATE_96_KBPS = 12000
    BITRATE_104_KBPS = 13000
    BITRATE_112_KBPS = 14000
    BITRATE_120_KBPS = 15000
    BITRATE_128_KBPS = 16000
    BITRATE_144_KBPS = 18000
    BITRATE_160_KBPS = 20000
    BITRATE_168_KBPS = 21000
    BITRATE_192_KBPS = 24000
    BITRATE_224_KBPS = 28000
    BITRATE_240_KBPS = 30000
    BITRATE_256_KBPS = 32000
    BITRATE_280_KBPS = 35000
    BITRATE_288_KBPS = 36000
    BITRATE_320_KBPS = 40000
    BITRATE_336_KBPS = 42000
    BITRATE_384_KBPS = 48000
    BITRATE_480_KBPS = 60000
    BITRATE_576_KBPS = 72000


class MPEGLayer(IntEnum):
    L_NOT = 0
    L1 = 1
    L2 = 2
    L3 = 3


class Frequency(IntEnum):
    FREQ_8000 = 8000
    FREQ_11025 = 11025
    FREQ_12000 = 12000
    FREQ_16000 = 16000
    FREQ_22050 = 22050
    FREQ_24000 = 24000
    FREQ_32000 = 32000
    FREQ_44100 = 44100
    FREQ_48000 = 48000


class AACMode(IntEnum):
    MPEG2_LC = 5
    MPEG4_LC = 6
    MPEG4_ER_LD = 7
    MPEG4_HE = 8
    MPEG_ELD = 10


class APTXType(IntEnum):
    STANDARD = 0
    ENHANCED_16_BITS = 1
    ENHANCED_20_BITS = 2
    ENHANCED_24_BITS = 3


class BondingType(IntEnum):
    NONE = 0
    CCSTELOS = 1
    J52 = 2


class DeviceNet(IntEnum):
    IP = 0
    ISDN = 1
    X21 = 2
    NONE = 3
    PSTN = 4


class G711Law(IntEnum):
    A = 0
    MU = 1


class MPEGL3Polarity(IntEnum):
    NORMATIVE = 0
    INVERSE = 1


class StreamingProtocol(IntEnum):
    PRODYS = 0
    SIP = 1
    SAP = 2
    PRODYS_V2 = 3
    CCS = 4
    RTP = 5
    PRODYS_V3 = 6
    PRODYS_V4 = 7


class DeviceSubNet(IntEnum):
    DEVICE_SUBNET_NONE = 0
    DEVICE_SUBNET_ETHERNET = 1
    DEVICE_SUBNET_3G = 2


class ProntoNetCodecMode(IntEnum):
    SIMPLE = 0
    DOUBLE = 1


class Codec(IntEnum):
    CODEC_1 = 0
    CODEC_2 = 1
    CODEC_MAX = 2
    CODEC_NONE = 3


class AlarmStatus(IntEnum):
    NONE = 0
    ALARM_ACTIVE = 1
    ALARM_HISTORY = 2


class AudioConfig(IntEnum):
    ANALOG = 0
    ANALOG_EXTERNAL_SYNC = 1
    AESEBU_AUDIO_SYNC = 2
    AESEBU_EXTERNAL_SYNC = 3
    AESEBU_INTERNAL_SYNC = 4
    AESEBU_TRANSPARENT = 5
    AESEBU_UBIT_MASTER = 6
    AESEBU_UBIT_SLAVE = 7


class SIPAddressType(IntEnum):
    LOCAL = 0
    PUBLIC = 1
    STUN = 2


class AudioAlgorithm(IntEnum):
    PCM = 0
    G711 = 1
    G722 = 2
    MPEG_LAYER_2 = 3
    MPEG_LAYER_3 = 4
    MPEG2_AAC_LC = 5
    MPEG4_AAC_LC = 6
    MPEG4_AAC_LD = 7
    MPEG4_AAC_HE = 8
    MPEG4_AAC_ELD = 9
    APTX = 10
    APTX_ENH_16_BITS = 11
    APTX_ENH_20_BITS = 12
    APTX_ENH_24_BITS = 13


class EthernetInterface(IntEnum):
    LAN_1 = 0
    LAN_2 = 1


class EthernetNegotiatedSpeed(IntEnum):
    LINK_DOWN = 0
    SPEED_10_MB_HALF_DUPLEX = 1
    SPEED_10_MB_FULL_DUPLEX = 2
    SPEED_100_MB_HALF_DUPLEX = 3
    SPEED_100_MB_FULL_DUPLEX = 4


class AudioModeAlgorithm(IntEnum):
    PCM = 0
    MPEG = 1
    AAC = 2
    G711 = 3
    G722 = 4
    AUTO = 5
    APTX = 6


class Acknowledge(IntEnum):
    ERROR = 0
    SUCCESS = 1