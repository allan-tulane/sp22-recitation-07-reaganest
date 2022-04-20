# CMPS 2200 Recitation 7
## Answers

**Name:** Reagan Esteves and Chenyu Zhao

Place all written answers from `recitation-07.md` here for easier grading.

- **d.** Do you see a consistent trend? If so, what is it?

|File        | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length|
|------------|---------------------|----------------|-------------------------|
|f1.txt      |         1340        |       826      |       0.616417910       |
|alice29.txt |        1039367      |      676374    |       0.650755700       |
|asyoulik.txt|        876253       |      606448    |       0.692092352       |
|grammar.lsp |         26047       |      17356     |       0.666333935       |
|fields.c    |         78050       |      56206     |       0.720128123       |

Based on the table, there is an consitent trend. The trend is the huffman coding is always less than fixed-length coding which means huffman coding. Moreover, the huffman vs fixed-length values are all shows that the huffman coding is about 2/3 the size of the fixed-length coding.

- **e.**

If every character had the same frequency, expected cost of the huffman encoding for the document would be the same.Moreover, the cost of the huffman coding would also be about the same as the fixed length coding in that specific scenario. The cost of the document is based on the frequency of every letter. Therefore, it is consistent across all the documents if each character in all the documents had the same frequency.



