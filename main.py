import streamlit as st
import math

def calcula_ist(tibc, latente_iron):
    ist = (tibc / (tibc + latente_iron)) * 100
    return f'TIBC: {tibc}', f'IST: {ist:.2f}%'


def calcula_glicose_estimada(hemoglobina_glicada):
    resultado = ((28.7 * hemoglobina_glicada) - 46.7)
    return f'Resultado da Glicose Estimada: {resultado:.2f}'


def calcula_homa(glicose, insulina):
    res1 = ((glicose * 0.0555) * insulina / 22.5)
    res2 = ((((20 * insulina) / ((glicose * 0.0555) - 3.5)) * 1))
    return f'HOMA IR é: {res1:.2f}', f'HOMA BETA é: {res2:.2f}'


def calculo_calcio_ionico(calcio, proteina, albumina):
    calcio_ionico = (6 * calcio - (((0.19 * proteina) + albumina) / 3)) / ((0.19 * proteina) + albumina + 6)
    calcio_ionico_mmol = calcio_ionico * 0.25
    return f'Cálcio Iônico (mg/dL): {calcio_ionico:.2f}', f'Cálcio Iônico (mmol/L): {calcio_ionico_mmol:.2f}'


def fatorLdl(col, hdl, varTrig):
    varNonHdl = col - hdl

    if varTrig >= 7 and varTrig <= 49 and varNonHdl < 100:
        varFator = 3.5

    elif varTrig >= 7 and varTrig <= 49 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 3.4

    elif varTrig >= 7 and varTrig <= 49 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 3.3

    elif varTrig >= 7 and varTrig <= 49 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 3.4

    elif varTrig >= 7 and varTrig <= 49 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 3.2

    elif varTrig >= 7 and varTrig <= 49 and varNonHdl >= 220:
        varFator = 3.1


    # inicio do texto modificado

    elif varTrig >= 50 and varTrig <= 56 and varNonHdl < 100:
        varFator = 4

    elif varTrig >= 50 and varTrig <= 56 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 3.9

    elif varTrig >= 50 and varTrig <= 56 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 3.7

    elif varTrig >= 50 and varTrig <= 56 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 3.6

    elif varTrig >= 50 and varTrig <= 56 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 3.6

    elif varTrig >= 50 and varTrig <= 56 and varNonHdl >= 220:
        varFator = 3.4

    # Final do bloco de modelo

    # Intervalo de 57 a 61

    elif varTrig >= 57 and varTrig <= 61 and varNonHdl < 100:
        varFator = 4.3

    elif varTrig >= 57 and varTrig <= 61 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 4.1

    elif varTrig >= 57 and varTrig <= 61 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 4

    elif varTrig >= 57 and varTrig <= 61 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 3.9

    elif varTrig >= 57 and varTrig <= 61 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 3.8

    elif varTrig >= 57 and varTrig <= 61 and varNonHdl >= 220:
        varFator = 3.6

    # Intervalo de 62 a 66

    elif varTrig >= 62 and varTrig <= 66 and varNonHdl < 100:
        varFator = 4.5

    elif varTrig >= 62 and varTrig <= 66 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 4.3

    elif varTrig >= 62 and varTrig <= 66 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 4.1

    elif varTrig >= 62 and varTrig <= 66 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 4

    elif varTrig >= 62 and varTrig <= 66 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 3.9

    elif varTrig >= 62 and varTrig <= 66 and varNonHdl >= 220:
        varFator = 3.9

        # Intervalo de 67 a 71

    elif varTrig >= 67 and varTrig <= 71 and varNonHdl < 100:
        varFator = 4.7

    elif varTrig >= 67 and varTrig <= 71 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 4.4

    elif varTrig >= 67 and varTrig <= 71 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 4.3

    elif varTrig >= 67 and varTrig <= 71 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 4.2

    elif varTrig >= 67 and varTrig <= 71 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 4.1

    elif varTrig >= 67 and varTrig <= 71 and varNonHdl >= 220:
        varFator = 3.9

    # Intervalo de 72 a 75

    elif varTrig >= 72 and varTrig <= 75 and varNonHdl < 100:
        varFator = 4.8

    elif varTrig >= 72 and varTrig <= 75 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 4.6

    elif varTrig >= 72 and varTrig <= 75 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 4.4

    elif varTrig >= 72 and varTrig <= 75 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 4.2

    elif varTrig >= 72 and varTrig <= 75 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 4.2

    elif varTrig >= 72 and varTrig <= 75 and varNonHdl >= 220:
        varFator = 4.1

        # Intervalo de 76 a 79

    elif varTrig >= 76 and varTrig <= 79 and varNonHdl < 100:
        varFator = 4.9

    elif varTrig >= 76 and varTrig <= 79 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 4.6

    elif varTrig >= 76 and varTrig <= 79 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 4.5

    elif varTrig >= 76 and varTrig <= 79 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 4.3

    elif varTrig >= 76 and varTrig <= 79 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 4.3

    elif varTrig >= 76 and varTrig <= 79 and varNonHdl >= 220:
        varFator = 4.2

        # Intervalo de 80 a 83
    elif varTrig >= 80 and varTrig <= 83 and varNonHdl < 100:
        varFator = 5

    elif varTrig >= 80 and varTrig <= 83 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 4.8

    elif varTrig >= 80 and varTrig <= 83 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 4.6

    elif varTrig >= 80 and varTrig <= 83 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 4.4

    elif varTrig >= 80 and varTrig <= 83 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 4.3

    elif varTrig >= 80 and varTrig <= 83 and varNonHdl >= 220:
        varFator = 4.2

    # Intervalo de 84 a 87

    elif varTrig >= 84 and varTrig <= 87 and varNonHdl < 100:
        varFator = 5.1

    elif varTrig >= 84 and varTrig <= 87 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 4.8

    elif varTrig >= 84 and varTrig <= 87 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 4.6

    elif varTrig >= 84 and varTrig <= 87 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 4.5

    elif varTrig >= 84 and varTrig <= 87 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 4.4

    elif varTrig >= 84 and varTrig <= 87 and varNonHdl >= 220:
        varFator = 4.3

    # Intervalo de 88 a 92

    elif varTrig >= 88 and varTrig <= 92 and varNonHdl < 100:
        varFator = 5.2

    elif varTrig >= 88 and varTrig <= 92 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 4.9

    elif varTrig >= 88 and varTrig <= 92 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 4.7

    elif varTrig >= 88 and varTrig <= 92 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 4.6

    elif varTrig >= 88 and varTrig <= 92 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 4.4

    elif varTrig >= 88 and varTrig <= 92 and varNonHdl >= 220:
        varFator = 4.3

    # Intervalo de 93 a 96

    elif varTrig >= 93 and varTrig <= 96 and varNonHdl < 100:
        varFator = 5.3

    elif varTrig >= 93 and varTrig <= 96 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 5

    elif varTrig >= 93 and varTrig <= 96 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 4.8

    elif varTrig >= 93 and varTrig <= 96 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 4.7

    elif varTrig >= 93 and varTrig <= 96 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 4.5

    elif varTrig >= 93 and varTrig <= 96 and varNonHdl >= 220:
        varFator = 4.4

    # Intervalo de 97 a 100

    elif varTrig >= 97 and varTrig <= 100 and varNonHdl < 100:
        varFator = 5.4

    elif varTrig >= 97 and varTrig <= 100 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 5.1

    elif varTrig >= 97 and varTrig <= 100 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 4.8

    elif varTrig >= 97 and varTrig <= 100 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 4.7

    elif varTrig >= 97 and varTrig <= 100 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 4.5

    elif varTrig >= 97 and varTrig <= 100 and varNonHdl >= 220:
        varFator = 4.3

    # Intervalo de 101 a 105

    elif varTrig >= 101 and varTrig <= 105 and varNonHdl < 100:
        varFator = 5.5

    elif varTrig >= 101 and varTrig <= 105 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 5.2

    elif varTrig >= 101 and varTrig <= 105 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 5

    elif varTrig >= 101 and varTrig <= 105 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 4.7

    elif varTrig >= 101 and varTrig <= 105 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 4.6

    elif varTrig >= 101 and varTrig <= 105 and varNonHdl >= 220:
        varFator = 4.5

    # Intervalo de 106 a 110

    elif varTrig >= 106 and varTrig <= 110 and varNonHdl < 100:
        varFator = 5.6

    elif varTrig >= 106 and varTrig <= 110 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 5.3

    elif varTrig >= 106 and varTrig <= 110 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 5

    elif varTrig >= 106 and varTrig <= 110 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 4.8

    elif varTrig >= 106 and varTrig <= 110 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 4.6

    elif varTrig >= 106 and varTrig <= 110 and varNonHdl >= 220:
        varFator = 4.5

    # Intervalo de 111 a 115

    elif varTrig >= 111 and varTrig <= 115 and varNonHdl < 100:
        varFator = 5.7

    elif varTrig >= 111 and varTrig <= 115 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 5.4

    elif varTrig >= 111 and varTrig <= 115 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 5.1

    elif varTrig >= 111 and varTrig <= 115 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 4.9

    elif varTrig >= 111 and varTrig <= 115 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 4.7

    elif varTrig >= 111 and varTrig <= 115 and varNonHdl >= 220:
        varFator = 4.5

    # Intervalo de 116 a 120

    elif varTrig >= 116 and varTrig <= 120 and varNonHdl < 100:
        varFator = 5.8

    elif varTrig >= 116 and varTrig <= 120 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 5.5

    elif varTrig >= 116 and varTrig <= 120 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 5.2

    elif varTrig >= 116 and varTrig <= 120 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 5

    elif varTrig >= 116 and varTrig <= 120 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 4.8

    elif varTrig >= 116 and varTrig <= 120 and varNonHdl >= 220:
        varFator = 4.6

    # Intervalo de 121 a 126

    elif varTrig >= 121 and varTrig <= 126 and varNonHdl < 100:
        varFator = 6

    elif varTrig >= 121 and varTrig <= 126 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 5.5

    elif varTrig >= 121 and varTrig <= 126 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 5.3

    elif varTrig >= 121 and varTrig <= 126 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 5

    elif varTrig >= 121 and varTrig <= 126 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 4.8

    elif varTrig >= 121 and varTrig <= 126 and varNonHdl >= 220:
        varFator = 4.6

    # Intervalo de 127 a 132

    elif varTrig >= 127 and varTrig <= 132 and varNonHdl < 100:
        varFator = 6.1

    elif varTrig >= 127 and varTrig <= 132 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 5.7

    elif varTrig >= 127 and varTrig <= 132 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 5.3

    elif varTrig >= 127 and varTrig <= 132 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 5.1

    elif varTrig >= 127 and varTrig <= 132 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 4.9

    elif varTrig >= 127 and varTrig <= 132 and varNonHdl >= 220:
        varFator = 4.7

    # Intervalo de 133 a 138

    elif varTrig >= 133 and varTrig <= 138 and varNonHdl < 100:
        varFator = 6.2

    elif varTrig >= 133 and varTrig <= 138 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 5.8

    elif varTrig >= 133 and varTrig <= 138 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 5.4

    elif varTrig >= 133 and varTrig <= 138 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 5.2

    elif varTrig >= 133 and varTrig <= 138 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 5

    elif varTrig >= 133 and varTrig <= 138 and varNonHdl >= 220:
        varFator = 4.7

    # Intervalo de 139 a 146

    elif varTrig >= 139 and varTrig <= 146 and varNonHdl < 100:
        varFator = 6.3

    elif varTrig >= 139 and varTrig <= 146 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 5.9

    elif varTrig >= 139 and varTrig <= 146 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 5.6

    elif varTrig >= 139 and varTrig <= 146 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 5.3

    elif varTrig >= 139 and varTrig <= 146 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 5

    elif varTrig >= 139 and varTrig <= 146 and varNonHdl >= 220:
        varFator = 4.8

    # Intervalo de 147 a 154

    elif varTrig >= 147 and varTrig <= 154 and varNonHdl < 100:
        varFator = 6.5

    elif varTrig >= 147 and varTrig <= 154 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 6

    elif varTrig >= 147 and varTrig <= 154 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 5.7

    elif varTrig >= 147 and varTrig <= 154 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 5.4

    elif varTrig >= 147 and varTrig <= 154 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 5.1

    elif varTrig >= 147 and varTrig <= 154 and varNonHdl >= 220:
        varFator = 4.8

    # Intervalo de 155 a 163

    elif varTrig >= 155 and varTrig <= 163 and varNonHdl < 100:
        varFator = 6.7

    elif varTrig >= 155 and varTrig <= 163 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 6.2

    elif varTrig >= 155 and varTrig <= 163 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 5.8

    elif varTrig >= 155 and varTrig <= 163 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 5.4

    elif varTrig >= 155 and varTrig <= 163 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 5.2

    elif varTrig >= 155 and varTrig <= 163 and varNonHdl >= 220:
        varFator = 4.9

    # Intervalo de 164 a 173

    elif varTrig >= 164 and varTrig <= 173 and varNonHdl < 100:
        varFator = 6.8

    elif varTrig >= 164 and varTrig <= 173 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 6.3

    elif varTrig >= 164 and varTrig <= 173 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 5.9

    elif varTrig >= 164 and varTrig <= 173 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 5.5

    elif varTrig >= 164 and varTrig <= 173 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 5.3

    elif varTrig >= 164 and varTrig <= 173 and varNonHdl >= 220:
        varFator = 5

    # Intervalo de 174 a 185

    elif varTrig >= 174 and varTrig <= 185 and varNonHdl < 100:
        varFator = 7

    elif varTrig >= 174 and varTrig <= 185 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 6.5

    elif varTrig >= 174 and varTrig <= 185 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 6

    elif varTrig >= 174 and varTrig <= 185 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 5.7

    elif varTrig >= 174 and varTrig <= 185 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 5.4

    elif varTrig >= 164 and varTrig <= 173 and varNonHdl >= 220:
        varFator = 5.1

    # Intervalo de 186 a 201

    elif varTrig >= 186 and varTrig <= 201 and varNonHdl < 100:
        varFator = 7.3

    elif varTrig >= 186 and varTrig <= 201 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 6.7

    elif varTrig >= 186 and varTrig <= 201 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 6.2

    elif varTrig >= 186 and varTrig <= 201 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 5.8

    elif varTrig >= 186 and varTrig <= 201 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 5.5

    elif varTrig >= 186 and varTrig <= 201 and varNonHdl >= 220:
        varFator = 5.2

    # Intervalo de 202 a 220

    elif varTrig >= 202 and varTrig <= 220 and varNonHdl < 100:
        varFator = 7.6

    elif varTrig >= 202 and varTrig <= 220 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 6.9

    elif varTrig >= 202 and varTrig <= 220 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 6.4

    elif varTrig >= 202 and varTrig <= 220 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 6

    elif varTrig >= 202 and varTrig <= 220 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 5.6

    elif varTrig >= 202 and varTrig <= 220 and varNonHdl >= 220:
        varFator = 5.3

    # Intervalo de 221 a 247

    elif varTrig >= 221 and varTrig <= 247 and varNonHdl < 100:
        varFator = 8

    elif varTrig >= 221 and varTrig <= 247 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 7.2

    elif varTrig >= 221 and varTrig <= 247 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 6.6

    elif varTrig >= 221 and varTrig <= 247 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 6.2

    elif varTrig >= 221 and varTrig <= 247 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 5.9

    elif varTrig >= 221 and varTrig <= 247 and varNonHdl >= 220:
        varFator = 5.4

    # Intervalo de 248 a 292

    elif varTrig >= 248 and varTrig <= 292 and varNonHdl < 100:
        varFator = 8.5

    elif varTrig >= 248 and varTrig <= 292 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 7.6

    elif varTrig >= 248 and varTrig <= 292 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 7

    elif varTrig >= 248 and varTrig <= 292 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 6.5

    elif varTrig >= 248 and varTrig <= 292 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 6.1

    elif varTrig >= 248 and varTrig <= 292 and varNonHdl >= 220:
        varFator = 5.6

    # Intervalo de 293 a 399

    elif varTrig >= 293 and varTrig <= 399 and varNonHdl < 100:
        varFator = 9.5

    elif varTrig >= 293 and varTrig <= 399 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 8.3

    elif varTrig >= 293 and varTrig <= 399 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 7.5

    elif varTrig >= 293 and varTrig <= 399 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 7

    elif varTrig >= 293 and varTrig <= 399 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 6.5

    elif varTrig >= 293 and varTrig <= 399 and varNonHdl >= 220:
        varFator = 5.9

    # Intervalo de 400 a 13975

    elif varTrig >= 400 and varTrig <= 13975 and varNonHdl < 100:
        varFator = 11.9

    elif varTrig >= 400 and varTrig <= 13975 and varNonHdl >= 100 and varNonHdl <= 129:
        varFator = 10

    elif varTrig >= 400 and varTrig <= 13975 and varNonHdl >= 130 and varNonHdl <= 159:
        varFator = 8.8

    elif varTrig >= 400 and varTrig <= 13975 and varNonHdl >= 160 and varNonHdl <= 189:
        varFator = 8.1

    elif varTrig >= 400 and varTrig <= 13975 and varNonHdl >= 190 and varNonHdl <= 219:
        varFator = 7.5

    elif varTrig >= 400 and varTrig <= 13975 and varNonHdl >= 220:
        varFator = 6.7

    # calculos

    ldl_calc = (varNonHdl - (varTrig / varFator))

    # calculo de Friedewald

    vldl = varTrig/5
    ldl_fw = col - (hdl + vldl)

    return varFator, varNonHdl, ldl_calc, vldl, ldl_fw

    #return f'Cálcio Iônico (mg/dL): {calcio_ionico:.2f}', f'Cálcio Iônico (mmol/L): {calcio_ionico_mmol:.2f}'



