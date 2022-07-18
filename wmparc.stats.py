import pandas  as pd
import numpy as np
import os 
from math import *
import scipy.stats
import pingouin as pg

os.chdir("/Users/jackychen/OneDrive - University College London/SINGLE_TASK/stats_parsing_result")


KAO = pd.read_csv("AI_re/wmparc.stats.csv")
AI = pd.read_csv("AI new/wmparc.stats.csv")

#patient = []
#for i in AI["patient ID"]:
#    patient.append(i[: -11])
#AI["patient ID"] = patient

columns_changed = {'1-NVoxels':'wm-lh-bankssts-NVoxels',
                   '1-Volume_mm3':'wm-lh-bankssts-Volume_mm3',
                   '2-NVoxels':'wm-lh-caudalanteriorcingulate-NVoxels',
                   '2-Volume_mm3':'wm-lh-caudalanteriorcingulate-Volume_mm3',
                   '3-NVoxels':'wm-lh-caudalmiddlefrontal-NVoxels',
                   '3-Volume_mm3':'wm-lh-caudalmiddlefrontal-Volume_mm3',  
                   '4-NVoxels':'wm-lh-cuneus-NVoxels',
                   '4-Volume_mm3':'wm-lh-cuneus-Volume_mm3',
                   '5-NVoxels':'wm-lh-entorhinal-NVoxels',
                   '5-Volume_mm3':'wm-lh-entorhinal-Volume_mm3',
                   '6-NVoxels':'wm-lh-fusiform-NVoxels',
                   '6-Volume_mm3':'wm-lh-fusiform-Volume_mm3',
                   '7-NVoxels':'wm-lh-inferiorparietal-NVoxels',
                   '7-Volume_mm3':'wm-lh-inferiorparietal-Volume_mm3',
                   '8-NVoxels':'wm-lh-inferiortemporal-NVoxels',
                   '8-Volume_mm3':'wm-lh-inferiortemporal-Volume_mm3',
                   '9-NVoxels':'wm-lh-isthmuscingulate-NVoxels',
                   '9-Volume_mm3':'wm-lh-isthmuscingulate-Volume_mm3',
                   '10-NVoxels':'wm-lh-lateraloccipital-NVoxels',
                   '10-Volume_mm3':'wm-lh-lateraloccipital-Volume_mm3',
                   '11-NVoxels':'wm-lh-lateralorbitofrontal-NVoxels',
                   '11-Volume_mm3':'wm-lh-lateralorbitofrontal-Volume_mm3',                  
                   '12-NVoxels':'wm-lh-lingual-NVoxels',
                   '12-Volume_mm3':'wm-lh-lingual-Volume_mm3',
                   '13-NVoxels':'wm-lh-medialorbitofrontal-NVoxels',
                   '13-Volume_mm3':'wm-lh-medialorbitofrontal-Volume_mm3',
                   '14-NVoxels':'wm-lh-middletemporal-NVoxels',
                   '14-Volume_mm3':'wm-lh-middletemporal-Volume_mm3',
                   '15-NVoxels':'wm-lh-parahippocampal-NVoxels',
                   '15-Volume_mm3':'wm-lh-parahippocampal-Volume_mm3',
                   '16-NVoxels':'wm-lh-paracentral-NVoxels',
                   '16-Volume_mm3':'wm-lh-paracentral-Volume_mm3',
                   '17-NVoxels':'wm-lh-parsopercularis-NVoxels',
                   '17-Volume_mm3':'wm-lh-parsopercularis-Volume_mm3',
                   '18-NVoxels':'wm-lh-parsorbitalis-NVoxels',
                   '18-Volume_mm3':'wm-lh-parsorbitalis-Volume_mm3',
                   '19-NVoxels':'wm-lh-parstriangularis-NVoxels',
                   '19-Volume_mm3':'wm-lh-parstriangularis-Volume_mm3',
                   '20-NVoxels':'wm-lh-pericalcarine-NVoxels',
                   '20-Volume_mm3':'wm-lh-pericalcarine-Volume_mm3',
                   '21-NVoxels':'wm-lh-postcentral-NVoxels',
                   '21-Volume_mm3':'wm-lh-postcentral-Volume_mm3',  
                   '22-NVoxels':'wm-lh-posteriorcingulate-NVoxels',
                   '22-Volume_mm3':'wm-lh-posteriorcingulate-Volume_mm3',
                   '23-NVoxels':'wm-lh-precentral-NVoxels',
                   '23-Volume_mm3':'wm-lh-precentral-Volume_mm3',
                   '24-NVoxels':'wm-lh-precuneus-NVoxels',
                   '24-Volume_mm3':'wm-lh-precuneus-Volume_mm3',
                   '25-NVoxels':'wm-lh-rostralanteriorcingulate-NVoxels',
                   '25-Volume_mm3':'wm-lh-rostralanteriorcingulate-Volume_mm3',
                   '26-NVoxels':'wm-lh-rostralmiddlefrontal-NVoxels',
                   '26-Volume_mm3':'wm-lh-rostralmiddlefrontal-Volume_mm3',                 
                   '27-NVoxels':'wm-lh-superiorfrontal-NVoxels',
                   '27-Volume_mm3':'wm-lh-superiorfrontal-Volume_mm3',
                   '28-NVoxels':'wm-lh-superiorparietal-NVoxels',
                   '28-Volume_mm3':'wm-lh-superiorparietal-Volume_mm3',
                   '29-NVoxels':'wm-lh-superiortemporal-NVoxels',
                   '29-Volume_mm3':'wm-lh-superiortemporal-Volume_mm3',
                   '30-NVoxels':'wm-lh-supramarginal-NVoxels',
                   '30-Volume_mm3':'wm-lh-supramarginal-Volume_mm3',
                   '31-NVoxels':'wm-lh-frontalpole-NVoxels',
                   '31-Volume_mm3':'wm-lh-frontalpole-Volume_mm3',
                   '32-NVoxels':'wm-lh-temporalpole-NVoxels',
                   '32-Volume_mm3':'wm-lh-temporalpole-Volume_mm3',
                   '33-NVoxels':'wm-lh-transversetemporal-NVoxels',
                   '33-Volume_mm3':'wm-lh-transversetemporal-Volume_mm3',
                   '34-NVoxels':'wm-lh-insula-NVoxels',
                   '34-Volume_mm3':'wm-lh-insula-Volume_mm3',
                   '35-NVoxels':'wm-rh-bankssts-NVoxels',
                   '35-Volume_mm3':'wm-rh-bankssts-Volume_mm3',
                   '36-NVoxels':'wm-rh-caudalanteriorcingulate-NVoxels',
                   '36-Volume_mm3':'wm-rh-caudalanteriorcingulate-Volume_mm3',
                   '37-NVoxels':'wm-rh-caudalmiddlefrontal-NVoxels',
                   '37-Volume_mm3':'wm-rh-caudalmiddlefrontal-Volume_mm3',  
                   '38-NVoxels':'wm-rh-cuneus-NVoxels',
                   '38-Volume_mm3':'wm-rh-cuneus-Volume_mm3',
                   '39-NVoxels':'wm-rh-entorhinal-NVoxels',
                   '39-Volume_mm3':'wm-rh-entorhinal-Volume_mm3',
                   '40-NVoxels':'wm-rh-fusiform-NVoxels',
                   '40-Volume_mm3':'wm-rh-fusiform-Volume_mm3',
                   '41-NVoxels':'wm-rh-inferiorparietal-NVoxels',
                   '41-Volume_mm3':'wm-rh-inferiorparietal-Volume_mm3',
                   '42-NVoxels':'wm-rh-inferiortemporal-NVoxels',
                   '42-Volume_mm3':'wm-rh-inferiortemporal-Volume_mm3',
                   '43-NVoxels':'wm-rh-isthmuscingulate-NVoxels',
                   '43-Volume_mm3':'wm-rh-isthmuscingulate-Volume_mm3',
                   '44-NVoxels':'wm-rh-lateraloccipital-NVoxels',
                   '44-Volume_mm3':'wm-rh-lateraloccipital-Volume_mm3',
                   '45-NVoxels':'wm-rh-lateralorbitofrontal-NVoxels',
                   '45-Volume_mm3':'wm-rh-lateralorbitofrontal-Volume_mm3',                  
                   '46-NVoxels':'wm-rh-lingual-NVoxels',
                   '46-Volume_mm3':'wm-rh-lingual-Volume_mm3',
                   '47-NVoxels':'wm-rh-medialorbitofrontal-NVoxels',
                   '47-Volume_mm3':'wm-rh-medialorbitofrontal-Volume_mm3',
                   '48-NVoxels':'wm-rh-middletemporal-NVoxels',
                   '48-Volume_mm3':'wm-rh-middletemporal-Volume_mm3',
                   '49-NVoxels':'wm-rh-parahippocampal-NVoxels',
                   '49-Volume_mm3':'wm-rh-parahippocampal-Volume_mm3',
                   '50-NVoxels':'wm-rh-paracentral-NVoxels',
                   '50-Volume_mm3':'wm-rh-paracentral-Volume_mm3',
                   '51-NVoxels':'wm-rh-parsopercularis-NVoxels',
                   '51-Volume_mm3':'wm-rh-parsopercularis-Volume_mm3',
                   '52-NVoxels':'wm-rh-parsorbitalis-NVoxels',
                   '52-Volume_mm3':'wm-rh-parsorbitalis-Volume_mm3',
                   '53-NVoxels':'wm-rh-parstriangularis-NVoxels',
                   '53-Volume_mm3':'wm-rh-parstriangularis-Volume_mm3',
                   '54-NVoxels':'wm-rh-pericalcarine-NVoxels',
                   '54-Volume_mm3':'wm-rh-pericalcarine-Volume_mm3',
                   '55-NVoxels':'wm-rh-postcentral-NVoxels',
                   '55-Volume_mm3':'wm-rh-postcentral-Volume_mm3',  
                   '56-NVoxels':'wm-rh-posteriorcingulate-NVoxels',
                   '56-Volume_mm3':'wm-rh-posteriorcingulate-Volume_mm3',
                   '57-NVoxels':'wm-rh-precentral-NVoxels',
                   '57-Volume_mm3':'wm-rh-precentral-Volume_mm3',
                   '58-NVoxels':'wm-rh-precuneus-NVoxels',
                   '58-Volume_mm3':'wm-rh-precuneus-Volume_mm3',
                   '59-NVoxels':'wm-rh-rostralanteriorcingulate-NVoxels',
                   '59-Volume_mm3':'wm-rh-rostralanteriorcingulate-Volume_mm3',
                   '60-NVoxels':'wm-rh-rostralmiddlefrontal-NVoxels',
                   '60-Volume_mm3':'wm-rh-rostralmiddlefrontal-Volume_mm3',                 
                   '61-NVoxels':'wm-rh-superiorfrontal-NVoxels',
                   '61-Volume_mm3':'wm-rh-superiorfrontal-Volume_mm3',
                   '62-NVoxels':'wm-rh-superiorparietal-NVoxels',
                   '62-Volume_mm3':'wm-rh-superiorparietal-Volume_mm3',
                   '63-NVoxels':'wm-rh-superiortemporal-NVoxels',
                   '63-Volume_mm3':'wm-rh-superiortemporal-Volume_mm3',
                   '64-NVoxels':'wm-rh-supramarginal-NVoxels',
                   '64-Volume_mm3':'wm-rh-supramarginal-Volume_mm3',
                   '65-NVoxels':'wm-rh-frontalpole-NVoxels',
                   '65-Volume_mm3':'wm-rh-frontalpole-Volume_mm3',
                   '66-NVoxels':'wm-rh-temporalpole-NVoxels',
                   '66-Volume_mm3':'wm-rh-temporalpole-Volume_mm3',
                   '67-NVoxels':'wm-rh-transversetemporal-NVoxels',
                   '67-Volume_mm3':'wm-rh-transversetemporal-Volume_mm3',
                   '68-NVoxels':'wm-rh-insula-NVoxels',
                   '68-Volume_mm3':'wm-rh-insula-Volume_mm3',
                   '69-NVoxels':'Left-UnsegmentedWhiteMatter-NVoxels',
                   '69-Volume_mm3':'Left-UnsegmentedWhiteMatter-Volume_mm3',
                   '70-NVoxels':'Right-UnsegmentedWhiteMatter-NVoxels',
                   '70-Volume_mm3':'Right-UnsegmentedWhiteMatter-Volume_mm3'
                   }
