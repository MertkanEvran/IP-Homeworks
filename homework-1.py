# Normalizasyon ve Standardizasyon arasında ki farklar?


"""
1-) Normalizasyon
Amaç: Verileri belirli bir araliğa (genellikle [0, 1] araliğina) dönüştürmek.
Formül: X(normalized) = (X - X(min)) / (X(max) - X(min))

Bu işlemle, orijinal veri kümesindeki değerler normalize edilir
ve hepsi [0, 1] araliğinda olur. Normalizasyon, özellikle derin öğrenme modellerinde siklikla kullanilir.


2-) Standardizasyon
Amaç: Verileri ortalamasi 0, standart sapmasi 1 olacak şekilde dönüştürmek.
Formül: X(standardized) = (X - mean(X)) / std(X)

Standardizasyon, veri kümesinin ortalamasini 0'a çeker ve standart sapmasini 1 yapar. Bu, veri setindeki
aykiri değerlere daha dirençli olabilir ve bazi istatistiksel modellerde daha uygun olabilir

"""