def calcula_ldl_martin():
    colesterol = st.number_input('Digite o valor do Colesterol (mg/dL):')
    hdl = st.number_input('Digite o valor do HDL (mg/dL):')
    triglicerides = st.number_input('Digite o valor do Triglierides (mg/dL):')
    if st.button('Calcular'):
        resultado1, resultado2, resultado3, resultado4, resultado5 = fatorLdl(colesterol, hdl, triglicerides)

        st.write("-----Resultado pela Fórmula de Martin-----")
        st.write(" ")
        st.write(f'Fator da Tabela de Martin: {resultado1}')
        st.write(f'Colesterol Não HDL (mg/dL): {resultado2:.0f}')
        st.write(f'Coletestol LDL (mg/dL): {resultado3:.0f}')
        st.write(" ")
        st.write("-----Resultado pela Fórmula de Friedewald-----")
        st.write(" ")
        st.write(f'Coletestol LDL (mg/dL): {resultado5:.0f}')
        st.write(f'Coletestol VLDL (mg/dL): {resultado4:.0f}')

def calcula_proteinas():
    proteina_total = st.number_input('Digite o valor das Proteínas Totais (g/L):')
    albumina = st.number_input('Digite o valor da Albumina (g/L):')
    if st.button('Calcular'):
        globulinas = proteina_total - albumina
        relacao_ag = albumina / globulinas if globulinas != 0 else "Indefinido"
        st.write(f'Globulinas (g/L): {globulinas:.2f}')
        st.write(f'Relação A/G: {relacao_ag:.2f}' if isinstance(relacao_ag, float) else relacao_ag)


