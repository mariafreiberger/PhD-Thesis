use strict;
#Crea las VP

open (DIRE, "/home/maria/Documentos/InterfaceRes/ListaRedundant_Unique");
my $pdbid;
my $R1X;
my $R1Y;
my $R1Z;
my $R2X;
my $R2Y;
my $R2Z;
my $X;
my $Y; 
my $Z;
my $lista=<DIRE>;

while($lista=<DIRE>){
	chomp $lista;
	my @sp=split " ",$lista;
	my @spb=split "_",@sp[0];
	open(guarda,">/home/maria/Documentos/InterfaceRes/VPs/@sp[0]/@sp[0].vpM");
	open(frst,"/home/maria/Documentos/InterfaceRes/@sp[0].pdb.done/FrustrationData/@sp[0].pdb_mutational");
	my $frst=<frst>;
	while($frst=<frst>){
		chomp $frst;
		my @splitfrst= split " ", $frst;
		open(coord,"/home/maria/Documentos/InterfaceRes/VPs/@sp[0]/@sp[0].coord");
		#print "aaaaaaaaa";
		while(my $coord=<coord>){ 
			chomp $coord;
			my @splitcoord= split " ", $coord;
			if(@splitfrst[0]==@splitcoord[0]){
				$R1X=@splitcoord[3];
				$R1Y=@splitcoord[4];
				$R1Z=@splitcoord[5];
				}
			if(@splitfrst[1]==@splitcoord[0]){
				$R2X=@splitcoord[3];
				$R2Y=@splitcoord[4];
				$R2Z=@splitcoord[5];	
				$X=($R1X+$R2X)/2;
				$Y=($R1Y+$R2Y)/2;
				$Z=($R1Z+$R2Z)/2;
				print guarda "@splitfrst[0] @splitfrst[1] @splitfrst[2] @splitfrst[3] ";
				printf guarda ("%.3f", $X); 
				print guarda " ";
				printf guarda ("%.3f", $Y);
				print guarda " ";
				printf guarda ("%.3f", $Z);
				print guarda " @splitfrst[11]\n";
				last;
			}

		}
	close (coord);

}
	close(guarda);
	close(frst);
}
close(DIRE);


