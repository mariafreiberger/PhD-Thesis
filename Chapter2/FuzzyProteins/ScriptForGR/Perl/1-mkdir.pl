use strict;

open(lista,"/home/maria/Documentos/InterfaceRes/ListaRedundant_Unique");
system("cd /home/maria/Documentos/InterfaceRes/; mkdir VPs");

my $lista=<lista>;
while($lista=<lista>){
	chomp $lista;
	my @splista=split " ",$lista;
	#@spb[0]=lc(@spb[0]);
	system("cd /home/maria/Documentos/InterfaceRes/VPs;mkdir @splista[0]");
}

close(lista);
