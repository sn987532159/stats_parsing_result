import pandas  as pd
import numpy as np
import os 
from math import *
import scipy.stats
import pingouin as pg

os.chdir("/Users/jackychen/OneDrive - University College London/SINGLE_TASK/stats_parsing_result")


KAO = pd.read_csv("AI_re/lh.w-g.pct.stats.csv")
AI = pd.read_csv("AI new/lh.w-g.pct.stats.csv")

#patient = []
#for i in AI["patient ID"]:
#    patient.append(i[: -11])
#AI["patient ID"] = patient

columns_changed = {'1-NVertices':'unknown-NVertices',
                   '1-Area_mm2':'unknown-Area_mm2',
                   '2-NVertices':'bankssts-NVertices',
                   '2-Area_mm2':'bankssts-Area_mm2',
                   '3-NVertices':'caudalanteriorcingulate-NVertices',
                   '3-Area_mm2':'caudalanteriorcingulate-Area_mm2',  
                   '4-NVertices':'caudalmiddlefrontal-NVertices',
                   '4-Area_mm2':'caudalmiddlefrontal-Area_mm2',
                   '5-NVertices':'cuneus-NVertices',
                   '5-Area_mm2':'cuneus-Area_mm2',
                   '6-NVertices':'entorhinal-NVertices',
                   '6-Area_mm2':'entorhinal-Area_mm2',
                   '7-NVertices':'fusiform-NVertices',
                   '7-Area_mm2':'fusiform-Area_mm2',
                   '8-NVertices':'inferiorparietal-NVertices',
                   '8-Area_mm2':'inferiorparietal-Area_mm2',
                   '9-NVertices':'inferiortemporal-NVertices',
                   '9-Area_mm2':'inferiortemporal-Area_mm2',
                   '10-NVertices':'isthmuscingulate-NVertices',
                   '10-Area_mm2':'isthmuscingulate-Area_mm2',
                   '11-NVertices':'lateraloccipital-NVertices',
                   '11-Area_mm2':'lateraloccipital-Area_mm2',                  
                   '12-NVertices':'lateralorbitofrontal-NVertices',
                   '12-Area_mm2':'lateralorbitofrontal-Area_mm2',
                   '13-NVertices':'lingual-NVertices',
                   '13-Area_mm2':'lingual-Area_mm2',
                   '14-NVertices':'medialorbitofrontal-NVertices',
                   '14-Area_mm2':'medialorbitofrontal-Area_mm2',
                   '15-NVertices':'middletemporal-NVertices',
                   '15-Area_mm2':'middletemporal-Area_mm2',
                   '16-NVertices':'parahippocampal-NVertices',
                   '16-Area_mm2':'parahippocampal-Area_mm2',
                   '17-NVertices':'paracentral-NVertices',
                   '17-Area_mm2':'paracentral-Area_mm2',
                   '18-NVertices':'parsopercularis-NVertices',
                   '18-Area_mm2':'parsopercularis-Area_mm2',
                   '19-NVertices':'parsorbitalis-NVertices',
                   '19-Area_mm2':'parsorbitalis-Area_mm2',
                   '20-NVertices':'parstriangularis-NVertices',
                   '20-Area_mm2':'parstriangularis-Area_mm2',
                   '21-NVertices':'pericalcarine-NVertices',
                   '21-Area_mm2':'pericalcarine-Area_mm2',  
                   '22-NVertices':'postcentral-NVertices',
                   '22-Area_mm2':'postcentral-Area_mm2',
                   '23-NVertices':'posteriorcingulate-NVertices',
                   '23-Area_mm2':'posteriorcingulate-Area_mm2',
                   '24-NVertices':'precentral-NVertices',
                   '24-Area_mm2':'precentral-Area_mm2',
                   '25-NVertices':'precuneus-NVertices',
                   '25-Area_mm2':'precuneus-Area_mm2',
                   '26-NVertices':'rostralanteriorcingulate-NVertices',
                   '26-Area_mm2':'rostralanteriorcingulate-Area_mm2',                 
                   '27-NVertices':'rostralmiddlefrontal-NVertices',
                   '27-Area_mm2':'rostralmiddlefrontal-Area_mm2',
                   '28-NVertices':'superiorfrontal-NVertices',
                   '28-Area_mm2':'superiorfrontal-Area_mm2',
                   '29-NVertices':'superiorparietal-NVertices',
                   '29-Area_mm2':'superiorparietal-Area_mm2',
                   '30-NVertices':'superiortemporal-NVertices',
                   '30-Area_mm2':'superiortemporal-Area_mm2',
                   '31-NVertices':'supramarginal-NVertices',
                   '31-Area_mm2':'supramarginal-Area_mm2',
                   '32-NVertices':'frontalpole-NVertices',
                   '32-Area_mm2':'frontalpole-Area_mm2',
                   '33-NVertices':'temporalpole-NVertices',
                   '33-Area_mm2':'temporalpole-Area_mm2',
                   '34-NVertices':'transversetemporal-NVertices',
                   '34-Area_mm2':'transversetemporal-Area_mm2',
                   '35-NVertices':'insula-NVertices',
                   '35-Area_mm2':'insula-Area_mm2'
                   }
