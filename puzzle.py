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
     # Regras estruturais: cada personagem é knight OU knave (mutuamente exclusivos)
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # A afirma: "We are the same kind"
    # Se A é knight (verdade), então A e B são do mesmo tipo (ambos knights ou ambos knaves)
    # Se A é knave (mentira), então NÃO são do mesmo tipo
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),

    # B afirma: "We are of different kinds"
    # Se B é knight (verdade), então A e B são de tipos diferentes
    # Se B é knave (mentira), então NÃO são de tipos diferentes
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight)))

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
     # Regras estruturais: cada personagem é knight OU knave (mutuamente exclusivos)
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # O que A disse: pode ser "I am a knight" ou "I am a knave"
    # Se A é knight, a frase dele (seja qual for) é verdadeira
    # Se A é knave, a frase dele (seja qual for) é falsa
    # A só pode ter dito "I am a Knave" (porque seria mentira se for knave, e um knight nunca diria isso)
    Biconditional(AKnight, Or(AKnight, AKnave)),

    # B afirma: "A said 'I am a knave'"
    # Se B é knight (fala verdade), então A realmente disse isso, logo A é knave
    # Se B é knave (mente), então A NÃO disse isso, logo A é knight
    Biconditional(BKnight, AKnave),
    
    # B afirma: "C is a knave"
    # Se B é knight (verdade), então C é knave
    # Se B é knave (mentira), então C é knight
    Biconditional(BKnight, CKnave),
    
    # C afirma: "A is a knight"
    # Se C é knight (verdade), então A é knight
    # Se C é knave (mentira), então A é knave
    Biconditional(CKnight, AKnight)

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
