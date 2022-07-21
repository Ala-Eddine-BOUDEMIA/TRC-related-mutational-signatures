import pandas as pd
import Tools

region = "tss"
E2 = "E2-2h"
Tools.create_folder("MCF7_DRIP_Profiles/" + region.upper() + "/" + E2 + "/")

file_names = ["only_" + region + "_mutations", "active_" + region + "_mutations", 
	"inactive_" + region + "_mutations", "active_" + region + "_only_mutations", 
	"inactive_" + region + "_only_mutations", "all_" + region + "_mutations", 
	"drip_mutations", "active_" + region + "_drip_mutations", "inactive_" + region + "_drip_mutations"]

for f in file_names:

	file = pd.read_csv("Annotations/MCF7/" + region.upper() + "/" + E2 + "/" + f + ".tsv", sep="\t")
	file = file[["Chr", "Start", "End", "Mutation"]]
	file["Start_Position"] = file["Mutation"] - 5
	file["End_Position"] = file["Mutation"] + 5
	file["Count"] = 1
	factor = len(file.drop_duplicates(subset=["Chr", "Start", "End"]))
	file["Count"] = file["Count"] / factor
	file.pop("Start")
	file.pop("End")
	file.pop("Mutation")

	file = file.sort_values(["Chr", "Start_Position"])
	file.to_csv("MCF7_DRIP_Profiles/" + region.upper() + "/" + E2 + "/" + f + ".bedGraph", 
		sep="\t", index=False, header=None)