def calcula_clearance_creatinina():
    peso = st.number_input('Peso (kg):')
    altura = st.number_input('Altura (cm):')
    creatinina_urina = st.number_input('Creatinina na urina (mg/dL):')
    creatinina_soro = st.number_input('Creatinina no soro (mg/dL):')
    volume_urina = st.number_input('Volume de urina (em 24 horas):')

    if st.button('Calcular'):
        superficie_corporal = 0.007184 * (altura ** 0.725) * (peso ** 0.425)
        volume_urinario_min = volume_urina / 1440
        depuracao = (creatinina_urina / creatinina_soro) * volume_urinario_min
        clearance = (depuracao * 1.73) / superficie_corporal if superficie_corporal != 0 else "Indefinido"

        st.write(f'Superfície corporal (m²): {superficie_corporal:.2f}')
        st.write(f'Volume urinário por Min: {volume_urinario_min:.2f}')
        st.write(f'Depuração: {depuracao:.2f}')
        st.write(f'Clearence (mL/min/1,73m²): {clearance:.2f}' if isinstance(clearance, float) else clearance)


def calcula_glicose():
    hemoglobina_glicada = st.number_input('Digite o valor da Hemoglobina Glicada (%):')
    if st.button('Calcular'):
        resultado_glicose = calcula_glicose_estimada(hemoglobina_glicada)
        st.write(resultado_glicose)


