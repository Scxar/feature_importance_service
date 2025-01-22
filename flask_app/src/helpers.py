#import os
#
#
#def get_datasets_path(path):
#    base_path = os.getenv('DATASETS_PATH')
#    return os.path.join(base_path, path)
#
#
#def get_trained_models_path(path):
#    return os.getenv('TRAINED_MODELS_PATH')
#
#
#def get_explainers_path(path):
#    return os.getenv('EXPLAINERS_PATH') + '/' + path
#

import os
def get_datasets_path(relative_path):
    base_path = os.getenv('DATASETS_PATH')
    if not base_path:
        raise EnvironmentError(
            "The environment variable 'DATASETS_PATH' is not set. Please set it to the path of your datasets directory."
        )
    full_path = os.path.join(base_path, relative_path)
    print(f"Resolved dataset path: {full_path}")
    return full_path


def get_trained_models_path(path):
    base_path = os.getenv('TRAINED_MODELS_PATH')
    if not base_path:
        raise EnvironmentError(
            "The environment variable 'TRAINED_MODELS_PATH' is not set. "
            "Please set it to the path of your trained models directory."
        )
    return base_path + '/' + path


def get_explainers_path(path):
    base_path = os.getenv('EXPLAINERS_PATH')
    if not base_path:
        raise EnvironmentError(
            "The environment variable 'EXPLAINERS_PATH' is not set. "
            "Please set it to the path of your explainers directory."
        )
    return base_path + '/' + path
print(f"EXPLAINERS_PATH: {os.getenv('EXPLAINERS_PATH')}")
print(f"TRAINED_MODELS_PATH: {os.getenv('TRAINED_MODELS_PATH')}")
print(f"DATASETS_PATH: {os.getenv('DATASETS_PATH')}")