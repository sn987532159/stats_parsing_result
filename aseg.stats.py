import pandas  as pd
import numpy as np
import os 
from math import *
import scipy.stats
import pingouin as pg

os.chdir("/Users/jackychen/OneDrive - University College London/SINGLE_TASK/stats_parsing_result")


KAO = pd.read_csv("AI_re/aseg.stats.csv")
AI = pd.read_csv("AI new/aseg.stats.csv")

#patient = []
#for i in AI["patient ID"]:
#    patient.append(i[: -11])
#AI["patient ID"] = patient

columns_changed = {'1-NVoxels':'Left-Lateral-Ventricle-NVoxels',
                   '1-Volume_mm3':'Left-Lateral-Ventricle-Volume_mm3',
                   '2-NVoxels':'Left-Inf-Lat-Vent-NVoxels',
                   '2-Volume_mm3':'Left-Inf-Lat-Vent-Volume_mm3',
                   '3-NVoxels':'Left-Cerebellum-White-Matter-NVoxels',
                   '3-Volume_mm3':'Left-Cerebellum-White-Matter-Volume_mm3',  
                   '4-NVoxels':'Left-Cerebellum-Cortex-NVoxels',
                   '4-Volume_mm3':'Left-Cerebellum-Cortex-Volume_mm3',
                   '5-NVoxels':'Left-Thalamus-NVoxels',
                   '5-Volume_mm3':'Left-Thalamus-Volume_mm3',
                   '6-NVoxels':'Left-Caudate-NVoxels',
                   '6-Volume_mm3':'Left-Caudate-Volume_mm3',
                   '7-NVoxels':'Left-Putamen-NVoxels',
                   '7-Volume_mm3':'Left-Putamen-Volume_mm3',
                   '8-NVoxels':'Left-Pallidum-NVoxels',
                   '8-Volume_mm3':'Left-Pallidum-Volume_mm3',
                   '9-NVoxels':'3rd-Ventricle-NVoxels',
                   '9-Volume_mm3':'3rd-Ventricle-Volume_mm3',
                   '10-NVoxels':'4th-Ventricle-NVoxels',
                   '10-Volume_mm3':'4th-Ventricle-Volume_mm3',
                   '11-NVoxels':'Brain-Stem-NVoxels',
                   '11-Volume_mm3':'Brain-Stem-Volume_mm3',                  
                   '12-NVoxels':'Left-Hippocampus-NVoxels',
                   '12-Volume_mm3':'Left-Hippocampus-Volume_mm3',
                   '13-NVoxels':'Left-Amygdala-NVoxels',
                   '13-Volume_mm3':'Left-Amygdala-Volume_mm3',
                   '14-NVoxels':'CSF-NVoxels',
                   '14-Volume_mm3':'CSF-Volume_mm3',
                   '15-NVoxels':'Left-Accumbens-area-NVoxels',
                   '15-Volume_mm3':'Left-Accumbens-area-Volume_mm3',
                   '16-NVoxels':'Left-VentralDC-NVoxels',
                   '16-Volume_mm3':'Left-VentralDC-Volume_mm3',
                   '17-NVoxels':'Left-vessel-NVoxels',
                   '17-Volume_mm3':'Left-vessel-Volume_mm3',
                   '18-NVoxels':'Left-choroid-plexus-NVoxels',
                   '18-Volume_mm3':'Left-choroid-plexus-Volume_mm3',
                   '19-NVoxels':'Right-Lateral-Ventricle-NVoxels',
                   '19-Volume_mm3':'Right-Lateral-Ventricle-Volume_mm3',
                   '20-NVoxels':'Right-Inf-Lat-Vent-NVoxels',
                   '20-Volume_mm3':'Right-Inf-Lat-Vent-Volume_mm3',
                   '21-NVoxels':'Right-Cerebellum-White-Matter-NVoxels',
                   '21-Volume_mm3':'Right-Cerebellum-White-Matter-Volume_mm3',  
                   '22-NVoxels':'Right-Cerebellum-Cortex-NVoxels',
                   '22-Volume_mm3':'Right-Cerebellum-Cortex-Volume_mm3',
                   '23-NVoxels':'Right-Thalamus-NVoxels',
                   '23-Volume_mm3':'Right-Thalamus-Volume_mm3',
                   '24-NVoxels':'Right-Caudate-NVoxels',
                   '24-Volume_mm3':'Right-Caudate-Volume_mm3',
                   '25-NVoxels':'Right-Putamen-NVoxels',
                   '25-Volume_mm3':'Right-Putamen-Volume_mm3',
                   '26-NVoxels':'Right-Pallidum-NVoxels',
                   '26-Volume_mm3':'Right-Pallidum-Volume_mm3',                 
                   '27-NVoxels':'Right-Hippocampus-NVoxels',
                   '27-Volume_mm3':'Right-Hippocampus-Volume_mm3',
                   '28-NVoxels':'Right-Amygdala-NVoxels',
                   '28-Volume_mm3':'Right-Amygdala-Volume_mm3',
                   '29-NVoxels':'Right-Accumbens-area-NVoxels',
                   '29-Volume_mm3':'Right-Accumbens-area-Volume_mm3',
                   '30-NVoxels':'Right-VentralDC-NVoxels',
                   '30-Volume_mm3':'Right-VentralDC-Volume_mm3',
                   '31-NVoxels':'Right-vessel-NVoxels',
                   '31-Volume_mm3':'Right-vessel-Volume_mm3',
                   '32-NVoxels':'Right-choroid-plexus-NVoxels',
                   '32-Volume_mm3':'Right-choroid-plexus-Volume_mm3',
                   '33-NVoxels':'5th-Ventricle-NVoxels',
                   '33-Volume_mm3':'5th-Ventricle-Volume_mm3',
                   '34-NVoxels':'WM-hypointensities-NVoxels',
                   '34-Volume_mm3':'WM-hypointensities-Volume_mm3',
                   '35-NVoxels':'Left-WM-hypointensities-NVoxels',
                   '35-Volume_mm3':'Left-WM-hypointensities-Volume_mm3',  
                   '36-NVoxels':'Right-WM-hypointensities-NVoxels',
                   '36-Volume_mm3':'Right-WM-hypointensities-Volume_mm3',
                   '37-NVoxels':'non-WM-hypointensities-NVoxels',
                   '37-Volume_mm3':'non-WM-hypointensities-Volume_mm3',
                   '38-NVoxels':'Left-non-WM-hypointensities-NVoxels',
                   '38-Volume_mm3':'Left-non-WM-hypointensities-Volume_mm3',
                   '39-NVoxels':'Right-non-WM-hypointensities-NVoxels',
                   '39-Volume_mm3':'Right-non-WM-hypointensities-Volume_mm3',
                   '40-NVoxels':'Optic-Chiasm-NVoxels',
                   '40-Volume_mm3':'Optic-Chiasm-Volume_mm3',                 
                   '41-NVoxels':'CC_Posterior-NVoxels',
                   '41-Volume_mm3':'CC_Posterior-Volume_mm3',
                   '42-NVoxels':'CC_Mid_Posterior-NVoxels',
                   '42-Volume_mm3':'CC_Mid_Posterior-Volume_mm3',
                   '43-NVoxels':'CC_Central-NVoxels',
                   '43-Volume_mm3':'CC_Central-Volume_mm3',
                   '44-NVoxels':'CC_Mid_Anterior-NVoxels',
                   '44-Volume_mm3':'CC_Mid_Anterior-Volume_mm3',
                   '45-NVoxels':'CC_Anterior-NVoxels',
                   '45-Volume_mm3':'CC_Anterior-Volume_mm3'
                   }