def calcula_homa_ir_beta():

    glicose = st.number_input('Digite o valor da Glicose (mg/dL):')
    insulina = st.number_input('Digite o valor da Insulina (uUI/mL):')
    if st.button('Calcular'):
        res1, res2 = calcula_homa(glicose, insulina)
        st.write(res1)
        st.write(res2)


def calcula_calcio_ionico():
    calcio = st.number_input('Digite o valor do Cálcio (mg/dL):')
    proteina = st.number_input('Digite o valor da Proteína (g/dL):')
    albumina = st.number_input('Digite o valor da Albumina (g/dL):')
    if st.button('Calcular'):
        resultado_calcio_ionico, resultado_calcio_ionico_mmol = calculo_calcio_ionico(calcio, proteina, albumina)
        st.write(resultado_calcio_ionico)
        st.write(resultado_calcio_ionico_mmol)

def calcular_resultados(shbg, testo):
    resultado1 = (
        (
            (
                (
                    (
                        (
                            (shbg - (testo * 0.03467) + 23.43) * (-1)
                        ) + math.sqrt(
                            (
                                (shbg - (testo * 0.03467) + 23.43) ** 2
                            ) - (4 * (10000000000) * 23.43 * ((testo * 0.03467) / (10**10) * (-1)))
                        )
                    )
                ) / (2 * (10000000000) * 23.43)
            ) * 288.5
        ) * 1000000000
    )

    resultado2 = resultado1 + ((resultado1 * 3.6 * (10**4) * 4.3 * 10) / 69000)

    resultado3 = (((testo / 100) * 3.467) * 100) / shbg  # Nova fórmula

    return resultado1, resultado2, resultado3


