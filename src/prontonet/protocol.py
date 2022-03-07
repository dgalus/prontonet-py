import struct
from prontonet.structures import *
from prontonet.enums import *


class ProdysProtocol:
    @staticmethod
    def connect():
        command_code = Command.CONNECT
        cs = CSConnect.securityString
        b = struct.pack("<ii", command_code, 20)
        return b + cs.zfill(20)

    @staticmethod
    def get_device_net():
        return struct.pack("<ii", Command.COMMAND_GET_DEVICE_NET, 0)

    @staticmethod
    def set_device_net():  # TODO
        command_code = 101
        pass

    @staticmethod
    def call():  # TODO
        command_code = 102
        pass

    @staticmethod
    def answer(arg: CommandAnswer):
        return struct.pack("<iii", Command.COMMAND_ANSWER, 4, arg.line)

    @staticmethod
    def hang_up(arg: CommandHangUp):
        return struct.pack("<iii", Command.COMMAND_HANG_UP, 4, arg.line)

    @staticmethod
    def get_line_status(arg: CommandGetLineStatus):
        return struct.pack("<iii", Command.COMMAND_GET_LINE_STATUS, 4, arg.line)

    @staticmethod
    def get_line_status_details(arg: CommandGetLineStatusDetails):
        return struct.pack("<iii", Command.COMMAND_GET_LINE_STATUS_DETAILS, 4, arg.line)

    @staticmethod
    def get_vu_meters():
        return struct.pack("<ii", Command.COMMAND_GET_VU_METERS, 0)

    @staticmethod
    def get_monitors():
        return struct.pack("<ii", Command.COMMAND_GET_MONITORS, 0)

    @staticmethod
    def get_alarm_status():
        return struct.pack("<ii", Command.COMMAND_DECODER_GET_AUDIO_MODE, 0)

    @staticmethod
    def get_decoder_audio_mode(arg: CommandDecoderGetAudioMode):
        return struct.pack("<iii", Command.COMMAND_DECODER_GET_AUDIO_MODE, 4, arg.codec)

    @staticmethod
    def get_encoder_audio_mode(arg: CommandEncoderGetAudioMode):
        return struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE, 4, arg.codec)

    @staticmethod
    def set_encoder_audio_mode_pcm(arg: CommandEncoderSetAudioModePCM):
        return struct.pack("<ii4i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_PCM, 16,
                           arg.codec, arg.bits_sample, arg.audio_mode, arg.encoder_mix)

    @staticmethod
    def set_encoder_audio_mode_mpeg(arg: CommandEncoderSetAudioModeMPEG):
        return struct.pack("<ii9i", Command.COMMAND_ENCODER_GET_AUDIO_MODE_MPEG, 36,
                           arg.codec, arg.bit_rate, arg.audio_mode, arg.mpeg_layer, arg.frequency,  arg.crc,
                           arg.aux_data, arg.encoder_mix, arg.bonding_type)

    @staticmethod
    def set_encoder_audio_mode_aac(arg: CommandEncoderSetAudioModeAAC):
        return struct.pack("<ii9i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_AAC, 36,
                           arg.codec, arg.bit_rate, arg.audio_mode, arg.aac_mode, arg.frequency, arg.crc,
                           arg.aux_data, arg.encoder_mix, arg.bonding_type)

    @staticmethod
    def set_encoder_audio_mode_g711(arg: CommandEncoderSetAudioModeG711):
        return struct.pack("<ii2i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_G711, 8,
                           arg.codec, arg.encoder_mix)

    @staticmethod
    def set_encoder_audio_mode_g722(arg: CommandEncoderSetAudioModeG722):
        return struct.pack("<ii2i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_G711, 8,
                           arg.codec, arg.encoder_mix)

    @staticmethod
    def set_encoder_audio_mode_auto(arg: CommandEncoderSetAudioModeAuto):
        return struct.pack("<ii2i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_AUTO, 8,
                           arg.codec, arg.aux_data)

    @staticmethod
    def set_encoder_audio_mode_aptx(arg: CommandEncoderSetAudioModeAPTX):
        return struct.pack("<ii7i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_APTX, 28,
                           arg.codec, arg.audio_mode, arg.aptx_type, arg.frequency,
                           arg.crc, arg.aux_data, arg.encoder_mix)

    @staticmethod
    def set_encoder_audio_mode_g711_v2(arg: CommandEncoderSetAudioModeG711v2):
        return struct.pack("<ii3i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_G711_V2, 12,
                           arg.codec, arg.encoder_mix, arg.g711_law)

    @staticmethod
    def set_encoder_audio_mode_g722_v2(arg: CommandEncoderSetAudioModeG722v2):
        return struct.pack("<ii3i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_G722_V2, 12,
                           arg.codec, arg.encoder_mix, arg.g722_dither)

    @staticmethod
    def set_encoder_audio_mode_mpeg_v2(arg: CommandEncoderSetAudioModeMPEGv2):
        return struct.pack("<ii10i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_MPEG_V2, 40,
                           arg.codec, arg.bit_rate, arg.audio_mode, arg.mpeg_layer, arg.frequency,
                           arg.crc, arg.aux_data, arg.encoder_mix, arg.bonding_type, arg.mpeg_l3_polarity)

    @staticmethod
    def get_ip_streaming_protocol():
        return struct.pack("<ii", Command.COMMAND_IP_GET_STREAMING_PROTOCOL, 0)

    @staticmethod
    def set_ip_streaming_protocol(arg: CommandIPSetStreamingProtocol):
        return struct.pack("<iii", Command.COMMAND_IP_SET_STREAMING_PROTOCOL, 4, arg.streaming_protocol)

    @staticmethod
    def x21_enable_tx(arg: CommandX21EnableTX):
        return struct.pack("<iii", Command.COMMAND_IP_SET_STREAMING_PROTOCOL, 4, arg.enable)

    @staticmethod
    def load_preset():  # TODO
        command_code = 125
        pass

    @staticmethod
    def call_from_book(arg: CommandCallFromBook):
        return struct.pack("<ii2i", Command.COMMAND_CALL_FROM_BOOK, 8, arg.line, arg.book_entry)

    @staticmethod
    def alarms_ack():
        return struct.pack("<ii", Command.COMMAND_ALARMS_ACK, 0)

    @staticmethod
    def alarms_delete():
        return struct.pack("<ii", Command.COMMAND_ALARMS_DELETE, 0)

    @staticmethod
    def call_from_book_all_lines(arg: CommandCallFromBookAllLines):
        return struct.pack("<iii", Command.COMMAND_CALL_FROM_BOOK_ALL_LINES, 4, arg.book_entry)

    @staticmethod
    def get_device_net_v2():  # TODO
        command_code = 130
        pass

    @staticmethod
    def set_device_net_v2(arg: CommandDeviceNetV2):
        return struct.pack("<ii5i", Command.COMMAND_SET_DEVICE_NET_V2, 20, arg.device_net, arg.device_sub_net,
                           arg.pronto_net_codec_mode, arg.multi_unicast, arg.streaming_protocol)

    @staticmethod
    def call_v2(arg: CommandCallV2): # TODO
        command_code = 132
        pass

    @staticmethod
    def get_loaded_preset_index(arg: CommandGetLoadedPresetIndex):
        return struct.pack("<iii", Command.COMMAND_GET_LOADED_PRESET_INDEX, 4, arg.index)

    @staticmethod
    def run_gpi_action(arg: CommandRunGPIAction):
        return struct.pack("<ii2i", Command.COMMAND_RUN_GPI_ACTION, 8, arg.gpi, arg.active)

    @staticmethod
    def enable_net_backup():   # TODO
        command_code = 135
        pass

    @staticmethod
    def reset_device():
        return struct.pack("<ii", Command.COMMAND_RESET_DEVICE, 0)

    @staticmethod
    def get_loaded_preset_name():  # TODO
        command_code = 137
        pass

    @staticmethod
    def get_streaming_stats(arg: CommandGetStreamingStats):
        return struct.pack("<iii", Command.COMMAND_GET_STREAMING_STATS, 20, arg.target_codec)

    @staticmethod
    def get_sip_server_register_status(arg: CommandGetSIPServerRegisterStatus):
        return struct.pack("<iii", Command.COMMAND_GET_SIP_SERVER_REGISTER_STATUS, 4, arg.registered)

    @staticmethod
    def get_stun_server_register_status(arg: CommandGetSTUNServerRegisterStatus):
        return struct.pack("<iii", Command.COMMAND_GET_STUN_SERVER_REGISTER_STATUS, 4, arg.registered)

    @staticmethod
    def get_call_duration(arg: CommandGetCallDuration):
        return struct.pack("<iii", Command.COMMAND_GET_CALL_DURATION, 4, arg.line)

    @staticmethod
    def alarms_get_log():  # TODO
        command_code = 142
        pass

    @staticmethod
    def get_audio_configuration():
        return struct.pack("<ii", Command.COMMAND_AUDIO_GET_CONFIGURATION, 0)

    @staticmethod
    def set_audio_configuration(arg: CommandAudioSetConfiguration):
        return struct.pack("<ii5i", Command.COMMAND_AUDIO_SET_CONFIGURATION, 20,
                           arg.audio_config, arg.db_in_left, arg.db_in_right, arg.db_out_left, arg.db_out_right)

    @staticmethod
    def get_device_name():
        return struct.pack("<ii", Command.COMMAND_SYS_GET_DEVICE_NAME, 0)

    @staticmethod
    def set_device_name():  # TODO
        command_code = 146
        pass

    @staticmethod
    def blink_device():
        return struct.pack("<ii", Command.COMMAND_SYS_BLINK_DEVICE, 0)

    @staticmethod
    def get_version_info():
        return struct.pack("<ii", Command.COMMAND_SYS_GET_VERSION_INFO, 0)

    @staticmethod
    def get_sip_configuration():
        return struct.pack("<ii", Command.COMMAND_SIP_GET_CONFIGURATION, 0)

    @staticmethod
    def set_sip_configuration():   # TODO
        command_code = 150
        pass

    @staticmethod
    def get_configuration_v4():
        return struct.pack("<ii", Command.COMMAND_PRODYS_V4_GET_CONFIGURATION, 0)

    @staticmethod
    def set_configuration_v4(arg: CommandProdysV4Configuration):
        return struct.pack("<ii6i", Command.COMMAND_PRODYS_V4_SET_CONFIGURATION, 24, arg.line_1_port,
                           arg.enable_control_port, arg.auto_answer, arg.enable_fec, arg.audio_packets_per_fec_packet,
                           arg.fec_delay)

    @staticmethod
    def get_streaming_tx_codec_configuration(arg: CommandStreamingTXCodecGetConfiguration):
        return struct.pack("<ii2i", Command.COMMAND_STREAMING_TX_GET_CODEC_CONFIGURATION,
                           arg.codec, arg.audio_algorithm)

    @staticmethod
    def set_streaming_tx_codec_configuration(arg: CommandStreamingTXCodecSetConfiguration):
        return struct.pack("<ii3i", Command.COMMAND_STREAMING_TX_SET_CODEC_CONFIGURATION,
                           arg.codec, arg.audio_algorithm, arg.time_between_packets)

    @staticmethod
    def get_streaming_rx_codec_configuration():
        command_code = 155
        pass

    @staticmethod
    def set_streaming_rx_codec_configuration():
        command_code = 156
        pass

    @staticmethod
    def get_streaming_stats_v2():
        command_code = 157
        pass

    @staticmethod
    def get_ethernet_speed():
        command_code = 158
        pass

    @staticmethod
    def streaming_stats_reset():
        command_code = 159
        pass

    @staticmethod
    def set_encoder_audio_mode_pcm_v2():
        command_code = 160
        pass

    @staticmethod
    def set_encoder_audio_mode_g711_v3():
        command_code = 161
        pass

    @staticmethod
    def set_encoder_audio_mode_g722_v3():
        command_code = 162
        pass

    @staticmethod
    def set_encoder_audio_mode_aptx_v2():
        command_code = 163
        pass

    @staticmethod
    def get_encoder_audio_mode_algorithm():
        command_code = 164
        pass

    @staticmethod
    def get_decoder_audio_mode_algorithm():
        command_code = 165
        pass

    @staticmethod
    def get_encoder_audio_mode_auto():
        command_code = 166
        pass

    @staticmethod
    def get_encoder_audio_mode_pcm():
        command_code = 167
        pass

    @staticmethod
    def get_encoder_audio_mode_g711():
        command_code = 168
        pass

    @staticmethod
    def get_encoder_audio_mode_g722():
        command_code = 169
        pass

    @staticmethod
    def get_encoder_audio_mode_mpeg():
        command_code = 170
        pass

    @staticmethod
    def get_encoder_audio_mode_acc():
        command_code = 171
        pass

    @staticmethod
    def get_encoder_audio_mode_aptx():
        command_code = 172
        pass

    @staticmethod
    def get_decoder_audio_mode_pcm():
        command_code = 173
        pass

    @staticmethod
    def get_decoder_audio_mode_g711():
        command_code = 174
        pass

    @staticmethod
    def get_decoder_audio_mode_g722():
        command_code = 175
        pass

    @staticmethod
    def get_decoder_audio_mode_mpeg():
        command_code = 176
        pass

    @staticmethod
    def get_decoder_audio_mode_aac():
        command_code = 177
        pass

    @staticmethod
    def get_decoder_audio_mode_aptx():
        command_code = 178
        pass

    @staticmethod
    def set_encoder_audio_mode_opus():
        command_code = 179
        pass

    @staticmethod
    def get_encoder_audio_mode_opus():
        command_code = 180
        pass

    @staticmethod
    def get_decoder_audio_mode_opus():
        command_code = 181
        pass
