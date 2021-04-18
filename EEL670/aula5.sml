fun ord (a:real,b:real,c:real) = 
	if a > b andalso a > c
	then 
		if b > c
		then [c,b,a]
		else ord(a,c,b)
	else 
		if b > c
		then ord (b,a,c)
		else ord(c,a,b)
;
