{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled12.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMSmzyZSufUQsbNYUK5B/Ou",
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
        "<a href=\"https://colab.research.google.com/github/Dakota-Han/NLPstudy/blob/main/tranformer.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LNFS_1mTtki7",
        "outputId": "affb266d-4203-4723-a10f-a99cec131410"
      },
      "source": [
        "!git clone https://github.com/Dakota-Han/NLPstudy.git"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Cloning into 'NLPstudy'...\n",
            "remote: Enumerating objects: 6, done.\u001b[K\n",
            "remote: Counting objects: 100% (6/6), done.\u001b[K\n",
            "remote: Compressing objects: 100% (4/4), done.\u001b[K\n",
            "remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0\u001b[K\n",
            "Unpacking objects: 100% (6/6), done.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PnxprXRHpWSq",
        "outputId": "97162af4-fb2a-4cf0-9e95-ff5f408c97f7"
      },
      "source": [
        "#Blue score calculate library update\n",
        "!pip install torchtext==0.6.0"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: torchtext==0.6.0 in /usr/local/lib/python3.7/dist-packages (0.6.0)\n",
            "Requirement already satisfied: torch in /usr/local/lib/python3.7/dist-packages (from torchtext==0.6.0) (1.8.1+cu101)\n",
            "Requirement already satisfied: sentencepiece in /usr/local/lib/python3.7/dist-packages (from torchtext==0.6.0) (0.1.95)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.7/dist-packages (from torchtext==0.6.0) (4.41.1)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.7/dist-packages (from torchtext==0.6.0) (1.19.5)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.7/dist-packages (from torchtext==0.6.0) (1.15.0)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.7/dist-packages (from torchtext==0.6.0) (2.23.0)\n",
            "Requirement already satisfied: typing-extensions in /usr/local/lib/python3.7/dist-packages (from torch->torchtext==0.6.0) (3.7.4.3)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests->torchtext==0.6.0) (1.24.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests->torchtext==0.6.0) (2020.12.5)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests->torchtext==0.6.0) (2.10)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests->torchtext==0.6.0) (3.0.4)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qge_O6-3rFUV"
      },
      "source": [
        "%%capture\n",
        "!python -m spacy download en\n",
        "!python -m spacy download de"
      ],
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "u5Wi44acp8Ur"
      },
      "source": [
        "import spacy #\n",
        "\n",
        "spacy_en = spacy.load('en')#영어토큰화\n",
        "spacy_de = spacy.load('de')#독일어토큰화"
      ],
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "co8Vw-_VqID-",
        "outputId": "b7f6f498-519f-47dc-c89b-d9fdf3b8b6d6"
      },
      "source": [
        "tokenized = spacy_en.tokenizer(\"I am a graduate student\")\n",
        "\n",
        "for i, token in enumerate(tokenized):\n",
        "  print(f\"인덱스 {i}: {token.text}\")"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "인덱스 0: I\n",
            "인덱스 1: am\n",
            "인덱스 2: a\n",
            "인덱스 3: graduate\n",
            "인덱스 4: student\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7HHlZOhdqYcT",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 133
        },
        "outputId": "9139edba-8607-461f-9820-52639097448d"
      },
      "source": [
        ""
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-19-edf9cb6576cf>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    from\u001b[0m\n\u001b[0m        ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1ZLHeFsMtrQZ"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}