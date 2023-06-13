library(tidyverse)
library(jurimetrics)

setwd('/Users/USERNAME/') # Trocar pelo local desejado

# Ler os dados
fi <- read.csv('./fisicas.csv')
head(fi)
fi$data_semana_comercial <- as.Date(fi$data_semana_comercial)
fi <- arrange(fi, data_semana_comercial, cod_loja)

# Somente para lojas unicas
cod_loja_values <- unique(fi$cod_loja)

# Para cada loja
results <- lapply(cod_loja_values, function(cod_loja) {
  fltr <- fi$cod_loja == cod_loja
  table(fltr)
  summary(fi$data_semana_comercial[fltr])
  
  lj <- ts(fi$venda[fltr], start = c(2017, 01), end = c(2022, 08),
           frequency = 52)
  
  # Modelar a previsão de vendas
  par(mfrow = c(1, 1))
  plot(lj)
  fits(lj, train = 0.7, show.sec.graph = TRUE, PI = FALSE)
})

# Armazenar os resultados em um arquivo chamado Predictions.csv
sink('Predictions.csv')
for (i in seq_along(cod_loja_values)) {
  cod_loja <- cod_loja_values[i]
  cat("Results for cod_loja:", cod_loja, "\n")
  print(results[[i]])
  cat("\n")
}
sink()
