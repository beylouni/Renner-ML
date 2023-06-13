library(tidyverse)
library(jurimetrics)


# Loja 406
fi <- read.csv('./input/clean_data/web.csv')
head(fi)
fi$data_semana_comercial <- as.Date(fi$data_semana_comercial)
fi <- arrange(fi, data_semana_comercial, cod_loja)

fltr <- fi$cod_loja == 406
table(fltr)
summary(fi$data_semana_comercial[fltr])

lj <- ts(fi$venda[fltr], start = c(2020,07), end = c(2022,10),
          frequency = 52)
par(mfrow=c(1,1))
plot(lj)
fits(lj, train = 0.7, show.sec.graph = TRUE, PI = TRUE)
1032
# fits(lj, train = 0.9, show.sec.graph = TRUE, PI = TRUE)


# Loja web
we <- read.csv('./input/clean_data/web.csv')
head(we)
we$data_semana_comercial <- as.Date(we$data_semana_comercial)
we <- arrange(we, data_semana_comercial, cod_loja)

fltr <- we$cod_loja == 407
table(fltr)
summary(we$data_semana_comercial[fltr])

lj <- ts(we$venda[fltr], start = c(2017,01), end = c(2022,10),
         frequency = 52)
par(mfrow=c(1,1))
plot(lj)
fits(lj, train = 0.7, show.sec.graph = TRUE, PI = TRUE)
