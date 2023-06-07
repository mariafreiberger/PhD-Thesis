use strict;

#/home/maria/@ARGV[1]ChainsGonza/Pdbs_Chain/VirtualParticules/$line/$line.DisEuc
#/home/maria/Desktop/EC_Class/Dimeros/Heterodimeros/EC_1/EC_HETED_1.txt
#/home/maria/Desktop/EC_Class/Dimeros/Homodimeros/EC_4/EC_HOMOD_4.txt

open (DIRE, "/home/maria/Documentos/InterfaceRes/CDRList_F");
open(CNM, ">/home/maria/Documentos/InterfaceRes/NeuMut.txt");
open(MinTM, ">/home/maria/Documentos/InterfaceRes/MinMut.txt");
open(MaxTM, ">/home/maria/Documentos/InterfaceRes/MaxMut.txt");
open(totalM, ">/home/maria/Documentos/InterfaceRes/Mut.txt");

my $d=0;
my $c0=0;
while(my $lista=<DIRE>){
	chomp $lista;
	my @sp=split " ",$lista;
	open(DE,"/home/maria/Documentos/InterfaceRes/VPs/@sp[0]/@sp[0].DistEuM");
	my $cont=0;
	while(my $DE=<DE>){
		chomp $DE;
		$cont++;
		my @splitter= split " ", $DE;
		my $tam=@splitter;
		if($tam<5){}
		else{
		if(@splitter[4]>0.78){	
				print MinTM "@splitter[0] @splitter[1] @splitter[2] @splitter[3] @splitter[4]\n";
				print totalM "@splitter[0] @splitter[1] @splitter[2] @splitter[3] @splitter[4]\n";
			}
		else {
			if(@splitter[4]>-1){	
				print CNM "@splitter[0] @splitter[1] @splitter[2] @splitter[3] @splitter[4]\n";
				print totalM "@splitter[0] @splitter[1] @splitter[2] @splitter[3] @splitter[4]\n";
			}
			else {
				print MaxTM "@splitter[0] @splitter[1] @splitter[2] @splitter[3] @splitter[4]\n";
				print totalM "@splitter[0] @splitter[1] @splitter[2] @splitter[3] @splitter[4]\n";	
				}
			}
		}
	}
	
	close(DE);
}
close(CNM);
close(MaxTM);
close(MinTM);
close(totalM);
close(DIRE);
