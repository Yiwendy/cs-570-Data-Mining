
unique_terms = set()

with open('paper.txt', 'r', encoding='utf-8') as paper_file:
    for line in paper_file:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            terms = parts[1].split()
            for term in terms:
                unique_terms.add(term)

term_to_index = {term: index for index, term in enumerate(sorted(unique_terms))}

with open('title.txt', 'w', encoding='utf-8') as title_file:
    with open('paper.txt', 'r', encoding='utf-8') as paper_file:
        for line in paper_file:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                terms = parts[1].split()
                term_count = {}
                for term in terms:
                    if term in term_count:
                        term_count[term] += 1
                    else:
                        term_count[term] = 1

                title_file.write(f"{len(terms)}")
                for term, count in term_count.items():
                    term_index = term_to_index[term]
                    title_file.write(f" {term_index}:{count}")
                title_file.write('\n')