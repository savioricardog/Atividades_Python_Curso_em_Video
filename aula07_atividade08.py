medida = float(input("Diga-me uma distancia em metros: "))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('{}m convertido para KM fica {:.4f}, para hm fica {:.3f},'
      '\n''para dam fica {:.3f}, para dm fica {:.0f}, para cm fica {:.0f},'
      '\npara mm fica {:.0f}' .format(medida, km, hm, dam,dm, cm, mm))