def calcula_tap_inr(tp_paciente, tp_pool_normal, isi):
    resultado_inr = (tp_paciente / tp_pool_normal) ** isi
    return resultado_inr
def calcula_ttp_ratio(ttp_paciente, ttp_pool_normal):
    resultado_ratio = ttp_paciente / ttp_pool_normal
    return resultado_ratio


def calcula_tap_inr_section():
    st.header('TAP/INR')
    tp_paciente = st.number_input('TP do paciente (segundos):')
    tp_pool_normal = st.number_input('TP do pool normal (segundos):')
    isi = st.number_input('ISI (Índice de Sensibilidade Internacional) - fabricante:')

    if st.button('Calcular'):
        resultado_inr = calcula_tap_inr(tp_paciente, tp_pool_normal, isi)
        st.write(f'INR: {resultado_inr:.2f}')


    # TTPA

    st.header('TTP/Ratio')
    ttp_paciente = st.number_input('TTPA - Paciente (Segundos):')
    ttp_pool_normal = st.number_input('TTPA - Pool Normal (Segundos):')

    if st.button('Calc. Ratio'):
        resultado_ratio = calcula_ttp_ratio(ttp_paciente, ttp_pool_normal)
        st.write(f'Ratio: {resultado_ratio:.2f}')


def calcula_leucocitos_corrigido(numero_eritroblastos, numero_leucocitos):
    resultado_leucocitos_corrigido = (numero_leucocitos * 100) / (numero_eritroblastos + 100)
    return resultado_leucocitos_corrigido


