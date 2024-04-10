{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/devcardososilva/App-kivy/blob/main/1%20-%20ATIVIDADE%20PYTHON%20-%20Estrutura%20Sequencial.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Atividade 1"
      ],
      "metadata": {
        "id": "Xdafd_VbXr_2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"Hello  world\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EaIf5pCwXwhi",
        "outputId": "2e83a380-7039-4590-862f-4ea7979dc200"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello  world\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Atividade 2"
      ],
      "metadata": {
        "id": "AmeZ6devXC8b"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "numero= int(input(\"Escreva um numero inteiro:  \"))\n",
        "\n",
        "print (numero)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3Cz1V-7IXFjN",
        "outputId": "d102f80c-0109-4a13-ce70-0066137f5213"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hola Escreva um numero inteiro:  1\n",
            "1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Atividade 3"
      ],
      "metadata": {
        "id": "MJy4bOi6Yg65"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "A = float(input(\"Escreva um número: \"))\n",
        "B = float(input(\"Escreva um outro número: \"))\n",
        "\n",
        "print(\"A soma dos números é: \", A + B)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vkvYicEkYa8i",
        "outputId": "77da9e8c-4b77-42d7-f2b6-717b494650a5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Escreva um número: 1\n",
            "Escreva um outro número: 1\n",
            "A soma dos números é:  2.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Atividade 4\n"
      ],
      "metadata": {
        "id": "6N9mRm5yZip_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "A = float(input(\"Digite a primeira nota: \"))\n",
        "B = float(input(\"Digite a segunda nota: \"))\n",
        "C = float(input(\"Digite a terceira nota: \"))\n",
        "D = float(input(\"Digite a quarta nota: \"))\n",
        "\n",
        "E = A + B + C + D\n",
        "\n",
        "print(\"Sua média é: \", E / 4)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kao-IEHcZkG6",
        "outputId": "e526a6de-ba77-4f33-b915-e506fbe26702"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a primeira nota: 7\n",
            "Digite a segunda nota: 7\n",
            "Digite a terceira nota: 7\n",
            "Digite a quarta nota: 7\n",
            "Sua média é:  7.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Atividade 5"
      ],
      "metadata": {
        "id": "vVInUhxea3S7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "A = float(input(\"Digite quantos metros você deseja converter para centímetros: \"))\n",
        "\n",
        "B = A * 100\n",
        "\n",
        "print(\"A conversão em centímetros é: \", B)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "L_2loOkra7cU",
        "outputId": "8f1152a3-fd7b-4f8b-9fa7-da242872851b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite quantos metros você deseja converter para centimetros: 1\n",
            "A conversão em centimetros é:  100.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Atividade 6"
      ],
      "metadata": {
        "id": "bXcQtxt8ddsz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "raio = float(input(\"Digite o raio do criculo: \"))\n",
        "\n",
        "area = 3.14 * raio ** 2\n",
        "\n",
        "print(\"o área do criculo: \", area)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7uSwVzTtdg6f",
        "outputId": "4b444377-e873-4384-fbe0-bafeca6c96b5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o raio do criculo: 3\n",
            "o area do criculo:  28.26\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Atividade 7"
      ],
      "metadata": {
        "id": "PJO2H4heb1EW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "A = float(input(\"Digite o primeiro lado do quadrado: \"))\n",
        "\n",
        "B = A * A\n",
        "\n",
        "print(\"A aréa do quadrado é: \", B)\n",
        "\n",
        "\n",
        "print(\"O dobro da aréa é: \", B * 2)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yl4FOtjhb400",
        "outputId": "b029f403-ab4e-41df-87ab-70917d37e165"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o primeiro lado do quadrado: 2\n",
            "A aréa do quadrado é:  4.0\n",
            "O dobro da aréa é:  8.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Atividade 8\n"
      ],
      "metadata": {
        "id": "Wy1SGTLFguzg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "A = float(input(\"Quanto você ganha por hora: \"))\n",
        "B= float(input(\"Quantas horas você trabalha no mês: \"))\n",
        "\n",
        "C = A * B\n",
        "\n",
        "print(\"Atualmente você ganha\", C, \" No mês\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "M04ctnYCgwzW",
        "outputId": "5c18307c-3125-4b93-dfce-29e721a246f1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Quanto você ganha por hora: 7.50\n",
            "Quantas horas você trabalha no mês: 80\n",
            "Atualmente você ganha 600.0  No mês\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Atividade 9"
      ],
      "metadata": {
        "id": "UqLhG8Xjizoz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "F = float(input(\"Digite a temperatura em graus Fahrenheit: \"))\n",
        "\n",
        "c = 5 * ((F-32) / 9)\n",
        "\n",
        "print(\"A temperatura em graus celsiues é: \", c)"
      ],
      "metadata": {
        "id": "Z_PntVUYi1HR"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Atividade 10"
      ],
      "metadata": {
        "id": "PdUwPUasl7L3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "C = float(input(\"Digite a temperatura em graus celsiues: \"))\n",
        "\n",
        "F = (C * 9/5) + 32\n",
        "\n",
        "print(\"A temperatura em fahrenheit é: \", F)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VasvVnjamOXT",
        "outputId": "69ac0f93-2599-4a16-e846-b5f096579c99"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a temperatura em graus celsiues: 10\n",
            "A temperatura em fahrenheit é:  50.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Atividade 11"
      ],
      "metadata": {
        "id": "5edh7Li7vhnq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "num1 = int(input(\"Digite o primeiro número inteiro: \"))\n",
        "num2 = int(input(\"Digite o segundo número inteiro: \"))\n",
        "num_real = float(input(\"Digite um número real: \"))\n",
        "\n",
        "resultado1 = (2 * num1) * (num2 / 2)\n",
        "resultado2 = (3 * num1) + num_real\n",
        "resultado3 = num_real ** 3\n",
        "\n",
        "print(\"O produto do dobro do primeiro com metade do segundo é:\", resultado1)\n",
        "print(\"A soma do triplo do primeiro com o terceiro é:\", resultado2)\n",
        "print(\"O terceiro elevado ao cubo é:\", resultado3)"
      ],
      "metadata": {
        "id": "KBYLVBefvksw",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ee6beacc-fb5a-4b5f-96a6-9b56faa7ebb0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o primeiro número inteiro: 2\n",
            "Digite o segundo número inteiro: 2\n",
            "Digite um número real: 2\n",
            "O produto do dobro do primeiro com metade do segundo é: 4.0\n",
            "A soma do triplo do primeiro com o terceiro é: 8.0\n",
            "O terceiro elevado ao cubo é: 8.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Atividade 12"
      ],
      "metadata": {
        "id": "0iMH9P4SXo72"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "peso = float(input(\"Digite o peso dos peixes em quilos: \"))\n",
        "excesso = max(0, peso - 50)\n",
        "multa = excesso * 4\n",
        "\n",
        "print(\"Excesso de peso:\", excesso, \"quilos\")\n",
        "print(\"Valor da multa a pagar: R$\", multa)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vq21Qg_1XqRG",
        "outputId": "512ab2fc-295f-4cb0-dea0-511e272ae796"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o peso dos peixes em quilos: 10\n",
            "Excesso de peso: 0 quilos\n",
            "Valor da multa a pagar: R$ 0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Atividade 13\n"
      ],
      "metadata": {
        "id": "mgX_4V47XvOh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "ganhoh = float(input(\"Digite quanto você ganha por hora: \"))\n",
        "horast = float(input(\"Digite o número de horas trabalhadas no mês: \"))\n",
        "\n",
        "salariob = ganhoh * horast\n",
        "\n",
        "ir = salariob * 0.11\n",
        "inss = salariob * 0.08\n",
        "sindicato = salariob * 0.05\n",
        "\n",
        "salariol = salariob - ir - inss - sindicato\n",
        "\n",
        "print(\"Salário Bruto: R$\",  salariob)\n",
        "print(\"Desconto do INSS: R$\", inss)\n",
        "print(\"Desconto do Sindicato: R$\", sindicato)\n",
        "print(\"Salário Líquido: R$\", salariol)"
      ],
      "metadata": {
        "id": "DYgb-C0tXwjB",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f54bfe4c-afcc-454d-bb1a-f90d993bd03f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite quanto você ganha por hora: 1\n",
            "Digite o número de horas trabalhadas no mês: 1\n",
            "Salário Bruto: R$ 1.0\n",
            "Desconto do INSS: R$ 0.08\n",
            "Desconto do Sindicato: R$ 0.05\n",
            "Salário Líquido: R$ 0.76\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Atividade 14"
      ],
      "metadata": {
        "id": "u77vMdR_X0c3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "\n",
        "area = float(input(\"Digite o tamanho da área a ser pintada em metros quadrados: \"))\n",
        "\n",
        "litros_tinta = area / 3\n",
        "quantidade_latas = math.ceil(litros_tinta / 18)\n",
        "preco_total = quantidade_latas * 80\n",
        "\n",
        "print(\"Quantidade de latas de tinta a serem compradas:\", quantidade_latas)\n",
        "print(\"Preço total: R$\", preco_total)\n"
      ],
      "metadata": {
        "id": "wr5lb8gvX12h",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3dd92ef2-7ed8-476d-b0b8-bdfe0e15bf6a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o tamanho da área a ser pintada em metros quadrados: 10\n",
            "Quantidade de latas de tinta a serem compradas: 1\n",
            "Preço total: R$ 80\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Atividade 15"
      ],
      "metadata": {
        "id": "K9ikXkqzX5Yp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "\n",
        "area = float(input(\"Digite o tamanho da área a ser pintada em metros quadrados: \"))\n",
        "\n",
        "litros_tinta = area / 6\n",
        "\n",
        "quantidade_latas = math.ceil((litros_tinta * 1.1) / 18)\n",
        "\n",
        "preco_latas = quantidade_latas * 80\n",
        "\n",
        "quantidade_galoes = math.ceil((litros_tinta * 1.1) / 3.6)\n",
        "\n",
        "preco_galoes = quantidade_galoes * 25\n",
        "\n",
        "quantidade_latas_misturadas = math.floor(litros_tinta / 18)\n",
        "resto = litros_tinta % 18\n",
        "quantidade_galoes_misturados = math.ceil((resto * 1.1) / 3.6)\n",
        "\n",
        "preco_mistura = (quantidade_latas_misturadas * 80) + (quantidade_galoes_misturados * 25)\n",
        "\n",
        "print(\"Quantidade de latas de tinta a serem compradas:\", quantidade_latas)\n",
        "print(\"Preço total para comprar apenas latas: R$\", preco_latas)\n",
        "print(\"Quantidade de galões de tinta a serem comprados:\", quantidade_galoes)\n",
        "print(\"Preço total para comprar apenas galões: R$\", preco_galoes)\n",
        "print(\"Quantidade de latas de tinta na mistura:\", quantidade_latas_misturadas)\n",
        "print(\"Quantidade de galões de tinta na mistura:\", quantidade_galoes_misturados)\n",
        "print(\"Preço total para a mistura de latas e galões: R$\", preco_mistura)\n"
      ],
      "metadata": {
        "id": "Jk5iQfT7X6-Y",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a6b5453a-bbef-42de-a1f9-1beb55a3ac77"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o tamanho da área a ser pintada em metros quadrados: 10\n",
            "Quantidade de latas de tinta a serem compradas: 1\n",
            "Preço total para comprar apenas latas: R$ 80\n",
            "Quantidade de galões de tinta a serem comprados: 1\n",
            "Preço total para comprar apenas galões: R$ 25\n",
            "Quantidade de latas de tinta na mistura: 0\n",
            "Quantidade de galões de tinta na mistura: 1\n",
            "Preço total para a mistura de latas e galões: R$ 25\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Atividade 16"
      ],
      "metadata": {
        "id": "VoSkZQ7nYGYM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "tamanho_mb = float(input(\"Digite o tamanho do arquivo para download (em MB): \"))\n",
        "velocidade_mbps = float(input(\"Digite a velocidade do link de Internet (em Mbps): \"))\n",
        "\n",
        "tamanho_mbps = tamanho_mb * 8\n",
        "\n",
        "tempo = (tamanho_mbps / velocidade_mbps) / 60\n",
        "\n",
        "print(\"Tempo aproximado de download:\", round(tempo, 2), \"minutos\")"
      ],
      "metadata": {
        "id": "iK5ar_XTYI5j",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f75e57bb-10d2-4c9a-bd3f-e18fe149dacd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o tamanho do arquivo para download (em MB): 1\n",
            "Digite a velocidade do link de Internet (em Mbps): 1\n",
            "Tempo aproximado de download: 0.13 minutos\n"
          ]
        }
      ]
    }
  ]
}