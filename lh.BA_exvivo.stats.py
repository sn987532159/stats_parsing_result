import pandas  as pd
import numpy as np
import os 
from math import *
import scipy.stats
import pingouin as pg

os.chdir("/Users/jackychen/OneDrive - University College London/SINGLE_TASK/stats_parsing_result")


KAO = pd.read_csv("AI_re/lh.BA_exvivo.stats.csv")
AI = pd.read_csv("AI new/lh.BA_exvivo.stats.csv")

#patient = []
#for i in AI["patient ID"]:
#    patient.append(i[: -11])
#AI["patient ID"] = patient

KAO_AI = pd.merge(KAO, AI, how = 'inner', on = "patient ID", suffixes = ("_KAO", "_AI"))

KAO_AI.to_csv("AI_RESULT/AI_AI/AI_AI_lh.BA_exvivo.stats.csv", index = False)

KAO_part = KAO_AI.loc[: , "BA1_exvivo-NumVert_KAO" : "entorhinal_exvivo-CurvInd_KAO"]
AI_part = KAO_AI.loc[: , "BA1_exvivo-NumVert_AI" : "entorhinal_exvivo-CurvInd_AI"]

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

p_value = scipy.stats.ttest_ind(KAO_part, AI_part, axis=0, nan_policy='omit')[1]
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
    
lh_BA_exvivo_stats = pd.DataFrame([Mean_KAO,sd_KAO,Mean_AI,sd_AI,Mean_Diff,Mean_Diff_Percentage,
                                         sd_Diff,sd_Diff_Percentage,se_Diff,se_Diff_Percentage,min_Diff,
                                         min_Diff_Percentage,max_Diff,max_Diff_Percentage,median,Mean_ABsDiff,
                                         Mean_ABsDiff_Percentage,sd_ABsDiff,sd_ABsDiff_Percentage,se_ABsDiff,
                                         se_ABsDiff_Percentage,min_ABsDiff,min_ABsDiff_Percentage,max_ABsDiff,
                                         max_ABsDiff_Percentage,icc,p_value,negative_log10_p]).T

lh_BA_exvivo_stats.columns = ['Mean_AI_re','sd_AI_re','Mean_AI','sd_AI','Mean_Diff','Mean_Diff_%',
                                    'sd_Diff','sd_Diff_%','se_Diff','se_Diff_%','min_Diff',
                                    'min_Diff_%','max_Diff','max_Diff_%','median','Mean_ABsDiff',
                                    'Mean_ABsDiff_%','sd_ABsDiff','sd_ABsDiff_%','se_ABsDiff',
                                    'se_ABsDiff_%','min_ABsDiff','min_ABsDiff_%','max_ABsDiff',
                                    'max_ABsDiff_%','ICC','p-value','(-)log10(p)']

df_index = []
for i in KAO_part.columns:
    df_index.append(i[: -4])
lh_BA_exvivo_stats.index = df_index
lh_BA_exvivo_stats.index.name = "Structure"
    
lh_BA_exvivo_stats.fillna("NaN", inplace=True)

lh_BA_exvivo_stats.to_csv("AI_RESULT/COMPARISON/comparison_lh.BA_exvivo.stats.csv")

