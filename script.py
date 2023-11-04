import sys

if len(sys.argv) != 2:
    print("Usage: python script.py path_to_fasta_file")
else:
    fasta_path = sys.argv[1]

    match_score=2
    mismatch_penalty=-1
    gap_penalty=-2

    def load_fasta(file_path):
        sequences = []
        with open(file_path, 'r') as file:
            sequence = ''
            for line in file:
                if line.startswith('>'):
                    if sequence:
                        sequences.append(sequence)
                        sequence = ''
                else:
                    sequence += line.strip()
            if sequence:
                sequences.append(sequence)
        return sequences

    def needleman_wunsch(sequence1, sequence2):
        n = len(sequence1)
        m = len(sequence2)

        # Inicialization of the score matrix
        score_matrix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        # Initializing the first row and first column of the score matrix
        for i in range(n + 1):
            score_matrix[i][0] = i * gap_penalty
        for j in range(m + 1):
            score_matrix[0][j] = j * gap_penalty

        # Populating the score matrix according to the Needleman-Wunsch algorithm.
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if sequence1[i - 1] == sequence2[j - 1]:
                    match = score_matrix[i - 1][j - 1] + match_score
                else:
                    match = score_matrix[i - 1][j - 1] + mismatch_penalty
                delete = score_matrix[i - 1][j] + gap_penalty
                insert = score_matrix[i][j - 1] + gap_penalty
                score_matrix[i][j] = max(match, delete, insert)

        # Calculating the path and the optimal alignment - "traceback".
        alignment1, alignment2 = [], []
        i, j = n, m
        while i > 0 and j > 0:
            if score_matrix[i][j] == score_matrix[i - 1][j - 1] + (match_score if sequence1[i - 1] == sequence2[j - 1] else mismatch_penalty):
                alignment1.append(sequence1[i - 1])
                alignment2.append(sequence2[j - 1])
                i -= 1
                j -= 1
            elif score_matrix[i][j] == score_matrix[i - 1][j] + gap_penalty:
                alignment1.append(sequence1[i - 1])
                alignment2.append("-")
                i -= 1
            else:
                alignment1.append("-")
                alignment2.append(sequence2[j - 1])
                j -= 1

        while i > 0:
            alignment1.append(sequence1[i - 1])
            alignment2.append("-")
            i -= 1
        while j > 0:
            alignment1.append("-")
            alignment2.append(sequence2[j - 1])
            j -= 1

        # Reversing the sequence
        alignment1 = ''.join(reversed(alignment1))
        alignment2 = ''.join(reversed(alignment2))

        return alignment1, alignment2

    sequences = load_fasta(fasta_path)
    if len(sequences) != 2:
        print("Fasta file should contain 2 sequneces.")
    else:
        alignment1, alignment2 = needleman_wunsch(sequences[0], sequences[1])

        print("Alignment 1:", alignment1)
        print("Alignment 2:", alignment2)

        final_score = 0

        for char1, char2 in zip(alignment1, alignment2):

            if char1=="-" or char2=="-":
                final_score+=gap_penalty
            elif char1 == char2:
                final_score+=match_score
            else:
                final_score+=mismatch_penalty

        print("Score:", final_score)

    def save_lines_to_file(lines):
        with open("output.txt", 'w') as file:
            file.writelines(lines)

    save_lines_to_file(["Alignment 1: "+ alignment1 +"\n", "Alignment 2: "+alignment2+"\n", str(final_score)+"\n"])

