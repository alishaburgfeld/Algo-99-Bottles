def bottle_song(num):
	count = num
	while count>1:
		print(f"{count} bottles of beer on the wall, {count} bottles of beer. Take one down and pass it around, {count-1} bottles of beer on the wall.")
		count-=1
		if count==2:
			print(f"{count} bottles of beer on the wall, {count} bottles of beer. Take one down and pass it around, ${count-1} bottle of beer on the wall.")
			count-=1
	print(f"{count} bottle of beer on the wall, {count} bottle of beer. Take one down and pass it around, no more bottles of beer on the wall. No more bottles of beer on the wall. No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, {num} bottles of beer on the wall.")

bottle_song(99)
