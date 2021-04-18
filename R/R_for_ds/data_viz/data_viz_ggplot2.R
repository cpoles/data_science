# loading tidyverse
library(tidyverse)

# graphing template
ggplot(data = <DATA>) +
  <GEOM_FUNCTION>(mapping = aes(<MAPPINGS>))

# plotting mpg displ vs hwy
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy))


# plotting mpg displ vs hwy
# adding color to the class variable
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy, colour = class))

# experimenting different levels with variable class
# alpha
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy, alpha = class))

# shape
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy, shape = class))

# setting aesthetics of geom_point
# all points are blue
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy), color = 'blue')



### Exercises
# Map a continuous variable to color, size and shape

# color
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy, color = year))

# shape - cant use as it is numerical
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy, shape = year))

# mess
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy, size = year, alpha = year, color = year))

# change size of points using stroke
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy, color = class), stroke = 2)


# conditional format. splits color in < 5 and >= 5
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy, color = displ < 5), stroke = 2)


######################

    # FACETS #

#####################

# facet on class variable
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy)) +
  facet_wrap(~ class, nrow = 2)

# facet on drv and cyl - using facet_grid
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy)) +
  facet_grid(drv ~ cyl)


ggplot(data = mpg) +
  geom_point(mapping = aes(x = drv, y = cyl)) 


ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy)) +
  facet_wrap(~ class, nrow = 2)


#####################

# GEOMETRIC OBJECTS #

#####################

# testing geom point and geom smooth
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy))

ggplot(data = mpg) +
  geom_smooth(mapping = aes(x = displ, y = hwy))


# plotting drv as linetype
ggplot(data = mpg) +
  geom_smooth(mapping = aes(x = displ, y = hwy, linetype = drv))

ggplot(data = mpg) +
  geom_smooth(mapping = aes(x = displ, y = hwy, group = drv))

# removes legend and plot drv as color
ggplot(data = mpg) +
  geom_smooth(
    mapping = aes(x = displ, y = hwy, color = drv),
    show.legend = FALSE
  )

# show multiple geoms
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy)) +
  geom_smooth(mapping = aes(x = displ, y = hwy))


# use a set of mappings to avoid redundancy
ggplot(data = mpg, mapping = aes(x = displ, y = hwy)) +
  geom_point() +
  geom_smooth()


# changing mapping argument for geom_point
ggplot(data = mpg, mapping = aes(x = displ, y = hwy)) +
  geom_point(mapping = aes(color = class)) +
  geom_smooth()


# draw only the subcompact class as a line
ggplot(data = mpg, mapping = aes(x = displ, y = hwy)) +
  geom_point(mapping = aes(color = class)) +
  geom_smooth(
   data = filter(mpg, class == 'subcompact'),
   se = TRUE
  )

# recreate graphs
# use a set of mappings to avoid redundancy
ggplot(data = mpg, mapping = aes(x = displ, y = hwy, color = drv)) +
  geom_point() +
  geom_smooth(
    se = FALSE
  )



ggplot(data = mpg, mapping = aes(x = displ, y = hwy)) +
  geom_point(mapping = aes(color = drv)) +
  geom_smooth(
    se = FALSE
  )


ggplot(data = mpg, mapping = aes(x = displ, y = hwy, color = drv)) +
  geom_point() +
  geom_smooth(
    mapping = aes(linetype = drv),
    se = FALSE
  )

ggplot(data = mpg, mapping = aes(x = displ, y = hwy, color = drv)) +
  geom_point()


