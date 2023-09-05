#from checkandinstall import check_and_install_libraries
from basic_pitch.inference import predict_and_save
import mido
from basic_pitch import ICASSP_2022_MODEL_PATH
import pathlib

mp3_file = pathlib.Path(r"C:\Users\bacon\OneDrive\Documents\GitHub\midi\[YT2mp3.info] - UTA - Imperial Circus Dead Decadence (piano) (128kbps).mp3")
midi_file = pathlib.Path(r"C:\Users\bacon\OneDrive\Documents\GitHub\midi")
predict_and_save(
    audio_path_list=[mp3_file],
    output_directory=[midi_file],
    save_midi=True,
    save_model_outputs=True,
    sonify_midi=True,
    save_notes=True,
    minimum_note_length=0.1,
    minimum_frequency=20,
    maximum_frequency=20000,
    midi_tempo=70
    )