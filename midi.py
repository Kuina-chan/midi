#from checkandinstall import check_and_install_libraries
from tensorflow import Tensor, signal, keras, saved_model
import numpy as np
import librosa
import pretty_midi

from basic_pitch.constants import (
    AUDIO_SAMPLE_RATE,
    AUDIO_N_SAMPLES,
    ANNOTATIONS_FPS,
    FFT_HOP,
)
from basic_pitch import ICASSP_2022_MODEL_PATH, note_creation as infer
from basic_pitch.commandline_printing import (
    generating_file_message,
    no_tf_warnings,
    file_saved_confirmation,
    failed_to_save,
)

from basic_pitch.inference import predict_and_save
import mido
from basic_pitch import ICASSP_2022_MODEL_PATH
import pathlib
from typing import Dict, List, Optional, Sequence, Tuple, Union
audio_path = pathlib.Path(r"C:\Users\bacon\OneDrive\Documents\GitHub\midi\[YT2mp3.info] - UTA - Imperial Circus Dead Decadence (piano) (128kbps).mp3")
output_directory = pathlib.Path(r"C:\Users\bacon\OneDrive\Documents\GitHub\midi\output")

predict_and_save(
    audio_path_list=[audio_path],
    output_directory=output_directory,
    save_midi=True,
    save_model_outputs=False,
    sonify_midi=True,
    save_notes=True,
    minimum_note_length=0.001,
    minimum_frequency=20,
    maximum_frequency=20000,
    midi_tempo=70,
    sonification_samplerate=44100
)