AI.rename(columns = columns_changed, inplace=True)
KAO.rename(columns = columns_changed, inplace=True)

columns_selected = ['patient ID','wm-lh-bankssts-NVoxels','wm-lh-bankssts-Volume_mm3',
                   'wm-lh-caudalanteriorcingulate-NVoxels','wm-lh-caudalanteriorcingulate-Volume_mm3',  
                   'wm-lh-caudalmiddlefrontal-NVoxels','wm-lh-caudalmiddlefrontal-Volume_mm3',
                   'wm-lh-cuneus-NVoxels','wm-lh-cuneus-Volume_mm3',
                   'wm-lh-entorhinal-NVoxels','wm-lh-entorhinal-Volume_mm3',
                   'wm-lh-fusiform-NVoxels','wm-lh-fusiform-Volume_mm3',
                   'wm-lh-inferiorparietal-NVoxels','wm-lh-inferiorparietal-Volume_mm3',
                   'wm-lh-inferiortemporal-NVoxels','wm-lh-inferiortemporal-Volume_mm3',
                   'wm-lh-isthmuscingulate-NVoxels','wm-lh-isthmuscingulate-Volume_mm3',
                   'wm-lh-lateraloccipital-NVoxels','wm-lh-lateraloccipital-Volume_mm3',                  
                   'wm-lh-lateralorbitofrontal-NVoxels','wm-lh-lateralorbitofrontal-Volume_mm3',
                   'wm-lh-lingual-NVoxels','wm-lh-lingual-Volume_mm3',
                   'wm-lh-medialorbitofrontal-NVoxels','wm-lh-medialorbitofrontal-Volume_mm3',
                   'wm-lh-middletemporal-NVoxels','wm-lh-middletemporal-Volume_mm3',
                   'wm-lh-parahippocampal-NVoxels','wm-lh-parahippocampal-Volume_mm3',
                   'wm-lh-paracentral-NVoxels','wm-lh-paracentral-Volume_mm3',
                   'wm-lh-parsopercularis-NVoxels','wm-lh-parsopercularis-Volume_mm3',
                   'wm-lh-parsorbitalis-NVoxels','wm-lh-parsorbitalis-Volume_mm3',
                   'wm-lh-parstriangularis-NVoxels','wm-lh-parstriangularis-Volume_mm3',
                   'wm-lh-pericalcarine-NVoxels','wm-lh-pericalcarine-Volume_mm3',  
                   'wm-lh-postcentral-NVoxels','wm-lh-postcentral-Volume_mm3',
                   'wm-lh-posteriorcingulate-NVoxels','wm-lh-posteriorcingulate-Volume_mm3',
                   'wm-lh-precentral-NVoxels','wm-lh-precentral-Volume_mm3',
                   'wm-lh-precuneus-NVoxels','wm-lh-precuneus-Volume_mm3',
                   'wm-lh-rostralanteriorcingulate-NVoxels','wm-lh-rostralanteriorcingulate-Volume_mm3',                 
                   'wm-lh-rostralmiddlefrontal-NVoxels','wm-lh-rostralmiddlefrontal-Volume_mm3',
                   'wm-lh-superiorfrontal-NVoxels','wm-lh-superiorfrontal-Volume_mm3',
                   'wm-lh-superiorparietal-NVoxels','wm-lh-superiorparietal-Volume_mm3',
                   'wm-lh-superiortemporal-NVoxels','wm-lh-superiortemporal-Volume_mm3',
                   'wm-lh-supramarginal-NVoxels','wm-lh-supramarginal-Volume_mm3',
                   'wm-lh-frontalpole-NVoxels','wm-lh-frontalpole-Volume_mm3',
                   'wm-lh-temporalpole-NVoxels','wm-lh-temporalpole-Volume_mm3',
                   'wm-lh-transversetemporal-NVoxels','wm-lh-transversetemporal-Volume_mm3',
                   'wm-lh-insula-NVoxels','wm-lh-insula-Volume_mm3',                   
                   'wm-rh-bankssts-NVoxels','wm-rh-bankssts-Volume_mm3',
                   'wm-rh-caudalanteriorcingulate-NVoxels','wm-rh-caudalanteriorcingulate-Volume_mm3',  
                   'wm-rh-caudalmiddlefrontal-NVoxels','wm-rh-caudalmiddlefrontal-Volume_mm3',
                   'wm-rh-cuneus-NVoxels','wm-rh-cuneus-Volume_mm3',
                   'wm-rh-entorhinal-NVoxels','wm-rh-entorhinal-Volume_mm3',
                   'wm-rh-fusiform-NVoxels','wm-rh-fusiform-Volume_mm3',
                   'wm-rh-inferiorparietal-NVoxels','wm-rh-inferiorparietal-Volume_mm3',
                   'wm-rh-inferiortemporal-NVoxels','wm-rh-inferiortemporal-Volume_mm3',
                   'wm-rh-isthmuscingulate-NVoxels','wm-rh-isthmuscingulate-Volume_mm3',
                   'wm-rh-lateraloccipital-NVoxels','wm-rh-lateraloccipital-Volume_mm3',                  
                   'wm-rh-lateralorbitofrontal-NVoxels','wm-rh-lateralorbitofrontal-Volume_mm3',
                   'wm-rh-lingual-NVoxels','wm-rh-lingual-Volume_mm3',
                   'wm-rh-medialorbitofrontal-NVoxels','wm-rh-medialorbitofrontal-Volume_mm3',
                   'wm-rh-middletemporal-NVoxels','wm-rh-middletemporal-Volume_mm3',
                   'wm-rh-parahippocampal-NVoxels','wm-rh-parahippocampal-Volume_mm3',
                   'wm-rh-paracentral-NVoxels','wm-rh-paracentral-Volume_mm3',
                   'wm-rh-parsopercularis-NVoxels','wm-rh-parsopercularis-Volume_mm3',
                   'wm-rh-parsorbitalis-NVoxels','wm-rh-parsorbitalis-Volume_mm3',
                   'wm-rh-parstriangularis-NVoxels','wm-rh-parstriangularis-Volume_mm3',
                   'wm-rh-pericalcarine-NVoxels','wm-rh-pericalcarine-Volume_mm3',  
                   'wm-rh-postcentral-NVoxels','wm-rh-postcentral-Volume_mm3',
                   'wm-rh-posteriorcingulate-NVoxels','wm-rh-posteriorcingulate-Volume_mm3',
                   'wm-rh-precentral-NVoxels','wm-rh-precentral-Volume_mm3',
                   'wm-rh-precuneus-NVoxels','wm-rh-precuneus-Volume_mm3',
                   'wm-rh-rostralanteriorcingulate-NVoxels','wm-rh-rostralanteriorcingulate-Volume_mm3',                 
                   'wm-rh-rostralmiddlefrontal-NVoxels','wm-rh-rostralmiddlefrontal-Volume_mm3',
                   'wm-rh-superiorfrontal-NVoxels','wm-rh-superiorfrontal-Volume_mm3',
                   'wm-rh-superiorparietal-NVoxels','wm-rh-superiorparietal-Volume_mm3',
                   'wm-rh-superiortemporal-NVoxels','wm-rh-superiortemporal-Volume_mm3',
                   'wm-rh-supramarginal-NVoxels','wm-rh-supramarginal-Volume_mm3',
                   'wm-rh-frontalpole-NVoxels','wm-rh-frontalpole-Volume_mm3',
                   'wm-rh-temporalpole-NVoxels','wm-rh-temporalpole-Volume_mm3',
                   'wm-rh-transversetemporal-NVoxels','wm-rh-transversetemporal-Volume_mm3',
                   'wm-rh-insula-NVoxels','wm-rh-insula-Volume_mm3',
                   'Left-UnsegmentedWhiteMatter-NVoxels','Left-UnsegmentedWhiteMatter-Volume_mm3',
                   'Right-UnsegmentedWhiteMatter-NVoxels','Right-UnsegmentedWhiteMatter-Volume_mm3']

