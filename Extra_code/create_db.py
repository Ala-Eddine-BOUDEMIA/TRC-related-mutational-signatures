import gffutils

db = gffutils.create_db(
	"Annotations/gencode-v39-annotation.gff3", 
	dbfn='gencode_grch38.db', force=True, 
	keep_order=True, merge_strategy='merge', 
	sort_attribute_values=True)