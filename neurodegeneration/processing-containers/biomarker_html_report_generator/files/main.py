import os
import shutil
import pandas as pd

from roi_quantifier.roi_quantifier import roi_quantifier_main
from spare_calculator.spare_calculator import spare_main
from normative_biomarker_visualizer.normative_biomarker_visualizer import biomarker_main

def main(muse_roi, dlicv_mask,  wmls_mask, dcm_json):
    
    ## Create a tmp directory to store the intermediate results
    tmp_dir = 'tmp'
    
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)
        
    os.mkdir(tmp_dir)
    
    ######################## Put all the intermediate output into the tmp folder##########################
    #      [UID]_all_MuseROIs_name.pkl – A dictionary with {‘ROI Name’: ‘ROI volume’}                    #
    #      [UID]_all_MuseROIs_num.pkl - A dictionary with {‘ROI Index’: ‘ROI volume’}                    #
    #      [UID]_allz_num.pkl - A dictionary with {‘ROI Index’: ‘Normalized ROI volume’}                 #
    #      [UID]_allz.pkl - A dictionary with {‘ROI Name’: ‘Normalized ROI volume’}                      #
    #      [UID]_dfPat.pkl - Patient Information includes patient ID, Age, Sex, dates                    #
    #      [UID]_dfRef.pkl - Reference Information                                                       #   
    #      [UID]_dfSub.pkl - Subject Information                                                         #
    #      [UID]_WMLSref.pkl - WMLS Reference Information                                                #
    ######################################################################################################
    
    dfSub, dfRef, WMLSref, dfPat, allz_num, allz, all_MuseROIs_num, all_MuseROIs_name = roi_quantifier_main(muse_roi, dlicv_mask, wmls_mask, dcm_json, './tmp/tmp.pdf')
    
    ######################## Put all the intermediate output into the tmp folder##########################
    #      [UID]_spareAD.pkl – SPARE AD score (single value)                                             #
    #      [UID]_spareBA.pkl - SPARE BA score (single value)                                             #
    ######################################################################################################
    
    spareAD, spareBA = spare_main(dfSub, all_MuseROIs_num, './tmp/tmp.pdf')
    
    ######################## Put all the intermediate output into the tmp folder##########################
    #      [UID]_flagtable.pkl –  html file contains table information (Brain Volumetry and Comparison   #
    #                                  with Normative Harmonized Population Values)                      #                      
    #      [UID]_roisubsettable.pkl - A html file contains table information (Regions that differ the    #
    #                                 most from normal                                                   #
    #      [UID]_plot.png                                                                                #
    #      [UID]_all_MuseROIs_num.pkl - A dictionary with {‘ROI Index’: ‘ROI volume’}                    #
    #      [UID]_all_MuseROIs_name.pkl – A dictionary with {‘ROI Name’: ‘ROI volume’}                    #
    #      [UID]_all_MuseROIs_num.pkl - A dictionary with {‘ROI Index’: ‘ROI volume’}                    #
    #      [UID]_allz_num.pkl - A dictionary with {‘ROI Index’: ‘Normalized ROI volume’}                 #
    #      [UID]_allz.pkl - A dictionary with {‘ROI Name’: ‘Normalized ROI volume’}                      #
    #      [UID]_dfPat.pkl - Patient Information includes patient ID, Age, Sex, dates                    #
    #      [UID]_dfRef.pkl - Reference Information                                                       #   
    #      [UID]_dfSub.pkl - Subject Information                                                         #
    #      [UID]_WMLSref.pkl - WMLS Reference Information                                                #
    ######################################################################################################
    
    dfSub = pd.read_pickle('./tmp/tmp_dfSub.pkl')
    dfRef = pd.read_pickle('./tmp/tmp_dfRef.pkl')
    WMLSref = pd.read_pickle('./tmp/tmp_WMLSref.pkl')
    allz_num = pd.read_pickle('./tmp/tmp_allz_num.pkl')
    allz = pd.read_pickle('./tmp/tmp_allz.pkl')
    all_MuseROIs_name = pd.read_pickle('./tmp/tmp_all_MuseROIs_name.pkl')
    spareAD = pd.read_pickle('./tmp/tmp_spareAD.pkl')
    spareBA = pd.read_pickle('./tmp/tmp_spareBA.pkl')
    
    
    biomarker_main(dfSub, dfRef, WMLSref, allz_num, allz, all_MuseROIs_name, spareAD, spareBA, './tmp/tmp.pdf')

    #output is a single html file + all files required by csv_extraction container
    
    
if __name__ == '__main__':
    # roi = ['/home/diwu/Desktop/kaapana-data-to-check-brainviz/F1/2.16.840.1.114362.1.12066432.24920037488.604832115.605.168/relabel/2.16.840.1.114362.1.12066432.24920037488.604832115.605.168.nii.gz']
    # icv = ['/home/diwu/Desktop/kaapana-data-to-check-brainviz/F1/2.16.840.1.114362.1.12066432.24920037488.604832115.605.168/dlicv-inference/2.16.840.1.114362.1.12066432.24920037488.604832115.605.168.nii.gz']
    # wmls = ['/home/diwu/Desktop/kaapana-data-to-check-brainviz/F1/2.16.840.1.114362.1.12066432.24920037488.604832115.605.168/wmls/2.16.840.1.114362.1.12066432.24920037488.604832115.605.168.nii.gz']
    # _json = '/home/diwu/Desktop/kaapana-data-to-check-brainviz/F1/2.16.840.1.114362.1.12066432.24920037488.604832115.605.168/GetT1Metadata/2.16.840.1.114362.1.12066432.24920037488.604832115.605.168.json'
    
    roi = ['/home/diwu/Desktop/5datasets_F8F12F18M13M5/F8/batch/2.16.840.1.114362.1.12066432.24920037488.604832630.1009.6328/extract_muse_result/2.16.840.1.114362.1.12066432.24920037488.604832630.1009.6328.nii.gz']
    icv = ['/home/diwu/Desktop/5datasets_F8F12F18M13M5/F8/batch/2.16.840.1.114362.1.12066432.24920037488.604832630.1009.6328/extract_dlicv_result/2.16.840.1.114362.1.12066432.24920037488.604832630.1009.6328.nii.gz']
    wmls = ['/home/diwu/Desktop/5datasets_F8F12F18M13M5/F8/batch/2.16.840.1.114362.1.12066432.24920037488.604832630.1009.6328/wmls-output/2.16.840.1.114362.1.12066432.24920037488.604832630.1009.6328.nii.gz']
    _json = '/home/diwu/Desktop/5datasets_F8F12F18M13M5/F8/batch/2.16.840.1.114362.1.12066432.24920037488.604832630.1009.6328/GetT1Metadata/2.16.840.1.114362.1.12066432.24920037488.604832630.1009.6328.json'
    
    main(roi, icv, wmls, _json)