AI.rename(columns = columns_changed, inplace=True)
KAO.rename(columns = columns_changed, inplace=True)

columns_selected = ['patient ID', 'unknown-NVertices', 'unknown-Area_mm2',
                   'bankssts-NVertices','bankssts-Area_mm2',
                   'caudalanteriorcingulate-NVertices','caudalanteriorcingulate-Area_mm2',  
                   'caudalmiddlefrontal-NVertices','caudalmiddlefrontal-Area_mm2',
                   'cuneus-NVertices','cuneus-Area_mm2',
                   'entorhinal-NVertices','entorhinal-Area_mm2',
                   'fusiform-NVertices','fusiform-Area_mm2',
                   'inferiorparietal-NVertices','inferiorparietal-Area_mm2',
                   'inferiortemporal-NVertices','inferiortemporal-Area_mm2',
                   'isthmuscingulate-NVertices','isthmuscingulate-Area_mm2',
                   'lateraloccipital-NVertices','lateraloccipital-Area_mm2',                  
                   'lateralorbitofrontal-NVertices','lateralorbitofrontal-Area_mm2',
                   'lingual-NVertices','lingual-Area_mm2',
                   'medialorbitofrontal-NVertices','medialorbitofrontal-Area_mm2',
                   'middletemporal-NVertices','middletemporal-Area_mm2',
                   'parahippocampal-NVertices','parahippocampal-Area_mm2',
                   'paracentral-NVertices','paracentral-Area_mm2',
                   'parsopercularis-NVertices','parsopercularis-Area_mm2',
                   'parsorbitalis-NVertices','parsorbitalis-Area_mm2',
                   'parstriangularis-NVertices','parstriangularis-Area_mm2',
                   'pericalcarine-NVertices','pericalcarine-Area_mm2',  
                   'postcentral-NVertices','postcentral-Area_mm2',
                   'posteriorcingulate-NVertices','posteriorcingulate-Area_mm2',
                   'precentral-NVertices','precentral-Area_mm2',
                   'precuneus-NVertices','precuneus-Area_mm2',
                   'rostralanteriorcingulate-NVertices','rostralanteriorcingulate-Area_mm2',                 
                   'rostralmiddlefrontal-NVertices','rostralmiddlefrontal-Area_mm2',
                   'superiorfrontal-NVertices','superiorfrontal-Area_mm2',
                   'superiorparietal-NVertices','superiorparietal-Area_mm2',
                   'superiortemporal-NVertices','superiortemporal-Area_mm2',
                   'supramarginal-NVertices','supramarginal-Area_mm2',
                   'frontalpole-NVertices','frontalpole-Area_mm2',
                   'temporalpole-NVertices','temporalpole-Area_mm2',
                   'transversetemporal-NVertices','transversetemporal-Area_mm2',
                   'insula-NVertices','insula-Area_mm2']
AI = AI[columns_selected]
KAO = KAO[columns_selected]
KAO_AI = pd.merge(KAO, AI, how = 'inner', on = "patient ID", suffixes = ("_KAO", "_AI"))

KAO_AI.to_csv("AI_RESULT/AI_AI/AI_AI_lh.w-g.pct.stats.csv", index = False)

KAO_part = KAO_AI.loc[: , "unknown-NVertices_KAO" : "insula-Area_mm2_KAO"]
AI_part = KAO_AI.loc[: , "unknown-NVertices_AI" : "insula-Area_mm2_AI"]

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
    
lh_w_g_pct_stats = pd.DataFrame([Mean_KAO,sd_KAO,Mean_AI,sd_AI,Mean_Diff,Mean_Diff_Percentage,
                                         sd_Diff,sd_Diff_Percentage,se_Diff,se_Diff_Percentage,min_Diff,
                                         min_Diff_Percentage,max_Diff,max_Diff_Percentage,median,Mean_ABsDiff,
                                         Mean_ABsDiff_Percentage,sd_ABsDiff,sd_ABsDiff_Percentage,se_ABsDiff,
                                         se_ABsDiff_Percentage,min_ABsDiff,min_ABsDiff_Percentage,max_ABsDiff,
                                         max_ABsDiff_Percentage,icc,p_value,negative_log10_p]).T

lh_w_g_pct_stats.columns = ['Mean_AI_re','sd_AI_re','Mean_AI','sd_AI','Mean_Diff','Mean_Diff_%',
                                    'sd_Diff','sd_Diff_%','se_Diff','se_Diff_%','min_Diff',
                                    'min_Diff_%','max_Diff','max_Diff_%','median','Mean_ABsDiff',
                                    'Mean_ABsDiff_%','sd_ABsDiff','sd_ABsDiff_%','se_ABsDiff',
                                    'se_ABsDiff_%','min_ABsDiff','min_ABsDiff_%','max_ABsDiff',
                                    'max_ABsDiff_%','ICC','p-value','(-)log10(p)']

df_index = []
for i in KAO_part.columns:
    df_index.append(i[: -4])
lh_w_g_pct_stats.index = df_index
lh_w_g_pct_stats.index.name = "Structure"

lh_w_g_pct_stats.fillna("NaN", inplace=True)
    
lh_w_g_pct_stats.to_csv("AI_RESULT/COMPARISON/comparison_lh.w-g.pct.stats.csv")

