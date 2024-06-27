
# LeetCode Challenge Solutions

Este repositório contém soluções para desafios do LeetCode, organizadas por dificuldade (easy, medium, hard). Cada solução é acompanhada de testes automatizados utilizando `unittest`.

## Estrutura do Projeto

```
leetcode-challenge-solutions/
├── README.md
└── src
    ├── __init__.py
    ├── problems
    │   ├── __init__.py
    │   ├── easy
    │   │   ├── __init__.py
    │   ├── medium
    │   │   └── __init__.py
    │   └── hard
    │       └── __init__.py
    └── tests
        ├── __init__.py
        ├── easy
        │   ├── __init__.py
        ├── medium
        │   └── __init__.py
        └── hard
            └── __init__.py
```

## Requisitos

- Python 3.10 ou superior
- `unittest` (incluído na biblioteca padrão do Python)

## Configuração do Ambiente Virtual

Recomenda-se o uso de um ambiente virtual para isolar as dependências do projeto. Siga os passos abaixo para configurar o ambiente:

1. Crie um ambiente virtual:
    ```bash
    python3 -m venv .venv
    ```

2. Ative o ambiente virtual:
    - No macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```
    - No Windows:
        ```cmd
        .venv\Scripts\activate
        ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Estrutura dos Arquivos

### Problemas

Cada problema está localizado na pasta `src/problems`, organizado por dificuldade (`easy`, `medium`, `hard`). Cada solução está em seu próprio arquivo Python.

#### Exemplo: `merge_sorted_array.py`

```python
# src/problems/easy/merge_sorted_array.py

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """     
        del(nums1[m: (m + n)])              
        nums1 += nums2
        nums1.sort()
```

### Testes

Os testes para cada problema estão localizados na pasta `src/tests`, também organizados por dificuldade (`easy`, `medium`, `hard`). Utilizamos o framework `unittest` para a criação e execução dos testes.

#### Exemplo: `test_merge_sorted_array.py`

```python
# src/tests/easy/test_merge_sorted_array.py

import unittest
from problems.easy.merge_sorted_array import Solution

class TestMergeSortedArray(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_merge_case_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        self.sol.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

if __name__ == "__main__":
    unittest.main()
```

## Executando os Testes

Para rodar todos os testes, use o seguinte comando:

```bash
python3 -m unittest discover -s src/tests -p "test_*.py"
```

Este comando descobre e executa todos os arquivos de teste que seguem o padrão `test_*.py` na pasta `src/tests`.

## Adicionando Novos Problemas

1. Crie um novo diretório para o problema na pasta correspondente à dificuldade (`easy`, `medium`, `hard`).
2. Adicione o arquivo de solução no novo diretório.
3. Crie um arquivo de teste correspondente na pasta `src/tests` com o mesmo padrão de nome.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para novos problemas, melhorias nas soluções existentes ou correções de bugs.