AI.rename(columns = columns_changed, inplace=True)
KAO.rename(columns = columns_changed, inplace=True)

columns_selected = ['patient ID', 'Left-Lateral-Ventricle-NVoxels', 'Left-Lateral-Ventricle-Volume_mm3',
                     'Left-Inf-Lat-Vent-NVoxels','Left-Inf-Lat-Vent-Volume_mm3',
                     'Left-Cerebellum-White-Matter-NVoxels','Left-Cerebellum-White-Matter-Volume_mm3',  
                     'Left-Cerebellum-Cortex-NVoxels','Left-Cerebellum-Cortex-Volume_mm3',
                     'Left-Thalamus-NVoxels','Left-Thalamus-Volume_mm3',
                     'Left-Caudate-NVoxels','Left-Caudate-Volume_mm3',
                     'Left-Putamen-NVoxels','Left-Putamen-Volume_mm3',
                     'Left-Pallidum-NVoxels','Left-Pallidum-Volume_mm3',
                     '3rd-Ventricle-NVoxels','3rd-Ventricle-Volume_mm3',
                     '4th-Ventricle-NVoxels','4th-Ventricle-Volume_mm3',
                     'Brain-Stem-NVoxels','Brain-Stem-Volume_mm3',
                     'Left-Hippocampus-NVoxels','Left-Hippocampus-Volume_mm3',
                     'Left-Amygdala-NVoxels','Left-Amygdala-Volume_mm3',
                     'CSF-NVoxels','CSF-Volume_mm3',
                     'Left-Accumbens-area-NVoxels','Left-Accumbens-area-Volume_mm3',
                     'Left-VentralDC-NVoxels','Left-VentralDC-Volume_mm3',
                     'Left-vessel-NVoxels','Left-vessel-Volume_mm3',
                     'Left-choroid-plexus-NVoxels','Left-choroid-plexus-Volume_mm3',
                     'Right-Lateral-Ventricle-NVoxels','Right-Lateral-Ventricle-Volume_mm3',
                     'Right-Inf-Lat-Vent-NVoxels','Right-Inf-Lat-Vent-Volume_mm3',
                     'Right-Cerebellum-White-Matter-NVoxels','Right-Cerebellum-White-Matter-Volume_mm3',  
                     'Right-Cerebellum-Cortex-NVoxels','Right-Cerebellum-Cortex-Volume_mm3',
                      'Right-Thalamus-NVoxels','Right-Thalamus-Volume_mm3',
                      'Right-Caudate-NVoxels','Right-Caudate-Volume_mm3',
                      'Right-Putamen-NVoxels','Right-Putamen-Volume_mm3',
                      'Right-Pallidum-NVoxels','Right-Pallidum-Volume_mm3',  
                      'Right-Hippocampus-NVoxels','Right-Hippocampus-Volume_mm3',
                      'Right-Amygdala-NVoxels','Right-Amygdala-Volume_mm3',
                      'Right-Accumbens-area-NVoxels','Right-Accumbens-area-Volume_mm3',
                      'Right-VentralDC-NVoxels','Right-VentralDC-Volume_mm3',
                      'Right-vessel-NVoxels','Right-vessel-Volume_mm3',
                      'Right-choroid-plexus-NVoxels','Right-choroid-plexus-Volume_mm3',
                      '5th-Ventricle-NVoxels','5th-Ventricle-Volume_mm3',
                      'WM-hypointensities-NVoxels','WM-hypointensities-Volume_mm3',
                      'Left-WM-hypointensities-NVoxels','Left-WM-hypointensities-Volume_mm3',  
                      'Right-WM-hypointensities-NVoxels','Right-WM-hypointensities-Volume_mm3',
                      'non-WM-hypointensities-NVoxels','non-WM-hypointensities-Volume_mm3',
                      'Left-non-WM-hypointensities-NVoxels','Left-non-WM-hypointensities-Volume_mm3',
                      'Right-non-WM-hypointensities-NVoxels','Right-non-WM-hypointensities-Volume_mm3',
                      'Optic-Chiasm-NVoxels','Optic-Chiasm-Volume_mm3',                 
                      'CC_Posterior-NVoxels','CC_Posterior-Volume_mm3',
                      'CC_Mid_Posterior-NVoxels','CC_Mid_Posterior-Volume_mm3',
                      'CC_Central-NVoxels','CC_Central-Volume_mm3',
                      'CC_Mid_Anterior-NVoxels','CC_Mid_Anterior-Volume_mm3',
                      'CC_Anterior-NVoxels','CC_Anterior-Volume_mm3']
