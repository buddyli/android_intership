

 %for item in data:

 	${ item.name } |
 	${ item.age} |
 	${ item.sex} |
 	%for studio in item.studio:
 		${ studio.name }
 	%endfor
 	<hr>
 %endfor