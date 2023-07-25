use strict;
open(lista, "/home/maria/Documentos/InterfaceRes/Fuzzy_NR");
my $DistEu;
my $l;
my $lista=<lista>;
while($lista=<lista>){
	chomp $lista;
	my @sp=split " ",$lista;
	my @spchain= split "_",@sp[0];
	open(guarda,">/home/maria/Documentos/InterfaceRes/VPs/@spchain[0]/@spchain[0].DistEuM");
	open(CR,"/home/maria/Documentos/InterfaceRes/VPs/@spchain[0]/@spchain[0].ResF");
	while(my $lineaCR=<CR>){
		chomp $lineaCR;
		my @splitterCR= split " ", $lineaCR;
		open(coordVP,"/home/maria/Documentos/InterfaceRes/VPs/@spchain[0]/@spchain[0].vpM");
		while(my $lineaVP=<coordVP>){
			chomp $lineaVP;
			my @spliterVP= split " ", $lineaVP;
			$DistEu=sqrt((@spliterVP[4]-@splitterCR[3])*(@spliterVP[4]-@splitterCR[3])+(@spliterVP[5]-@splitterCR[4])*(@spliterVP[5]-@splitterCR[4])+(@spliterVP[6]-@splitterCR[5])*(@spliterVP[6]-@splitterCR[5]));
			print guarda "@splitterCR[0] @spliterVP[0] @spliterVP[1] ";
			printf guarda ("%.3f", $DistEu);
			print guarda " @spliterVP[7]\n";
				}
		close(coordVP);
	}
	close(CR);
}
close(lista);