AI = AI[columns_selected]
KAO = KAO[columns_selected]
KAO_AI = pd.merge(KAO, AI, how = 'inner', on = "patient ID", suffixes = ("_KAO", "_AI"))

KAO_AI.to_csv("AI_RESULT/AI_AI/AI_AI_aseg.stats.csv", index = False)

KAO_part = KAO_AI.loc[: , "Left-Lateral-Ventricle-NVoxels_KAO" : "CC_Anterior-Volume_mm3_KAO"]
AI_part = KAO_AI.loc[: , "Left-Lateral-Ventricle-NVoxels_AI" : "CC_Anterior-Volume_mm3_AI"]

KAO_AI_DIFF = AI_part - KAO_part.values
KAO_AI_ABsDiff = abs(AI_part - KAO_part.values)


Mean_KAO = []
sd_KAO = []
for i in KAO_part:
    Mean_KAO.append(KAO_part[i].mean())
    sd_KAO.append(KAO_part[i].std())
    
Mean_AI = []
sd_AI = []
for i in AI_part:
    Mean_AI.append(AI_part[i].mean())
    sd_AI.append(AI_part[i].std())
    

Mean_add = (np.array(Mean_AI) + np.array(Mean_KAO))/2

    
Mean_Diff = np.array(Mean_AI) - np.array(Mean_KAO)

Mean_Diff_Percentage = (Mean_Diff/Mean_add)*100

