def main():
	fw = open("Summing.txt",'w')
	fw2014 = open("Summing2014.txt",'w')
	fwpok = open("SummingPOK.txt",'w')
	ftime = open("../../Data Processing/Report/articleTime.csv",'r')
	fword = open("pok",'r')
	times = []
	for line in ftime:
		times.append(line.split(',')[1][0])
	ftime.close()
	wordExistsDocs = []
	for line in fword:
		wordExistsDocs.append(int(line.split(':')[0]))
	fword.close()
	stopwords = ("little","caused","held","ends","police","work","way","care","city","gastech","pok","abila","elodis","kronos","end","time","pm","am","ii","january","ago","today","and","or","one","today","day","man","bring","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the","happen","chance","chances","people","like","good","bad","new","old","news","year","years",);
	for i in range(0,845):
		fr = open("./articles/"+str(i)+".txt",'r')
		for line in fr:
			line= line.replace('"',' ')
			line= line.replace("'",' ')
			line= line.replace(',',' ')
			line= line.replace('.',' ')
			line= line.replace(':',' ')
			line= line.replace(';',' ')
			line= line.replace('=',' ')
			line= line.replace('?',' ')	
			line= line.replace('~',' ')
			line= line.replace('`',' ')
			line= line.replace('_',' ')
			line= line.replace('+',' ')
			line= line.replace('-',' ')
			line= line.replace('*',' ')
			line= line.replace('@',' ')
			line= line.replace('$',' ')
			line= line.replace('#',' ')
			line= line.replace('%',' ')
			line= line.replace('^',' ')
			line= line.replace('&',' ')
			line= line.replace('|',' ')
			line= line.replace('!',' ')
			line= line.replace('/',' ')
			line= line.replace('\\',' ')
			line= line.replace('(',' ')
			line= line.replace(')',' ')
			line= line.replace(']',' ')
			line= line.replace('[',' ')
			line= line.replace('}',' ')
			line= line.replace('{',' ')
			line= line.replace('<',' ')
			line= line.replace('>',' ')
			line= line.replace('0',' ')
			line= line.replace('1',' ')
			line= line.replace('2',' ')
			line= line.replace('3',' ')
			line= line.replace('4',' ')
			line= line.replace('5',' ')
			line= line.replace('6',' ')
			line= line.replace('7',' ')
			line= line.replace('8',' ')
			line= line.replace('9',' ')
			line= line.split()
			for word in line:
				if word.lower() not in stopwords:
					fw.write(word+' ')
					if times[i]=='2':
						fw2014.write(word+' ')
					if i in wordExistsDocs:
						fwpok.write(word+' ')
		fr.close()
	fw.close()
	fw2014.close()
	fwpok.close()

if __name__ == '__main__':
	main()