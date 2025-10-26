# Knights and Knaves - CS50 AI Project

## Introdução
Este projeto implementa um sistema de resolução automática de puzzles lógicos "Knights and Knaves" usando lógica proposicional e model checking. 

Os puzzles baseiam-se numa premissa simples: cada personagem é um cavaleiro (que sempre diz a verdade) ou um mentiroso (que sempre mente). O objetivo é determinar, através das declarações das personagens, quem é cavaleiro e quem é mentiroso.

## Descrição do Projeto

O projeto resolve 4 puzzles de complexidade crescente:

### Puzzle 0 - Uma Personagem
- **Personagens**: A
- **Declaração**: A diz "Sou cavaleiro e mentiroso"
- **Solução**: A é mentiroso (pois ninguém pode ser ambos)

### Puzzle 1 - Declaração sobre Ambos
- **Personagens**: A e B
- **Declaração**: A diz "Somos ambos mentirosos"
- **Solução**: A contradiz-se (cavaleiro não diria isso), logo A é mentiroso e B é cavaleiro

### Puzzle 2 - Declarações Conflituantes
- **Personagens**: A e B
- **Declarações**: 
  - A diz "Somos do mesmo tipo"
  - B diz "Somos de tipos diferentes"
- **Solução**: As declarações são opostas, revelando quem mente

### Puzzle 3 - Três Personagens com Interdependência
- **Personagens**: A, B e C
- **Declarações**:
  - B diz que A disse "Sou mentiroso"
  - B diz "C é mentiroso"
  - C diz "A é cavaleiro"
- **Solução**: Análise complexa de declarações indiretas

## Estrutura do Código

Cada knowledge base (`knowledge0`, `knowledge1`, `knowledge2`, `knowledge3`) codifica dois tipos de informação:

1. **Restrições Estruturais**: Cada personagem é exclusivamente cavaleiro OU mentiroso
```python
   Or(AKnight, AKnave),
   Not(And(AKnight, AKnave))
```

2. **Implicações Lógicas**: As declarações são verdadeiras se ditas por cavaleiros, falsas se ditas por mentirosos
```python
   Implication(AKnight, declaracao),
   Implication(AKnave, Not(declaracao))
```

## Ferramentas de IA Usadas

### Claude (Anthropic)
Utilizado para:
- Compreensão da lógica proposicional e sintaxe das expressões lógicas
- Estruturação das knowledge bases para cada puzzle
- Debugging de implicações lógicas complexas (especialmente Puzzle 3)
- Organização do workflow Git com branches e conventional commits
- Criação desta documentação

### GitHub Copilot
Utilizado para:
- Sugestões de sintaxe Python durante a escrita do código
- Autocompletar expressões lógicas repetitivas
- Acelerar a escrita de padrões similares entre puzzles

## Exemplos de Prompts e Outputs

### Prompt 1: Estrutura Base
**Input ao Claude**: 
> "Como representar em lógica proposicional que uma personagem é exclusivamente cavaleiro OU mentiroso?"

**Output da IA**: 
```python
Or(AKnight, AKnave),      # A é cavaleiro OU mentiroso
Not(And(AKnight, AKnave)) # Mas NÃO ambos simultaneamente
```
Esta representação usa XOR (ou exclusivo) através da combinação de OR e NOT(AND).

### Prompt 2: Implicações de Declarações
**Input ao Claude**: 
> "Se A diz 'Somos ambos mentirosos', como codifico isto considerando que A pode ser cavaleiro ou mentiroso?"

**Output da IA**: 
- Se A é cavaleiro (diz verdade): `Implication(AKnight, And(AKnave, BKnave))`
  - A declaração "somos ambos mentirosos" seria verdadeira
- Se A é mentiroso (diz mentira): `Implication(AKnave, Not(And(AKnave, BKnave)))`
  - A declaração seria falsa (pelo menos um não é mentiroso)

### Prompt 3: Paradoxos Lógicos
**Input ao Claude**: 
> "No Puzzle 3, porque é que 'A nunca diria que é mentiroso'?"

**Output da IA**: 
Esta é uma declaração paradoxal:
- Se A fosse cavaleiro e dissesse "Sou mentiroso", estaria a mentir → Impossível (cavaleiros não mentem)
- Se A fosse mentiroso e dissesse "Sou mentiroso", estaria a dizer a verdade → Impossível (mentirosos não dizem verdades)
- Logo, nenhuma personagem (cavaleiro ou mentiroso) pode fazer esta declaração consistentemente

### Prompt 4: Organização Git
**Input ao Claude**: 
> "Como organizar os commits deste projeto usando conventional commits e feature branches?"

**Output da IA**: 
Sugeriu a estrutura:
- `feature/puzzle-0`, `feature/puzzle-1`, etc. para cada puzzle
- Conventional commits: `feat(puzzle0):`, `docs:`, `test:`, etc.
- Workflow: criar branch → commits → merge na main → push

## Como Executar

### Executar o programa:
```bash
python puzzle.py
```

### Executar testes:
```bash
check50 ai50/projects/2024/x/knights
```

### Verificar estilo:
```bash
style50 puzzle.py
```

## Resultados Esperados

Ao executar `python puzzle.py`, deverá ver:
```
Puzzle 0
    A is a Knave
Puzzle 1
    A is a Knave
    B is a Knight
Puzzle 2
    A is a Knave
    B is a Knight
Puzzle 3
    A is a Knight
    B is a Knave
    C is a Knight
```

## Tecnologias Utilizadas
- Python 3.12
- Lógica Proposicional
- Model Checking Algorithm
- Git & GitHub para controlo de versões

## Autor
Sofia Martins - CS50 AI 2024/2025

## Licença
Este projeto foi desenvolvido como parte do curso CS50's Introduction to Artificial Intelligence with Python.