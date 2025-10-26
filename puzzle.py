from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Regra estrutural: A é knight OU knave (mutuamente exclusivos)
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # A afirma: "I am both a knight and a knave"
    # Se A é knight (diz verdade), então a afirmação é verdadeira
    # S e A é knave (mente), então a afirmação é falsa
    Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
     # Regra estrutural para A: knight OU knave (mutuamente exclusivos)
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # Regra estrutural para B: knight OU knave (mutuamente exclusivos)
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # A afirma: "We are both knaves"
    # Se A é knight (fala verdade), então ambos são knaves
    # Se A é knave (mente), então a afirmação de que ambos são knaves é falsa
    Biconditional(AKnight, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
