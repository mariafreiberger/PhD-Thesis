use strict;
#obtiene las coordenadas de todos los residuos del pbd 17 18 19

open (DIRE, "/home/maria/Documentos/InterfaceRes/ListaRedundant_Unique");
my $pdbid;
my $lista=<DIRE>;

while($lista=<DIRE>){
	chomp $lista;
	my @sp=split " ",$lista; 
	open (pdb,"/home/maria/Documentos/InterfaceRes/@sp[0].pdb.done/@sp[0].pdb");
	open (guarda, ">/home/maria/Documentos/InterfaceRes/VPs/@sp[0]/@sp[0].coord");
	while(my $pdb=<pdb>){
		chomp $pdb;
		my @splitter2= split "", $pdb;
		my $atom="@splitter2[0]@splitter2[1]@splitter2[2]@splitter2[3]";
		my $ca="@splitter2[13]@splitter2[14]";
		if (($atom eq "ATOM") and ($ca eq "CA")){
			my $res="@splitter2[22]@splitter2[23]@splitter2[24]@splitter2[25]";
			my $x="@splitter2[26]@splitter2[27]@splitter2[28]@splitter2[29]@splitter2[30]@splitter2[31]@splitter2[32]@splitter2[33]@splitter2[34]@splitter2[35]@splitter2[36]@splitter2[37]";
			my $y="@splitter2[38]@splitter2[39]@splitter2[40]@splitter2[41]@splitter2[42]@splitter2[43]@splitter2[44]@splitter2[45]";
			my $z="@splitter2[46]@splitter2[47]@splitter2[48]@splitter2[49]@splitter2[50]@splitter2[51]@splitter2[52]@splitter2[53]";
			$res =~ s/^\s+//;
			$x =~ s/^\s+//;
			$y =~ s/^\s+//;
			$z =~ s/^\s+//;
			print guarda "$res @splitter2[21] @splitter2[17]@splitter2[18]@splitter2[19] $x $y $z\n";
			}
		}
		close(pdb);
		close(guarda);	
	}
close(DIRE);
