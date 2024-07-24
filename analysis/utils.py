import os
from typing import Optional, Union, Any, List

import numpy as np
import pandas as pd
import plotly.express as px

import pEYES as peyes
from pEYES._DataModels.UnparsedEventLabel import UnparsedEventLabelType, UnparsedEventLabelSequenceType


CWD = os.getcwd()
OUTPUT_DIR = os.path.join(CWD, "output")
DATASETS_DIR = os.path.join(CWD, "output", "datasets")

LABELER_STR = "labeler"
DEFAULT_STR = "default"
METADATA_STR = "metadata"
MATCHES_STR = "matches"
FIELD_NAME_STR = "field_name"
GT_STR, PRED_STR = "gt", "pred"
MATCHING_SCHEME_STR = "matching_scheme"
CHANNEL_STR = "channel"
CHANNEL_TYPE_STR = f"{CHANNEL_STR}_{peyes.constants.TYPE_STR}"

DATASET_ANNOTATORS = {
    "lund2013": ["RA", "MN"],
    "irf": ['RZ'],
    "hfc": ['DN', 'IH', 'JB', 'JF', 'JV', 'KH', 'MN', 'MS', 'PZ', 'RA', 'RH', 'TC']
}
DETECTOR_NAMES = ["ivt", "ivvt", "idt", "engbert", "nh", "remodnav"]
DEFAULT_DETECTORS = [
    peyes.create_detector(det, missing_value=np.nan, min_event_duration=4, pad_blinks_time=0) for det in DETECTOR_NAMES
]

SAMPLE_METRICS = {"accuracy": ("Accuracy", 1), "balanced_accuracy": ("Balanced Accuracy", 2),
                  "cohen's_kappa": ("Cohen's Kappa", 3), "mcc": ("MCC", 4), "recall": ("Recall", 5),
                  "precision": ("Precision", 6), "f1": ("f1", 7), "1_nld": ("1 - NLD", 8), "d_prime": ("d'", 9),
                  "criterion": ("Criterion", 10),
}


DEFAULT_DISCRETE_COLORMAP = px.colors.qualitative.Dark24
DEFAULT_CONTINUOUS_COLORMAP = px.colors.sequential.Viridis

###########################################


def get_default_output_dir(dataset_name: str) -> str:
    res = os.path.join(OUTPUT_DIR, dataset_name, DEFAULT_STR)
    os.makedirs(res, exist_ok=True)
    return res


def get_filename_for_labels(
        labels: Optional[Union[UnparsedEventLabelType, UnparsedEventLabelSequenceType]] = None,
        prefix: str = "",
        suffix: str = "",
        extension: str = "pkl"
) -> str:
    if prefix and not prefix.endswith("_"):
        prefix += "_"
    if suffix and not suffix.startswith("_"):
        suffix = "_" + suffix
    if labels is None:
        return f"{prefix}all_labels{suffix}.{extension}"
    elif isinstance(labels, UnparsedEventLabelType):
        return f"{prefix}{peyes.parse_label(labels).name.lower()}{suffix}.{extension}"
    elif isinstance(labels, UnparsedEventLabelSequenceType):
        return f"{prefix}{'_'.join([peyes.parse_label(l).name.lower() for l in labels])}{suffix}.{extension}"
    else:
        raise TypeError(f"Unknown pos_labels type: {type(labels)}")


def trial_ids_by_condition(dataset: pd.DataFrame, key: str, values: Union[Any, List[Any]]) -> List[int]:
    if not isinstance(values, list):
        values = [values]
    all_trial_ids = dataset[peyes.constants.TRIAL_ID_STR]
    is_condition = dataset[key].isin(values)
    return all_trial_ids[is_condition].unique().tolist()
