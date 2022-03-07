from prontonet.prodys_device import ProntonetDevice
from prontonet.protocol import ProdysProtocol
from prontonet.structures import *
from prontonet.enums import *

if __name__ == '__main__':
    pd = ProntonetDevice("193.47.151.26")
    pd.connect()

    pd.disconnect()

    c = CommandEncoderSetAudioModePCM(
        Codec.CODEC_1,
        BitsSample.BITS_SAMPLE_16,
        AudioMode.STEREO,
        EncoderMix.LR
    )
    print(ProdysProtocol.set_encoder_audio_mode_pcm(c))


