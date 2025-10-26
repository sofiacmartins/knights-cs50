# Knights and Knaves - CS50 AI Project

## Introdução
Este projeto implementa um sistema de resolução automática de puzzles lógicos "Knights and Knaves" usando lógica proposicional e model checking. 

Os puzzles baseiam-se numa premissa simples: cada personagem é um cavaleiro (knight) que sempre diz a verdade, ou um mentiroso (knave) que sempre mente. O objetivo é determinar, através das declarações das personagens, quem é cavaleiro e quem é mentiroso.

## Descrição do Projeto

O projeto resolve 4 puzzles de complexidade crescente através de bases de conhecimento em lógica proposicional:

### Puzzle 0 - Declaração Auto-Contraditória
- **Personagens**: A
- **Declaração**: A diz "Sou simultaneamente cavaleiro e mentiroso"
- **Lógica implementada**: 
  - Restrições estruturais: A é OU cavaleiro OU mentiroso (mutuamente exclusivos)
  - Bicondicional que liga o tipo de A à veracidade da sua afirmação
- **Solução**: A é mentiroso (pois ninguém pode ser ambos)

### Puzzle 1 - Declaração sobre Ambos
- **Personagens**: A e B
- **Declaração**: A diz "Somos ambos mentirosos", B não diz nada
- **Lógica implementada**: 
  - Restrições estruturais para ambas as personagens
  - Se A fosse cavaleiro, a afirmação seria verdadeira (mas isso criaria contradição)
  - Se A é mentiroso, a afirmação é falsa (logo pelo menos um não é mentiroso)
- **Solução**: A é mentiroso, B é cavaleiro

### Puzzle 2 - Declarações Conflituantes
- **Personagens**: A e B
- **Declarações**: 
  - A diz "Somos do mesmo tipo"
  - B diz "Somos de tipos diferentes"
- **Lógica implementada**: 
  - Duas bicondicionais opostas que forçam uma contradição
  - Se A fala verdade, são iguais; se B fala verdade, são diferentes
  - Apenas uma pode ser verdadeira
- **Solução**: A é mentiroso, B é cavaleiro (as declarações são logicamente opostas)

### Puzzle 3 - Três Personagens com Declarações Indiretas
- **Personagens**: A, B e C
- **Declarações**:
  - A diz "Sou cavaleiro" OU "Sou mentiroso" (não sabemos qual)
  - B diz que A disse "Sou mentiroso"
  - B diz "C é mentiroso"
  - C diz "A é cavaleiro"
- **Lógica implementada**: 
  - A nunca diria "Sou mentiroso" (paradoxo lógico)
  - Logo B está a mentir sobre o que A disse
  - Cadeia de implicações através das três personagens
- **Solução**: A é cavaleiro, B é mentiroso, C é cavaleiro

## Estrutura do Código

### Componentes Principais

Cada knowledge base contém dois tipos de informação:

#### 1. Restrições Estruturais
Define que cada personagem é exclusivamente cavaleiro OU mentiroso:
```python
Or(AKnight, AKnave),      # A é cavaleiro OU mentiroso
Not(And(AKnight, AKnave)) # Mas NÃO ambos simultaneamente
```

#### 2. Bicondicionais Lógicas
Liga o tipo da personagem à veracidade das suas declarações:
```python
# Se A é cavaleiro ↔ a declaração é verdadeira
# Se A é mentiroso ↔ a declaração é falsa
Biconditional(AKnight, declaracao)
```

### Exemplo Completo - Puzzle 1
```python
knowledge1 = And(
    # Restrições estruturais
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    
    # A afirma: "Somos ambos mentirosos"
    # Bicondicional: A é knight ↔ (A é knave E B é knave)
    Biconditional(AKnight, And(AKnave, BKnave))
)
```

**Análise**: 
- Se A fosse knight: `True ↔ (False AND ?)` = contradição!
- Logo A é knave: `False ↔ (True AND ?)` = B tem de ser knight

## Ferramentas de IA Usadas

### Claude (Anthropic) - Sonnet 4.5
**Utilização principal**: Assistente de desenvolvimento e aprendizagem

**Tarefas realizadas**:
- Explicação detalhada da lógica proposicional e operadores (And, Or, Not, Implication, Biconditional)
- Clarificação da diferença entre Implication e Biconditional no contexto deste problema
- Análise de puzzles complexos (especialmente Puzzle 3 com declarações indiretas)
- Estruturação do workflow Git com feature branches
- Orientação sobre conventional commits em português
- Revisão e correção de erros lógicos no código
- Criação desta documentação

### GitHub Copilot
**Utilização secundária**: Autocompletar e sugestões de código

**Tarefas realizadas**:
- Sugestões de sintaxe Python durante escrita
- Autocompletar padrões repetitivos (restrições estruturais)
- Acelerar escrita de expressões lógicas similares

## Exemplos de Prompts e Outputs de IA

### Prompt 1: Compreender Operadores Lógicos
**Input ao Claude**: 
> "Qual a diferença entre usar Implication e Biconditional para representar que um knight diz a verdade?"

**Output da IA**: 
```
Implication (A → B): "Se A então B"
- Implication(AKnight, declaracao): Se A é knight, então declaracao é verdadeira
- Problema: não diz nada sobre quando A é knave

Biconditional (A ↔ B): "A se e somente se B"
- Biconditional(AKnight, declaracao): A é knight ↔ declaracao é verdadeira
- Vantagem: captura ambos os casos:
  * Se A é knight → declaracao é verdadeira
  * Se A é knave → declaracao é falsa
```

