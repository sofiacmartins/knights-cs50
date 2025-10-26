# Feature: Estatísticas de Puzzles

## Descrição
Esta feature adiciona capacidade de calcular e visualizar estatísticas sobre as soluções dos puzzles Knights and Knaves.

## Motivação
Durante o desenvolvimento, foi útil ter uma visão rápida sobre:
- Quantas personagens existem em cada puzzle
- Quantos knights vs knaves em cada solução
- Ratio entre knights e knaves

Estas estatísticas ajudam a validar rapidamente se as soluções fazem sentido e a identificar padrões nos puzzles.

## Funcionalidades Implementadas

### 1. Função `puzzle_statistics(knowledge, symbols)`
Calcula estatísticas sobre um puzzle resolvido:
- **Input**: Knowledge base e lista de símbolos
- **Output**: Dicionário com:
  - `total_characters`: número total de personagens
  - `knights`: número de knights
  - `knaves`: número de knaves
  - `solved_characters`: lista de personagens e seus tipos

### 2. Função `print_statistics(puzzle_name, stats)`
Visualiza as estatísticas de forma legível:
- Formatação clara com emojis
- Cálculo automático do ratio knight/knave
- Layout consistente

### 3. Interface melhorada do `main()`
- Header e footer visuais
- Estatísticas após cada solução
- Separação clara entre puzzles

## Uso de IA no Desenvolvimento

### Ferramenta: Claude (Anthropic) - Sonnet 4.5

#### Prompt 1: Concepção da Feature
**Input**:
> "Quero adicionar uma feature simples ao projeto Knights. Sugere algo útil que mostre informação adicional sobre os puzzles resolvidos."

**Output**:
```
Sugestões de features:
1. Estatísticas (quantos knights/knaves)
2. Tempo de resolução
3. Complexidade do puzzle
4. Exportar para JSON

Recomendo a #1 (estatísticas) porque:
- Simples de implementar
- Útil para validação
- Não requer bibliotecas externas
- Boa demonstração de processamento de resultados
```

#### Prompt 2: Implementação
**Input**:
> "Como implemento uma função que conta quantos knights e knaves existem na solução de um puzzle?"

**Output da IA**:
```python
def puzzle_statistics(knowledge, symbols):
    stats = {"knights": 0, "knaves": 0}
    
    for symbol in symbols:
        if model_check(knowledge, symbol):
            if "Knight" in str(symbol):
                stats["knights"] += 1
            elif "Knave" in str(symbol):
                stats["knaves"] += 1
    
    return stats
```

#### Prompt 3: Correção de Bug
**Input**:
> "A contagem de 'total_characters' está errada. Puzzle 1 mostra 1 mas deveria ser 2."

**Output da IA**:
```
O problema é que está a contar apenas knights em total_characters.
Solução: usar um set() para rastrear personagens únicas:

characters_found = set()
# ... adicionar cada personagem ao set
stats["total_characters"] = len(characters_found)

Isso garante que cada personagem (A, B, C) seja contada apenas uma vez.
```

#### Prompt 4: Melhorias Visuais
**Input**:
> "Como posso tornar a saída mais visual e profissional?"

**Output da IA**:
- Adicionar headers com separadores (`=` * 50)
- Usar emoji 📊 para destacar estatísticas
- Calcular ratios para análise comparativa
- Formatação consistente com indentação

## Exemplo de Output

### Antes (versão original):
```
Puzzle 1
    A is a Knave
    B is a Knight
```

### Depois (com feature de estatísticas):
```
==================================================
KNIGHTS AND KNAVES - PUZZLE SOLVER
==================================================

Puzzle 1
    A is a Knave
    B is a Knight

  📊 Statistics for Puzzle 1:
     Total characters: 2
     Knights: 1
     Knaves: 1
     Knight/Knave ratio: 1.00

==================================================
```

## Código Adicionado

### Localização
- **Ficheiro**: `puzzle.py`
- **Linhas adicionadas**: ~60 linhas

### Funções Criadas
1. `puzzle_statistics(knowledge, symbols)` - 25 linhas
2. `print_statistics(puzzle_name, stats)` - 10 linhas
3. `main()` - modificado (+15 linhas)

## Testes e Validação

### Teste Manual
```bash
python puzzle.py
```

### Resultados Validados
- ✅ Puzzle 0: 1 personagem (0 knights, 1 knave)
- ✅ Puzzle 1: 2 personagens (1 knight, 1 knave, ratio 1.00)
- ✅ Puzzle 2: 2 personagens (1 knight, 1 knave, ratio 1.00)
- ✅ Puzzle 3: 3 personagens (2 knights, 1 knave, ratio 2.00)

### Padrões Identificados
Através das estatísticas, podemos observar:
- Puzzles simples (0-1) tendem a ter poucos knights
- Puzzles com declarações conflituantes (2) têm ratio equilibrado
- Puzzles complexos (3) têm mais knights que knaves

## Benefícios

### Para o Utilizador
- **Visão rápida** da composição de cada puzzle
- **Validação visual** das soluções
- **Interface profissional** com formatação clara

### Para o Desenvolvedor
- **Debugging facilitado**: ratios ajudam a identificar padrões
- **Extensibilidade**: fácil adicionar mais métricas
- **Código modular**: funções separadas e reutilizáveis

## Possíveis Extensões Futuras

1. **Gráficos ASCII**: Visualizar ratios em barras
2. **Comparação global**: Estatísticas agregadas de todos os puzzles
3. **Complexidade**: Score baseado em número de declarações e personagens
4. **Export**: Guardar estatísticas em JSON/CSV
5. **Modo verbose**: Mostrar raciocínio passo a passo

## Compatibilidade

- ✅ Python 3.12
- ✅ Não requer bibliotecas adicionais
- ✅ Compatível com check50
- ✅ Não altera a lógica dos puzzles existentes
- ✅ Mantém retrocompatibilidade

## Commits Relacionados
```bash
feat(statistics): adicionar cálculo de estatísticas dos puzzles
feat(statistics): adicionar visualização formatada com emojis
fix(statistics): corrigir contagem de personagens totais
fix(puzzle3): restaurar implementação completa do knowledge3
docs(statistics): adicionar documentação completa da feature
```

## Autor
Sofia Martins  
Desenvolvido com assistência de Claude AI (Anthropic)  
Outubro 2025

## Licença
Parte do projeto Knights - CS50 AI