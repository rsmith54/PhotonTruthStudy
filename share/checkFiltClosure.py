
filteff = {
    "CVetoBVeto": {
        211: {"GammaPt0":     0.41028,
              "GammaPt70":    0.39960,
              "GammaPt140":   0.41049,
              "GammaPt280":   0.41834,
              "GammaPt500":   0.38226,
              "GammaPt1000":  0.37036,
              "GammaPt2000":  0.38030,
              "GammaPt4000":  0.40351,
              "ZPt0":         0.77837,
              "ZPt70":        0.64863,
              "ZPt140":       0.60566,
              "ZPt280":       0.49112,
              "ZPt500":       0.54643,
              "ZPt700":       0.57944,
              "ZPt1000":      0.35762,
              },
        145: {"GammaPt140":   0.42556,
              "GammaPt280":   0.40983,
              "GammaPt500":   0.39686,
              "ZPt0":         0.63727,
              "ZPt70":        0.50634,
              "ZPt140":       0.47131,
              "ZPt280":       0.44226,
              "ZPt500":       0.41562,
              }
        },
    "CFilterBVeto": {
        211: {"GammaPt0":     0.48609,
              "GammaPt70":    0.48199,
              "GammaPt140":   0.50284,
              "GammaPt280":   0.47349,
              "GammaPt500":   0.47148,
              "GammaPt1000":  0.46691,
              "GammaPt2000":  0.45148,
              "GammaPt4000":  0.41614,
              "ZPt0":         0.14008,
              "ZPt70":        0.21209,
              "ZPt140":       0.22794,
              "ZPt280":       0.23583,
              "ZPt500":       0.25074,
              "ZPt700":       0.20360,
              "ZPt1000":      0.19538,
              },
        145: {"GammaPt140":   0.47310,
              "GammaPt280":   0.46833,
              "GammaPt500":   0.46546,
              "ZPt0":         0.32350,
              "ZPt70":        0.39045,
              "ZPt140":       0.40475,
              "ZPt280":       0.43294,
              "ZPt500":       0.43676,
              }
        },
    "BFilter": {
        211: {"GammaPt0":     0.10752,
              "GammaPt70":    0.11728,
              "GammaPt140":   0.12874,
              "GammaPt280":   0.14069,
              "GammaPt500":   0.14811,
              "GammaPt1000":  0.15751,
              "GammaPt2000":  0.16549,
              "GammaPt4000":  0.14831,
              "ZPt0":         0.079239,
              "ZPt70":        0.12738,
              "ZPt140":       0.13435,
              "ZPt280":       0.074043,
              "ZPt500":       0.12721,
              "ZPt700":       0.17925,
              "ZPt1000":      0.13404,
              },
        145: {"GammaPt140":   0.10098,
              "GammaPt280":   0.12017,
              "GammaPt500":   0.13950,
              "ZPt0":         0.039883,
              "ZPt70":        0.10310,
              "ZPt140":       0.11957,
              "ZPt280":       0.13493,
              "ZPt500":       0.14685,
              }
        }
}

for version in [145,211]:
    for boson in ["Gamma","Z"]:
        for ptcut in [0,70,140,280,500,700,1000]:
            key = "{0}Pt{1}".format(boson,ptcut)
            totfilteff = 0.
            for flavour in ["CVetoBVeto","CFilterBVeto","BFilter"]:
                if key in filteff[flavour][version].keys():
                    totfilteff += filteff[flavour][version][key]
            print version, key, totfilteff
