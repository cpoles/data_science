##########
#  EDA   #
##########

library(tidyverse)
library(ggstance)
library(nycflights13)


# Visualising categorical variable distributions
ggplot(data = diamonds) +
  geom_bar(mapping = aes(x = cut))

# counting occurences of the categories of cut variable
diamonds %>%
  count(cut)

# visualising continuous variable distribution
ggplot(data = diamonds) +
  geom_histogram(mapping = aes(x = carat), binwidth = 0.5)

diamonds %>%
  count(cut_width(carat, 0.5))

smaller <- diamonds %>%
  filter(carat < 3)

ggplot(data = smaller, mapping = aes(x = carat)) +
  geom_histogram(binwidth = 0.1)

# overlay histograms
ggplot(data = smaller, mapping = aes(x = carat, color=cut)) +
  geom_freqpoly(binwidth = 0.1)

# smaller bin
ggplot(data = smaller, mapping = aes(x = carat)) +
  geom_histogram(binwidth = 0.01)

# distribution of x
diamonds %>%
  ggplot(mapping = aes(x = x)) +
  geom_histogram(binwidth = 0.01)

# distribution of y
diamonds %>%
  ggplot(mapping = aes(x = y)) +
  geom_histogram(binwidth = 0.1) +
  coord_cartesian(xlim = c(0, 60))

# distribution of z
diamonds %>%
  ggplot(mapping = aes(x = z)) +
  geom_histogram(binwidth = 0.01) +
  coord_cartesian(xlim = c(0, 12))

diamonds %>%
  filter(carat == 1.00) %>%
  count()

# replacing outliers
# y < 3 and y > 20
diamonds2 <- diamonds %>%
  mutate(y = ifelse(y < 3 | y > 20, NA, y))

ggplot(data = diamonds2, mapping = aes(x = x, y = y), alpha=1/10) +
  geom_point()

# boxplot comparing categorical and continuous variables
ggplot(data = diamonds, mapping = aes(x = cut, y = price)) +
  geom_boxplot()

# hwy mileage vs class
ggplot(data = mpg, mapping = aes(x = class, y = hwy)) +
  geom_boxplot()

# reording previous based on the median
ggplot(data = mpg) +
  geom_boxplot(
    mapping = aes(
      x = reorder(class, hwy, FUN = median),
      y = hwy
    )
  )

# flip so that the longer names axis becomes more readable
ggplot(data = mpg) +
  geom_boxplot(
    mapping = aes(
      x = reorder(class, hwy, FUN = median),
      y = hwy
    )
  ) +
  coord_flip()


# horizontal boxplot using ggstance
ggplot(data = mpg) +
  geom_boxploth(
    mapping = aes(
      x = hwy,
      y = reorder(class, hwy, FUN = median) 
    )
  )

# count diamonds by color and cut
diamonds %>% 
  count(color, cut)

# visualise heatmap
diamonds %>% 
  count(color, cut) %>% 
  ggplot(mapping = aes(x = color, y = cut)) +
    geom_tile(mapping = aes(fill = n))

# 
diamonds %>% 
  count(cut, color) %>% 
  ggplot(mapping = aes(x = cut, y = n)) +
    geom_count(mapping = aes(color = color))