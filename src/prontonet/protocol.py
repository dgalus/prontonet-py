import struct
from prontonet.structures import *
from prontonet.enums import *


class ProntonetProtocol:
    @staticmethod
    def connect():
        command_code = Command.CONNECT
        cs = CSConnect.securityString
        b = struct.pack("<ii", command_code, 20)
        return b + cs.zfill(20)

    @staticmethod
    def get_device_net() -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_GET_DEVICE_NET, 0),
            "iii",
            DeviceNet
        )

    @staticmethod
    def set_device_net():  # TODO
        command_code = 101
        pass

    @staticmethod
    def call():  # TODO
        command_code = 102
        pass

    @staticmethod
    def answer(arg: CommandAnswer) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ANSWER, 4, arg.line),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def hang_up(arg: CommandHangUp) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_HANG_UP, 4, arg.line),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_line_status(arg: CommandGetLineStatus) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_GET_LINE_STATUS, 4, arg.line),
            "iii",
            CommandGetLineStatusResponse
        )

    @staticmethod
    def get_line_status_details(arg: CommandGetLineStatusDetails):  # TODO
        return struct.pack("<iii", Command.COMMAND_GET_LINE_STATUS_DETAILS, 4, arg.line)

    @staticmethod
    def get_vu_meters() -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_GET_VU_METERS, 0),
            "iiiiii",
            CommandGetVUMetersResponse
        )

    @staticmethod
    def get_monitors() -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_GET_MONITORS, 0),
            "iiiiii",
            CommandGetMonitorsResponse
        )

    @staticmethod
    def get_alarm_status() -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_ALARMS_GET_STATUS, 0),
            "iii",
            AlarmStatus
        )

    @staticmethod
    def get_decoder_audio_mode(arg: CommandDecoderGetAudioMode) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_DECODER_GET_AUDIO_MODE, 4, arg.codec),
            "ii#",
            bytes
        )

    @staticmethod
    def get_encoder_audio_mode(arg: CommandEncoderGetAudioMode) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE, 4, arg.codec),
            "ii#",
            bytes
        )

    @staticmethod
    def set_encoder_audio_mode_pcm(arg: CommandEncoderSetAudioModePCM) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii4i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_PCM, 16,
                        arg.codec, arg.bits_sample, arg.audio_mode, arg.encoder_mix),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_mpeg(arg: CommandEncoderSetAudioModeMPEG) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii9i", Command.COMMAND_ENCODER_GET_AUDIO_MODE_MPEG, 36,
                        arg.codec, arg.bit_rate, arg.audio_mode, arg.mpeg_layer, arg.frequency, arg.crc,
                        arg.aux_data, arg.encoder_mix, arg.bonding_type),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_aac(arg: CommandEncoderSetAudioModeAAC) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii9i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_AAC, 36,
                        arg.codec, arg.bit_rate, arg.audio_mode, arg.aac_mode, arg.frequency, arg.crc,
                        arg.aux_data, arg.encoder_mix, arg.bonding_type),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_g711(arg: CommandEncoderSetAudioModeG711) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii2i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_G711, 8,
                        arg.codec, arg.encoder_mix),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_g722(arg: CommandEncoderSetAudioModeG722) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii2i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_G711, 8,
                        arg.codec, arg.encoder_mix),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_auto(arg: CommandEncoderSetAudioModeAuto) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii2i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_AUTO, 8,
                        arg.codec, arg.aux_data),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_aptx(arg: CommandEncoderSetAudioModeAPTX) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii7i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_APTX, 28,
                        arg.codec, arg.audio_mode, arg.aptx_type, arg.frequency,
                        arg.crc, arg.aux_data, arg.encoder_mix),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_g711_v2(arg: CommandEncoderSetAudioModeG711v2) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii3i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_G711_V2, 12,
                        arg.codec, arg.encoder_mix, arg.g711_law),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_g722_v2(arg: CommandEncoderSetAudioModeG722v2) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii3i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_G722_V2, 12,
                        arg.codec, arg.encoder_mix, arg.g722_dither),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_mpeg_v2(arg: CommandEncoderSetAudioModeMPEGv2) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii10i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_MPEG_V2, 40,
                        arg.codec, arg.bit_rate, arg.audio_mode, arg.mpeg_layer, arg.frequency,
                        arg.crc, arg.aux_data, arg.encoder_mix, arg.bonding_type, arg.mpeg_l3_polarity),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_ip_streaming_protocol() -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_IP_GET_STREAMING_PROTOCOL, 0),
            "iii",
            StreamingProtocol
        )

    @staticmethod
    def set_ip_streaming_protocol(arg: CommandIPSetStreamingProtocol) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_IP_SET_STREAMING_PROTOCOL, 4, arg.streaming_protocol),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def x21_enable_tx(arg: CommandX21EnableTX) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_IP_SET_STREAMING_PROTOCOL, 4, arg.enable),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def load_preset():  # TODO
        command_code = 125
        pass

    @staticmethod
    def call_from_book(arg: CommandCallFromBook) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii2i", Command.COMMAND_CALL_FROM_BOOK, 8, arg.line, arg.book_entry),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def alarms_ack() -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_ALARMS_ACK, 0),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def alarms_delete() -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_ALARMS_DELETE, 0),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def call_from_book_all_lines(arg: CommandCallFromBookAllLines) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_CALL_FROM_BOOK_ALL_LINES, 4, arg.book_entry),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_device_net_v2():  # TODO
        command_code = 130
        pass

    @staticmethod
    def set_device_net_v2(arg: CommandDeviceNetV2):
        return struct.pack("<ii5i", Command.COMMAND_SET_DEVICE_NET_V2, 20, arg.device_net, arg.device_sub_net,
                           arg.pronto_net_codec_mode, arg.multi_unicast, arg.streaming_protocol)

    @staticmethod
    def call_v2(arg: CommandCallV2):  # TODO
        command_code = 132
        pass

    @staticmethod
    def get_loaded_preset_index(arg: CommandGetLoadedPresetIndex) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_GET_LOADED_PRESET_INDEX, 4, arg.index),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def run_gpi_action(arg: CommandRunGPIAction) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii2i", Command.COMMAND_RUN_GPI_ACTION, 8, arg.gpi, arg.active),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def enable_net_backup():  # TODO
        command_code = 135
        pass

    @staticmethod
    def reset_device() -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_RESET_DEVICE, 0),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_loaded_preset_name():  # TODO
        command_code = 137
        pass

    @staticmethod
    def get_streaming_stats(arg: CommandGetStreamingStats) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_GET_STREAMING_STATS, 20, arg.target_codec),
            "ii4i",
            CommandGetStreamingStatsResponse
        )

    @staticmethod
    def get_sip_server_register_status(arg: CommandGetSIPServerRegisterStatus) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_GET_SIP_SERVER_REGISTER_STATUS, 4, arg.registered),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_stun_server_register_status(arg: CommandGetSTUNServerRegisterStatus) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_GET_STUN_SERVER_REGISTER_STATUS, 4, arg.registered),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_call_duration(arg: CommandGetCallDuration) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_GET_CALL_DURATION, 4, arg.line),
            "iii",
            CommandGetCallDurationResponse
        )

    @staticmethod
    def alarms_get_log() -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_ALARMS_GET_LOG, 0),
            "ii#",
            bytes
        )

    @staticmethod
    def get_audio_configuration() -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_AUDIO_GET_CONFIGURATION, 0),
            "ii6i",
            CommandAudioGetConfigurationResponse
        )

    @staticmethod
    def set_audio_configuration(arg: CommandAudioSetConfiguration) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii5i", Command.COMMAND_AUDIO_SET_CONFIGURATION, 20,
                        arg.audio_config, arg.db_in_left, arg.db_in_right, arg.db_out_left, arg.db_out_right),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_device_name() -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_SYS_GET_DEVICE_NAME, 0),
            "ii#",
            bytes
        )

    @staticmethod
    def set_device_name():  # TODO
        command_code = 146
        pass

    @staticmethod
    def blink_device() -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_SYS_BLINK_DEVICE, 0),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_version_info():  # TODO
        return struct.pack("<ii", Command.COMMAND_SYS_GET_VERSION_INFO, 0)

    @staticmethod
    def get_sip_configuration():  # TODO
        return struct.pack("<ii", Command.COMMAND_SIP_GET_CONFIGURATION, 0)

    @staticmethod
    def set_sip_configuration():  # TODO
        command_code = 150
        pass

    @staticmethod
    def get_configuration_v4() -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii", Command.COMMAND_PRODYS_V4_GET_CONFIGURATION, 0),
            "ii6i",
            CommandProdysV4ConfigurationResponse
        )

    @staticmethod
    def set_configuration_v4(arg: CommandProdysV4Configuration) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii6i", Command.COMMAND_PRODYS_V4_SET_CONFIGURATION, 24, arg.line_1_port,
                        arg.enable_control_port, arg.auto_answer, arg.enable_fec, arg.audio_packets_per_fec_packet,
                        arg.fec_delay),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_streaming_tx_codec_configuration(arg: CommandStreamingTXCodecGetConfiguration) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii2i", Command.COMMAND_STREAMING_TX_GET_CODEC_CONFIGURATION,
                        arg.codec, arg.audio_algorithm),
            "iiii",
            CommandStreamingTXCodecGetConfigurationResponse
        )

    @staticmethod
    def set_streaming_tx_codec_configuration(arg: CommandStreamingTXCodecSetConfiguration) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii3i", Command.COMMAND_STREAMING_TX_SET_CODEC_CONFIGURATION,
                        arg.codec, arg.audio_algorithm, arg.time_between_packets),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_streaming_rx_codec_configuration(arg: CommandStreamingRXCodecGetConfiguration) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_STREAMING_RX_GET_CODEC_CONFIGURATION, 4, arg.codec),
            "ii7i",
            CommandStreamingRXCodecGetConfigurationResponse
        )

    @staticmethod
    def set_streaming_rx_codec_configuration(arg: CommandStreamingRXCodecSetConfiguration) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii7i", Command.COMMAND_STREAMING_RX_SET_CODEC_CONFIGURATION, 28,
                        arg.codec, arg.auto_adjustment, arg.auto_min_delay, arg.auto_min_delay_duration,
                        arg.auto_max_delay, arg.auto_max_delay_duration, arg.manual_max_delay),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_streaming_stats_v2(arg: CommandGetStreamingStatsV2) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_GET_STREAMING_STATS_V2, 4, arg.codec),
            "ii10i",
            CommandGetStreamingStatsV2Response
        )

    @staticmethod
    def get_ethernet_speed(arg: CommandEthernetGetSpeed) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ETHERNET_GET_SPEED, 4, arg.ethernet_interface),
            "ii3i",
            CommandEthernetGetSpeedResponse
        )

    @staticmethod
    def streaming_stats_reset(arg: CommandStreamingStatsReset) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_STREAMING_STATS_RESET, 4, arg.codec),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_pcm_v2(arg: CommandAudioModeConfigPCMV2) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii5i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_PCM_V2, 20,
                        arg.codec, arg.bits_sample, arg.audio_mode, arg.encoder_mix, arg.aux_data),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_g711_v3(arg: CommandAudioModeConfigG711V3) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii4i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_G711_V3, 16,
                        arg.codec, arg.g711_law, arg.encoder_mix, arg.aux_data),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_g722_v3(arg: CommandAudioModeConfigG722V3) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii4i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_G722_V3, 16,
                        arg.codec, arg.encoder_mix, arg.aux_data, arg.g722_dither),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def set_encoder_audio_mode_aptx_v2(arg: CommandAudioModeConfigAPTXV2) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii6i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_APTX_V2, 24,
                        arg.codec, arg.aptx_type, arg.bit_rate, arg.audio_mode, arg.encoder_mix, arg.aux_data),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_encoder_audio_mode_algorithm(arg: CommandGetAudioModeAlgorithm) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE_ALGORITHM, 4, arg.codec),
            "ii2i",
            CommandEncoderGetAudioModeAlgorithmResponse
        )

    @staticmethod
    def get_decoder_audio_mode_algorithm(arg: CommandGetAudioModeAlgorithm) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_DECODER_GET_AUDIO_MODE_ALGORITHM, 4, arg.codec),
            "ii3i",
            CommandDecoderGetAudioModeAlgorithmResponse
        )

    @staticmethod
    def get_encoder_audio_mode_auto(arg: CommandEncoderGetAudioMode) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE_AUTO, 4, arg.codec),
            "ii2i",
            CommandEncoderGetAudioModeAutoResponse
        )

    @staticmethod
    def get_encoder_audio_mode_pcm(arg: CommandEncoderGetAudioMode) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE_PCM, 4, arg.codec),
            "ii5i",
            CommandEncoderGetAudioModePCMResponse
        )

    @staticmethod
    def get_encoder_audio_mode_g711(arg: CommandEncoderGetAudioMode) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE_G711, 4, arg.codec),
            "ii4i",
            CommandEncoderGetAudioModeG711Response
        )

    @staticmethod
    def get_encoder_audio_mode_g722(arg: CommandEncoderGetAudioMode) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE_G722, 4, arg.codec),
            "ii4i",
            CommandEncoderGetAudioModeG722Response
        )

    @staticmethod
    def get_encoder_audio_mode_mpeg(arg: CommandEncoderGetAudioMode) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE_MPEG, 4, arg.codec),
            "ii10i",
            CommandEncoderGetAudioModeMPEGResponse
        )

    @staticmethod
    def get_encoder_audio_mode_acc(arg: CommandEncoderGetAudioMode) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE_AAC, 4, arg.codec),
            "ii9i",
            CommandEncoderGetAudioModeAACResponse
        )

    @staticmethod
    def get_encoder_audio_mode_aptx(arg: CommandEncoderGetAudioMode) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE_APTX, 4, arg.codec),
            "ii6i",
            CommandEncoderGetAudioModeAPTXResponse
        )

    @staticmethod
    def get_decoder_audio_mode_pcm(arg: CommandDecoderGetAudioMode) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_DECODER_GET_AUDIO_MODE_PCM, 4, arg.codec),
            "ii5i",
            CommandDecoderGetAudioModePCMResponse
        )

    @staticmethod
    def get_decoder_audio_mode_g711(arg: CommandDecoderGetAudioMode) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_DECODER_GET_AUDIO_MODE_G711, 4, arg.codec),
            "ii4i",
            CommandDecoderGetAudioModeG711Response
        )

    @staticmethod
    def get_decoder_audio_mode_g722(arg: CommandDecoderGetAudioMode) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_DECODER_GET_AUDIO_MODE_G722, 4, arg.codec),
            "ii4i",
            CommandDecoderGetAudioModeG722Response
        )

    @staticmethod
    def get_decoder_audio_mode_mpeg(arg: CommandDecoderGetAudioMode) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_DECODER_GET_AUDIO_MODE_MPEG, 4, arg.codec),
            "ii10i",
            CommandDecoderGetAudioModeMPEGResponse
        )

    @staticmethod
    def get_decoder_audio_mode_aac(arg: CommandDecoderGetAudioMode) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_DECODER_GET_AUDIO_MODE_AAC, 4, arg.codec),
            "ii9i",
            CommandDecoderGetAudioModeAACResponse
        )

    @staticmethod
    def get_decoder_audio_mode_aptx(arg: CommandDecoderGetAudioMode) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_DECODER_GET_AUDIO_MODE_APTX, 4, arg.codec),
            "ii6i",
            CommandDecoderGetAudioModeAPTXResponse
        )

    @staticmethod
    def set_encoder_audio_mode_opus(arg: CommandAudioModeOPUS) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<ii4i", Command.COMMAND_ENCODER_SET_AUDIO_MODE_OPUS, 16,
                        arg.codec, arg.bit_rate, arg.encoder_mix, arg.aux_data),
            "iiii",
            AcknowledgeResponse
        )

    @staticmethod
    def get_encoder_audio_mode_opus(arg: CommandEncoderGetAudioMode) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_ENCODER_GET_AUDIO_MODE_OPUS, 4, arg.codec),
            "ii4i",
            CommandAudioModeOPUS
        )

    @staticmethod
    def get_decoder_audio_mode_opus(arg: CommandDecoderGetAudioMode) -> ProntonetCommand:
        return ProntonetCommand(
            struct.pack("<iii", Command.COMMAND_DECODER_GET_AUDIO_MODE_OPUS, 4, arg.codec),
            "ii4i",
            CommandAudioModeOPUS
        )
