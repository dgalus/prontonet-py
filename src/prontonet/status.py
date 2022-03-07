class ProdysStatus:
    def device_net_changed(self):
        command_code = 10

    def line_status_changed(self):
        command_code = 11

    def alarms_status(self):
        command_code = 12

    def decoder_audio_mode_changed(self):
        command_code = 13

    def encoder_audio_mode_changed(self):
        command_code = 14
