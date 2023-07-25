use strict;

open(lista,"/home/maria/Documentos/InterfaceRes/Fuzzy_NR");
#P07674 253 293 1R71_D

while(my $lista=<lista>){
	chomp $lista;
	my @sp=split " ",$lista;
	my @spchain= split "_",@sp[0];
	my @spres=split ";",@sp[1];
	#@spb[0]=lc(@spb[0]);
	open(res,">>/home/maria/Documentos/InterfaceRes/VPs/@spchain[0]/@spchain[0].ResPos");
	my $d=@spres;
	my $c=0;
	while($c<$d){
		print res "@spres[$c] @spchain[1]\n";
		$c++;
	}
}	
close(lista);
