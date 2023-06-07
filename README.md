# PhD-Thesis
In this repository you will find all the data and algorithms used in my PhD thesis.

To download the ANK.sql database, please click here:


Abstract:

Proteins are key macromolecules that modulate all processes occurring in living organisms. The diversity of these polymers is determined by variations in amino acid sequences, which influence the formation of three-dimensional structures, dynamics, and function.

In this thesis work, we designed, developed, implemented, and applied bioinformatics tools for protein studies. Our main focus was on repetitive proteins, specifically those containing ankyrin repeat motifs, which are among the most abundant repetitive proteins. We also studied different types and families of proteins, such as proteins containing fuzzy regions and evolutionarily related protein families like hemoglobin and bacterial elongation factor.

The bioinformatics tools we developed are based on the "Principle of Minimal Frustration," which states that proteins fold by minimizing their energy conflicts. However, this principle does not allow for remaining conflicts in the protein structure. It has been shown that these conflicts are related to certain functional aspects of proteins, such as protein-protein binding sites, allosteric sites, and catalytic sites.

We added new functionalities based on the concepts of "local frustration" and implemented a package called "FrustratometeR" in R. This algorithm calculates local frustration in proteins. Additionally, we developed two new tools. One is called "FrustraEvo," which calculates the conservation degree of local frustration in a set of protein structures belonging to the same protein family. The other tool is called "FrustraPocket," which uses a simple machine learning algorithm to predict protein-ligand binding sites. These tools allowed us to study and characterize the frustration patterns of fuzzy regions and protein-ligand binding sites, which are enriched with highly frustrated interactions. We were able to identify residues involved in the conformational change from the non-activated state to the activated state in the bacterial elongation factor. We also studied energy patterns based on the conservation of frustration levels in the hemoglobin family (α and β subunits) and related conserved and highly frustrated residues to functional residues. Finally, we evaluated the "FrustraPocket" model as a predictor of binding sites and obtained an area under the ROC curve of 0.7.

Furthermore, we characterized the exon-intron structure of the ankyrin family (ANK), finding that the most frequent exon length is 99 nt, coinciding with the size of ankyrin repeats, and that most exons are of symmetric class, indicating potential alternative splicing events. We studied possible evolutionary mechanisms acting on these proteins, such as duplication events, exon shuffling, and alternative splicing events. We discovered that these mechanisms do play a role in these proteins, but we could not detect clear and recurrent patterns of specific occurrences. We also characterized the distribution of ankyrin repeats in exons and found that many repeats are encoded by more than one exon.

Finally, we studied the folding dynamics of proteins with ankyrin repeats using a coarse-grained molecular dynamics model (AWSEM). We characterized the folding of several ankyrin family proteins of different lengths and evaluated the performance and robustness of the AWSEM force field in predicting the change in folding free energy due to point mutations. The results showed good performance of the force field in predicting the structures of proteins with a few ankyrin repeats (between 3 and 6). However, AWSEM was not a good force field for predicting the effect of point mutations on the change in free energy in these proteins.

These results provide new tools and methodologies for the study of structural biology by applying the concept of local frustration. Additionally, we were able to characterize and predict functional sites in proteins, discover limitations related to stability and function, and identify differential frustration patterns in families with a common ancestry.
