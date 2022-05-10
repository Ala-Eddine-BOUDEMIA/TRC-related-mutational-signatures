import pandas as pd 
import numpy as np

import Config 

cancer = Config.args.cancer_type

if Config.args.is_active == "True":
    state = "active"
elif Config.args.is_active == "False" :
    state = "inactive"

if Config.args.is_cancer_specific == "False":
    state = "6kb"

def cos_sim(a, b):
      
    """
    Taken from SigProfilerExtractor source code: https://github.com/AlexandrovLab/SigProfilerExtractor/blob/master/SigProfilerExtractor/subroutines.py
    Takes 2 vectors a, b and returns the cosine similarity according 
    to the definition of the dot product
    
    Dependencies: 
    *Requires numpy library. 
    *Does not require any custom function 
    
    Required by:
    * pairwise_cluster_raw
    """

    if np.sum(a)==0 or np.sum(b) == 0:
        return 0.0      
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)

if __name__ == '__main__':
    
    tss = pd.read_csv("Mutational_Signatures/" + cancer +"/TSS/" + state + "/SBS96/Suggested_Solution/SBS96_De-Novo_Solution/Signatures/SBS96_De-Novo_Signatures.txt", sep = "\t")
    tts = pd.read_csv("Mutational_Signatures/" + cancer +"/TTS/" + state + "/SBS96/Suggested_Solution/SBS96_De-Novo_Solution/Signatures/SBS96_De-Novo_Signatures.txt", sep = "\t")

    tss_sig = tss["SBS96B"]
    tts_sig = tts["SBS96A"]

    print("Cosine Similarity between the two signatures is: ", round(cos_sim(tss_sig, tts_sig), 3))
