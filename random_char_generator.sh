tenrandomchars() {
	< /dev/urandom tr -dc A-Za-z0-9 | head -c10;
	echo;
}
outfile=$(date +%s)_randchars.out

for i in {0..1000000}; do
	tenrandomchars >>$outfile
done

