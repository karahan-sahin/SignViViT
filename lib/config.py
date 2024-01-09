# MODEL PARAMS
AXIS = 2
DISTANCE = 'euc' # EUC, COS, OR MAHAL

# IMAGE ENCODER PARAMS
IMAGE_SIZE = 65
NUM_CHANNELS = 2
MODEL_TYPE = 'vivit'
NUM_HIDDEN_LAYERS = 5
NUM_ATTENTION_HEADS = 8
NUM_FRAMES = 100
PATCH_SIZE = 4
TUBELET_SIZE = 8 
MAX_TOKENS = 256

# MODEL TYPE
POSE_ENCODER_TYPE = 'videomae' # VIVIT, VIDEOMAE
VIDEO_ENCODER_MODEL_VIVIT = 'google/vivit-b-16x2'
VIDEO_ENCODER_MODEL_VIDEOMAE = 'MCG-NJU/videomae-base'
TEXT_DECODER_MODEL = 'gpt2'
POSE_ENCODER_MODEL = 'posemae_base'
TRANSLATION_MODEL = 'vivit-gpt-model'


# TRAINING PARAMS
TASK_TYPE = 'classification' # TRANSLATION, CLASSIFICATION
DATASET_TYPE = 'bsign22k' # BSIGN22K, AUTSL, ASL FINGER SPELLING
NUM_CLASSES = 768 # 768 for bsign, , 22 for classification
NUM_EPOCHS = 100
BATCH_SIZE = 32
LEARNING_RATE = 1e-4
EPSILON = 1e-8
DEVICE = 'cpu'


# BSIGN22K DATASET PARAMS
DATASET_FILE_PATH ='data/bsign22k/BosphorusSign22k.csv' 
POSE_DATA_PATH = 'data/autsl/mmpose-full'

# AUTSL DATASET PARAMS


# ASL FINGER SPELLING DATASET PARAMS


# LOGGING PARAMS
LOG_DIR = f'signmae_base-{POSE_ENCODER_TYPE}-{TASK_TYPE}-{NUM_EPOCHS}-{BATCH_SIZE}-{TUBELET_SIZE}-{NUM_FRAMES}-{PATCH_SIZE}-logs.txt'