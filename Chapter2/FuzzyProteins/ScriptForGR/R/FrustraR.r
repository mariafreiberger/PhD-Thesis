library(frustratometeR)

PdbsDir <- "/Fuzzy/"
ResultsDir <- "/Fuzzy/"

# Calculate frustration of Pdbs contained in PdbDir
dir_frustration(PdbsDir = PdbsDir, Mode = "configurational", ResultsDir = ResultsDir)
dir_frustration(PdbsDir = PdbsDir, Mode = "mutational", ResultsDir = ResultsDir)
dir_frustration(PdbsDir = PdbsDir, Mode = "singleresidue", ResultsDir = ResultsDir)
