import os

import numpy as np
import pandas as pd
from tqdm import tqdm
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

import pEYES as peyes
import analysis.utils as u
from analysis.pipeline.full_pipeline import run

pio.renderers.default = "browser"

################
## ALL LABELS ##

results = run(output_dir=os.path.join(u.OUTPUT_DIR, "default_values"), dataset_name="lund2013", verbose=False)
# (dataset, labels, metadata, events, matches, sample_mets, time_diffs, channel_sdt_metrics, matched_features, matches_sdt_metrics) = results
# del results

# TODO: calculate channel-metrics based on labels and not events
## TODO: statistical tests for: sample metrics, label-channel metrics, matched-events metrics

################
## FIX LABELS ##

results = run(output_dir=os.path.join(u.OUTPUT_DIR, "default_values"), dataset_name="lund2013", verbose=False, pos_labels=1)
# (dataset, labels, metadata, events, matches, sample_mets, time_diffs, channel_sdt_metrics, matched_features, matches_sdt_metrics) = results
# del results

################
## SAC LABELS ##

results = run(output_dir=os.path.join(u.OUTPUT_DIR, "default_values"), dataset_name="lund2013", verbose=False, pos_labels=2)
# (dataset, labels, metadata, events, matches, sample_mets, time_diffs, channel_sdt_metrics, matched_features, matches_sdt_metrics) = results
# del results