sd_Diff = []
min_Diff = []
max_Diff = []
median = []
for i in KAO_AI_DIFF:
    sd_Diff.append(KAO_AI_DIFF[i].std())
    min_Diff.append(KAO_AI_DIFF[i].min())
    max_Diff.append(KAO_AI_DIFF[i].max())
    median.append(KAO_AI_DIFF[i].median())

sd_Diff_Percentage = (sd_Diff/Mean_add)*100

se_Diff = np.array(sd_Diff)/sqrt(len(KAO_part))

se_Diff_Percentage = (se_Diff/Mean_add)*100

min_Diff_Percentage = (min_Diff/Mean_add)*100

max_Diff_Percentage = (max_Diff/Mean_add)*100    

Mean_ABsDiff = []
sd_ABsDiff = []
min_ABsDiff = []
max_ABsDiff = []
for i in KAO_AI_DIFF:
    Mean_ABsDiff.append(KAO_AI_ABsDiff[i].mean())
    sd_ABsDiff.append(KAO_AI_ABsDiff[i].std())
    min_ABsDiff.append(KAO_AI_ABsDiff[i].min())
    max_ABsDiff.append(KAO_AI_ABsDiff[i].max())
    
Mean_ABsDiff_Percentage = (Mean_ABsDiff/Mean_add)*100

sd_ABsDiff_Percentage = (sd_ABsDiff/Mean_add)*100

se_ABsDiff = np.array(sd_ABsDiff)/sqrt(len(KAO_part))

se_ABsDiff_Percentage = (se_ABsDiff/Mean_add)*100

min_ABsDiff_Percentage = (min_ABsDiff/Mean_add)*100

max_ABsDiff_Percentage = (max_ABsDiff/Mean_add)*100 

p_value = scipy.stats.ttest_ind(KAO_part,AI_part, axis=0, nan_policy='omit')[1]
p_value = list(p_value)

negative_log10_p = []
for i in p_value:
    negative_log10_p.append(-log10(i))  
    

icc = []
for i in range(len(KAO_part.columns)):
    KAO_targets = range(len(KAO_part))
    KAO_raters = []
    KAO_scores = KAO_part.iloc[:, i].values
    kao_icc= pd.DataFrame([KAO_targets, KAO_raters, KAO_scores]).T
    kao_icc.columns = ["targets", "raters", "scores"]
    kao_icc["raters"] = "KAO"

    AI_targets = range(len(AI_part))
    AI_raters = []
    AI_scores = AI_part.iloc[:, i].values
    ai_icc= pd.DataFrame([AI_targets, AI_raters, AI_scores]).T
    ai_icc.columns = ["targets", "raters", "scores"]
    ai_icc["raters"] = "AI"

    KAO_AI_icc = pd.concat([kao_icc, ai_icc], axis = 0)

    icc_value = pg.intraclass_corr(data=KAO_AI_icc, targets='targets', raters='raters', ratings='scores')
    icc.append(icc_value["ICC"][2])
    
comparison_aseg_stats111 = pd.DataFrame([Mean_KAO,sd_KAO,Mean_AI,sd_AI,Mean_Diff,Mean_Diff_Percentage,
                                         sd_Diff,sd_Diff_Percentage,se_Diff,se_Diff_Percentage,min_Diff,
                                         min_Diff_Percentage,max_Diff,max_Diff_Percentage,median,Mean_ABsDiff,
                                         Mean_ABsDiff_Percentage,sd_ABsDiff,sd_ABsDiff_Percentage,se_ABsDiff,
                                         se_ABsDiff_Percentage,min_ABsDiff,min_ABsDiff_Percentage,max_ABsDiff,
                                         max_ABsDiff_Percentage,icc,p_value,negative_log10_p]).T

comparison_aseg_stats111.columns = ['Mean_AI_re','sd_AI_re','Mean_AI','sd_AI','Mean_Diff','Mean_Diff_%',
                                    'sd_Diff','sd_Diff_%','se_Diff','se_Diff_%','min_Diff',
                                    'min_Diff_%','max_Diff','max_Diff_%','median','Mean_ABsDiff',
                                    'Mean_ABsDiff_%','sd_ABsDiff','sd_ABsDiff_%','se_ABsDiff',
                                    'se_ABsDiff_%','min_ABsDiff','min_ABsDiff_%','max_ABsDiff',
                                    'max_ABsDiff_%','ICC','p-value','(-)log10(p)']

df_index = []
for i in KAO_part.columns:
    df_index.append(i[: -4])
comparison_aseg_stats111.index = df_index
comparison_aseg_stats111.index.name = "Structure"

comparison_aseg_stats111.fillna("NaN", inplace=True)
    
comparison_aseg_stats111.to_csv("AI_RESULT/COMPARISON/comparison_aseg.stats.csv")

