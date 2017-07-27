from collections import namedtuple

unique_identifiers = ['name', 'abbreviation', 'letter']
Aminoacid = namedtuple('Aminoacid', unique_identifiers +
            ['mass', 'side_chain_class',
             'side_chain_polarity', 'side_chain_charge'])


amino_acids = [
    Aminoacid("Alanine", "Ala", "A", 89.094, "aliphatic", "nonpolar", "neutral"),
    Aminoacid("Arginine", "Arg", "R", 174.203, "basic", "basic polar", "positive"),
    Aminoacid("Asparagine", "Asn", "N", 132.119, "amide", "polar", "neutral"),
    Aminoacid("Aspartic Acid", "Asp", "D", 133.104, "acid", "acidic polar", "negative"),
    Aminoacid("Cysteine", "Cys", "C", 121.154, "sulfur-containing", "nonpolar", "neutral"),
    Aminoacid("Glutatmic Acid", "Glu", "E", 147.131, "acid", "acidic polar", "negative"),
    Aminoacid("Glutamine", "Gln", "Q", 146.146, "amide", "polar", "neutral"),
    Aminoacid("Glycine", "Gly", "G", 75.067, "aliphatic", "nonpolar", "neutral"),
    Aminoacid("Histidine", "His", "H", 155.156, "basic aromatic", "basic polar", "positive 0.1/neutral 0.9"),
    Aminoacid("Isoleucine", "Ile", "I", 131.175, "aliphatic", "nonpolar", "neutral"),
    Aminoacid("Leucine", "Leu", "L", 131.175, "aliphatic", "nonpolar", "neutral"),
    Aminoacid("Lysine", "Lys", "K", 146.189, "basic", "basic polar", "positive"),
    Aminoacid("Methionine", "Met", "M", 149.208, "sulfur-containing", "nonpolar", "neutral"),
    Aminoacid("Phenylalanine", "Phe", "F", 165.192, "aromatic", "nonpolar", "neutral"),
    Aminoacid("Proline", "Pro", "P", 115.132, "cyclic", "nonpolar", "neutral"),
    Aminoacid("Serine", "Ser", "S", 105.093, "hydroxyl-containing", "polar", "neutral"),
    Aminoacid("Threonine", "Thr", "T", 119.119, "hydroxyl-containing", "polar", "neutral"),
    Aminoacid("Tryptophan", "Trp", "W", 204.228, "aromatic", "nonpolar", "neutral"),
    Aminoacid("Tyrosine", "Tyr", "Y", 181.191, "aromatic", "polar", "neutral"),
    Aminoacid("Valine", "Val", "V", 117.148, "aliphatic", "nonpolar", "neutral"),
]


data = unique_identifiers, amino_acids
