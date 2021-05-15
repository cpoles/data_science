deck <- read.csv("~/Programming/data_science/R/R_hands_on/R_Objects/deck.csv")

write.csv(deck, file = "cards.csv", row.names = FALSE)
