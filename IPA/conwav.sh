sdir='sounds/vowels/'
cont=$(ls $sdir)
for entity in $cont
do
	lengh=${#entity}
	echo $entity, $lengh, ${entity:0:lengh-4}
	
	output=${entity:0:lengh-4}
	
	echo $output
	ffmpeg -i $sdir$entity $sdir$output.wav 
done