def calcula_leucocitos_corrigido_section():
    st.header('Número de Leucócitos Corrigido')
    numero_eritroblastos = st.number_input('Número de Eritroblastos Contados:')
    numero_leucocitos = st.number_input('Número de Leucócitos (Equipamento):')

    if st.button('Calcular'):
        resultado_leucocitos_corrigido = calcula_leucocitos_corrigido(numero_eritroblastos, numero_leucocitos)
        st.write(f'Número de Leucócitos Corrigido: {resultado_leucocitos_corrigido:.0f}')


def calcula_calcio_24horas(calcio, volume_24horas):
    resultado_calcio_24horas = (calcio * volume_24horas) / 100
    return resultado_calcio_24horas

def calcula_prot_24horas  (proteina, volume_24horas):
    resultado_prot_24horas = (proteina * volume_24horas) / 100
    return resultado_prot_24horas


def calcula_24horas_section():
    st.header('Cálcio em 24 Horas')
    calcio = st.number_input('Cálcio (mg/dL):')
    volume_24horas = st.number_input('Volume em 24 Horas (mL):')

    if st.button('Calcular'):
        resultado_calcio_24horas = calcula_calcio_24horas(calcio, volume_24horas)
        st.write(f'Cálcio em 24 Horas (mg/24horas): {resultado_calcio_24horas:.2f}')

    #proteina
    st.header('Proteína (mg/dL)')
    proteina = st.number_input('Proteína (mg/dL):')
    volume_24horas_pt = st.number_input('Volume em 24 Horas (mL)(pt):')

    if st.button('Calc.Prot'):
        resultado_prot_24horas = calcula_prot_24horas(proteina, volume_24horas_pt)
        st.write(f'Proteína(mg/24 horas): {resultado_prot_24horas:.2f}')


