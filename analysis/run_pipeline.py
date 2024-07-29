import os

import plotly.io as pio

import analysis.utils as u
from analysis.process.full_pipeline import run

pio.renderers.default = "browser"

###################

results = run(output_dir=os.path.join(u.OUTPUT_DIR, "default_values"), dataset_name="lund2013", verbose=False)
fix_results = run(
    output_dir=os.path.join(u.OUTPUT_DIR, "default_values"), dataset_name="lund2013", verbose=False, pos_labels=1
)
sac_results = run(
    output_dir=os.path.join(u.OUTPUT_DIR, "default_values"), dataset_name="lund2013", verbose=False, pos_labels=2
)
fix_sac_results = run(
    output_dir=os.path.join(u.OUTPUT_DIR, "default_values"), dataset_name="lund2013", verbose=False, pos_labels=[1, 2]
)
