# Howard Chen CSC 427 Report

# PART 1

I cloned the repo Genome Assembly and ran the [main.py](http://main.py) file. The [main.py](http://main.py) function was called 4 times using the unzipped data1, data2, data3, data4 folders. The results were as follows:

| data1 | data2 | data3 | data4 |
| :---- | :---- | :---- | :---- |
| short\_1.fasta 8500 100 short\_2.fasta 8500 100 long.fasta 250 1000 0 15650 1 9997 2 9997 3 9990 4 9990 5 9956 6 9956 7 4615 8 3277 9 828 10 684 11 669 12 669 13 666 14 666 15 655 16 654 17 639 18 639 19 636  | short\_1.fasta 5000 100 short\_2.fasta 5000 100 long.fasta 500 1000 0 15744 1 10013 2 10013 3 9992 4 9992 5 9992 6 5752 7 5171 8 4664 9 3309 10 1009 11 938 12 829 13 733 14 654 15 652 16 652 17 652 18 652 19 652  | short\_1.fasta 2500 100 short\_2.fasta 2500 100 long.fasta 500 1000 0 9824 1 9824 2 9824 3 9824 4 9824 5 9824 6 9824 7 9824 8 3656 9 3656 10 3592 11 3592 12 2604 13 1848 14 1654 15 1517 16 1431 17 1408 18 1352 19 1239  | short\_1.fasta 25000 100 short\_2.fasta 25000 100 long.fasta 5000 1000 0 173867 1 173801 2 159255 3 152869 4 25669 5 21727 6 21727 7 18827 8 18827 9 10981 10 6798 11 6798 12 6467 13 6423 14 5715 15 5715 16 5219 17 5219 18 4798 19 4798  |

The script creates a `DBG` object: `dbg = DBG(k=k, data_list=[short1, short2, long1])`. The script then enters a `for` loop that runs 20 times, which finds the longest contigs. 

# PART 2

Created main.codon, dbg.codon and utils.codon using google gemini. The errors 

(venv) Howards-Air:genome-assembly howardchen$ \~/.codon/bin/codon run \-plugin seq main.codon data1  
utils.codon:6 (15-39): error: cannot import name 'join' from 'os.path'  
├─ utils.codon:15 (14-24): error: during the realization of read\_fasta(path: str, name: str)  
├─ main.codon:13 (29-38): error: during the realization of read\_data(path: str)  
╰─ main.codon:29 (5-9): error: during the realization of main()

were caused by Gemini thinning os.path was a supported library in Codon. Fixed by string concatonation. Overall this was surprisingly easy to do. 

# PART 3

Created [evaluate.py](http://evaluate.py) instead of .sh 