**Impacto**: Percebi que Biconditional é mais conciso e captura toda a lógica num só operador.

---

### Prompt 2: Resolver Puzzle 1
**Input ao Claude**: 
> "No Puzzle 1, A diz 'Somos ambos mentirosos'. Como represento isto?"

**Output da IA**:
```python
# A afirma: "We are both knaves"
# Usa Biconditional para ligar o tipo de A à veracidade da afirmação
Biconditional(AKnight, And(AKnave, BKnave))

# Análise:
# Se AKnight for True: True ↔ (False AND BKnave)
# Isto é impossível! Logo A não pode ser knight.

# Se AKnight for False (A é knave): False ↔ (True AND BKnave)  
# Para isso ser consistente: BKnave tem de ser False (B é knight)
```

**Impacto**: Compreendi como o model checker resolve contradições automaticamente.

---

### Prompt 3: Puzzle 3 - Paradoxo Lógico
**Input ao Claude**: 
> "No Puzzle 3, porque é que nenhuma personagem diria 'Sou mentiroso'?"

**Output da IA**:
```
Esta é uma declaração paradoxal conhecida como "Paradoxo do Mentiroso":

Caso 1: A é knight (diz verdade)
- Se A dissesse "Sou mentiroso", estaria a afirmar algo falso
- Mas knights não mentem → Contradição!

Caso 2: A é knave (mente)
- Se A dissesse "Sou mentiroso", estaria a dizer a verdade
- Mas knaves não dizem verdades → Contradição!

Conclusão: NENHUMA personagem (knight ou knave) pode fazer 
esta declaração de forma logicamente consistente.

Logo, no Puzzle 3, quando B diz que "A disse 'Sou mentiroso'", 
B está necessariamente a mentir (é um knave).
```

**Impacto**: Esta explicação foi crucial para resolver o Puzzle 3 corretamente.

---

### Prompt 4: Organização Git
**Input ao Claude**: 
> "Como organizar este projeto com Git usando conventional commits e feature branches?"

**Output da IA**:
```
Estrutura recomendada:

1. Branches:
   - main (branch principal)
   - feature/puzzle-0 (apenas Puzzle 0)
   - feature/puzzle-1 (apenas Puzzle 1)
   - feature/puzzle-2 (apenas Puzzle 2)
   - feature/puzzle-3 (apenas Puzzle 3)
   - feature/documentacao (README)

2. Conventional Commits em PT-PT:
   - feat(puzzle0): implementar lógica...
   - fix(puzzle2): corrigir implicação...
   - docs: adicionar README...
   - test: validar com check50...
   - style: aplicar formatação...

3. Workflow:
   git checkout -b feature/puzzle-X
   # desenvolver
   git commit -m "feat(puzzleX): ..."
   git checkout main
   git merge feature/puzzle-X
   git push
```

**Impacto**: Consegui organizar o projeto de forma profissional e cumprir os requisitos de avaliação.

## Como Executar

### Pré-requisitos
- Python 3.12
- Ficheiros `logic.py` e `puzzle.py` na mesma pasta

### Executar o programa
```bash
python puzzle.py
```

### Resultados Esperados
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

## Testes e Validação

### Verificar correção do código
```bash
check50 ai50/projects/2024/x/knights
```

### Verificar estilo do código
```bash
style50 puzzle.py
```

### Submeter projeto
```bash
submit50 ai50/projects/2024/x/knights
```

## Estrutura do Repositório
```
knights/
├── logic.py          # Classes para lógica proposicional (fornecido)
├── puzzle.py         # Implementação das knowledge bases (desenvolvido)
├── README.md         # Esta documentação
└── .gitignore        # Ficheiros ignorados pelo Git
```

## Tecnologias Utilizadas
- **Python 3.12**: Linguagem de programação
- **Lógica Proposicional**: Representação do conhecimento
- **Model Checking**: Algoritmo de inferência lógica
- **Git & GitHub**: Controlo de versões

## Aprendizagens

### Conceitos Técnicos
1. **Lógica Proposicional**: Como representar conhecimento em símbolos e conectivos lógicos
2. **Model Checking**: Como um algoritmo pode explorar todos os modelos possíveis para encontrar soluções
3. **Bicondicionais**: Representação concisa de "se e somente se" em lógica
4. **Paradoxos Lógicos**: Como declarações auto-referenciadas podem ser inconsistentes

### Boas Práticas
1. **Git Workflow**: Uso de feature branches e conventional commits
2. **Documentação**: Importância de documentar decisões e uso de ferramentas
3. **Decomposição de Problemas**: Resolver puzzles incrementalmente (0→1→2→3)

## Features Adicionais

### 📊 Estatísticas de Puzzles
O programa inclui estatísticas automáticas para cada puzzle resolvido:
- **Total de personagens** no puzzle
- **Contagem separada** de knights e knaves
- **Ratio knight/knave** para análise comparativa
- **Interface visual melhorada** com headers e emojis

Exemplo de output:
```
  📊 Statistics for Puzzle 3:
     Total characters: 3
     Knights: 2
     Knaves: 1
     Knight/Knave ratio: 2.00
```

Para documentação detalhada desta feature, consulta [FEATURE_statistics.md](FEATURE_statistics.md).

## Autor
Sofia Martins - Universidade do Algarve  
CS50's Introduction to Artificial Intelligence with Python - 2024/2025

## Referências
- Smullyan, Raymond (1978). "What is the name of this book?"
- CS50 AI Course Materials
- Documentação Python 3.12
- Claude AI Documentation (Anthropic)

## Licença
Este projeto foi desenvolvido como trabalho académico para o curso CS50 AI.