def calcula_fg(crt_soro, idade, sexo):
    if sexo == "Masculino":
        nao_negros = (186 * (crt_soro ** (-1.154)) * (idade ** (-0.203)))
        negros = nao_negros * 1.212
        return nao_negros, negros
    elif sexo == "Feminino":
        nao_negros = (186 * (crt_soro ** (-1.154)) * (idade ** (-0.203))) * 0.742
        negros = ((186 * (crt_soro ** (-1.154)) * (idade ** (-0.203))) * 1.212) * 0.742
        return nao_negros, negros


def calcula_fg_section():
    st.header('Filtração Glomerular')
    st.text("Esse cálculo utiliza a formula de MDRD SIMPLIFICADO")
    crt_soro = st.number_input('Creatinina no soro (mg/dL):')
    idade = st.number_input('Idade:')
    sexo = st.selectbox('Sexo:', ('Masculino', 'Feminino'))

    if st.button('Calcular'):
        resultado_nao_negros, resultado_negros = calcula_fg(crt_soro, idade, sexo)
        st.write(f'Não Negros: {resultado_nao_negros:.2f}')
        st.write(f'Negros....: {resultado_negros:.2f}')


# inicio da parte grafica
st.title('Cálculos em Análises Clinicas')

escolha = st.sidebar.selectbox("Selecione uma opção", ["Humano", "Veterinário"])

if escolha == "Humano":



    menu_option = st.sidebar.selectbox("Calculos em analises clinicas ", (" ","LDL (Martin)",
"Glicose Estimada", "Calc. Testosterona", "Calc. Ferro", "Calculo de homa", "Cálcio Iônico", "Prot. Total e frações",
"Clearence de Creatinina","TAP/INR","Correção de Eritroblastos","Cálcula Urina 24 horas","Filtração Glomerular"))


    if menu_option == 'Calc. Ferro':

        st.text('Capacidade Total de Fixação do Ferro (TIBC) e Índice de Saturação da Transferrina (IST)')
        tibc = st.number_input('Digite o valor do Ferro (ug/dL):')
        latente_iron = st.number_input('Digite o valor da Capacidade Latente Ligação do Ferro:')
        if st.button('Calcular'):
            resultado_tibc, resultado_ist = calcula_ist(tibc, latente_iron)
            st.write(resultado_tibc)
            st.write(resultado_ist)


    elif menu_option == 'Glicose Estimada':

        st.text('Gilocose Estimada')
        calcula_glicose()

    elif menu_option == "Filtração Glomerular":
        calcula_fg_section()

    elif menu_option == "TAP/INR":
        calcula_tap_inr_section()


    elif menu_option == 'LDL (Martin)':


        st.markdown("<h1 style='font-size: 24px;'>Frações de colesterol</h1>", unsafe_allow_html=True)


        calcula_ldl_martin()


    elif menu_option == 'Calc. Testosterona':
        st.header('Testosterona')
        shbg = st.number_input('Digite o valor de SHBG (nmol/L):')
        testo = st.number_input('Digite o valor da Testosterona Total (ng/dL):')
        if st.button('Calcular'):
            resultado1, resultado2, resultado3 = calcular_resultados(shbg, testo)
            st.write(f'Testosterona livre: {resultado1:.2f}')
            st.write(f'Testosterona biodisponível: {resultado2:.2f}')
            st.write(f'Índice de Androgênios Livres: {resultado3:.2f}')


    elif menu_option == 'Calculo de homa':
        st.text('Cálculo do HOMA')
        calcula_homa_ir_beta()


    elif menu_option == 'Cálcio Iônico':
        st.text('Cálculo do Cálcio Iônico')
        calcula_calcio_ionico()

    elif menu_option == 'Prot. Total e frações':
        st.text('Prot. Total e frações')
        calcula_proteinas()

    elif menu_option == 'Clearence de Creatinina':
        st.text('Clearence de Creatinina')
        calcula_clearance_creatinina()

    elif menu_option == "Correção de Eritroblastos":
        calcula_leucocitos_corrigido_section()

    elif menu_option == "Cálcula Urina 24 horas":
        calcula_24horas_section()


    else:
        # st.text("Escolha a opção desejada no menu ao lado.")
        st.markdown("<h1 style='font-size: 24px;'>Escolha a opção desejada no menu ao lado</h1>",
                    unsafe_allow_html=True)



elif escolha == "Veterinário":

    menu_option = st.sidebar.selectbox("Calculos em analises vet ", (" "))
