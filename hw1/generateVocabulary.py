unique_terms = set()

with open('paper.txt', 'r', encoding='utf-8') as paper_file:
    for line in paper_file:
        # Split the line into PaperID and terms
        parts = line.strip().split('\t')
        if len(parts) == 2:
            terms = parts[1].split()
            for term in terms:
                unique_terms.add(term)

# Step 2: Write the unique terms to 'vocab.txt'
with open('vocab.txt', 'w', encoding='utf-8') as vocab_file:
    for term in unique_terms:
        vocab_file.write(term + '\n')