AI = AI[columns_selected]
KAO = KAO[columns_selected]
KAO_AI = pd.merge(KAO, AI, how = 'inner', on = "patient ID", suffixes = ("_KAO", "_AI"))

KAO_AI.to_csv("AI_RESULT/AI_AI/AI_AI_wmparc.stats.csv", index = False)

KAO_part = KAO_AI.loc[: , "wm-lh-bankssts-NVoxels_KAO" : "Right-UnsegmentedWhiteMatter-Volume_mm3_KAO"]
AI_part = KAO_AI.loc[: , "wm-lh-bankssts-NVoxels_AI" : "Right-UnsegmentedWhiteMatter-Volume_mm3_AI"]

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

    icc_value = pg.intraclass_corr(data=KAO_AI_icc, targets='targets', raters='raters', ratings='scores', nan_policy='omit')
    icc.append(icc_value["ICC"][2])
    
wmparc_stats = pd.DataFrame([Mean_KAO,sd_KAO,Mean_AI,sd_AI,Mean_Diff,Mean_Diff_Percentage,
                                         sd_Diff,sd_Diff_Percentage,se_Diff,se_Diff_Percentage,min_Diff,
                                         min_Diff_Percentage,max_Diff,max_Diff_Percentage,median,Mean_ABsDiff,
                                         Mean_ABsDiff_Percentage,sd_ABsDiff,sd_ABsDiff_Percentage,se_ABsDiff,
                                         se_ABsDiff_Percentage,min_ABsDiff,min_ABsDiff_Percentage,max_ABsDiff,
                                         max_ABsDiff_Percentage,icc,p_value,negative_log10_p]).T

wmparc_stats.columns = ['Mean_AI_re','sd_AI_re','Mean_AI','sd_AI','Mean_Diff','Mean_Diff_%',
                                    'sd_Diff','sd_Diff_%','se_Diff','se_Diff_%','min_Diff',
                                    'min_Diff_%','max_Diff','max_Diff_%','median','Mean_ABsDiff',
                                    'Mean_ABsDiff_%','sd_ABsDiff','sd_ABsDiff_%','se_ABsDiff',
                                    'se_ABsDiff_%','min_ABsDiff','min_ABsDiff_%','max_ABsDiff',
                                    'max_ABsDiff_%','ICC','p-value','(-)log10(p)']

df_index = []
for i in KAO_part.columns:
    df_index.append(i[: -4])
wmparc_stats.index = df_index
wmparc_stats.index.name = "Structure"

wmparc_stats.fillna("NaN", inplace=True)
    
wmparc_stats.to_csv("AI_RESULT/COMPARISON/comparison_wmparc.stats.csv")

