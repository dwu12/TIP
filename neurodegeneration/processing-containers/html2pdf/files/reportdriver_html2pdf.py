import sys, os
import glob
import html2pdf
import pickle
from datetime import datetime

# For local testng
# os.environ["WORKFLOW_DIR"] = "/sharedFolder/5datasets_F8F12F18M13M5/F8"
# os.environ["BATCH_NAME"] = "batch"
# os.environ["OPERATOR_OUT_DIR"] = "/sharedFolder/5datasets_F8F12F18M13M5/F8/output-html-wo-wmls"
# os.environ["OPERATOR_IN_DIR_QUANT"] = "roi-quantification"
# os.environ["OPERATOR_IN_DIR_BIOMARKER"] = "normative-bio-visual-ouput2"
# os.environ["OPERATOR_IN_DIR_BRAINVIS"] = "brain-visualize"

# From the template
batch_folders = sorted([f for f in glob.glob(os.path.join('/', os.environ['WORKFLOW_DIR'], os.environ['BATCH_NAME'], '*'))])

for batch_element_dir in batch_folders:
    in_path_biomarker=os.path.join(batch_element_dir, os.environ['OPERATOR_IN_DIR_BIOMARKER'])
    in_path_quant=os.path.join(batch_element_dir, os.environ['OPERATOR_IN_DIR_QUANT'])
    in_path_brainvis=os.path.join(batch_element_dir, os.environ['OPERATOR_IN_DIR_BRAINVIS'])
    out_path=os.path.join(batch_element_dir, os.environ['OPERATOR_OUT_DIR'])

    if not os.path.exists(out_path):
        os.makedirs(out_path)

    pdf_file_path = os.path.join(out_path, "{}.pdf".format(os.path.basename(batch_element_dir)))
    html2pdf._main(pdf_file_path,in_path_biomarker,in_path_quant,in_path_brainvis)