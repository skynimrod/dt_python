from matplotlib.pyplot import *

# some simple data
x = [1, 2, 3, 4]
y = [5, 4, 3, 2]

# create new figure
figure()

# divide subplots into 2 x 3 grid
# and select #1
subplot(231)
plot(x, y)

# select #2
subplot(232)
bar(x, y)

# select #3  horizontal bar-charts
subplot(233)
barh(x, y)

# select #4 create stacked bar charts
subplot(234)
bar(x, y)

# select #5 we need more data for stacked bar charts
y1 = [7, 8, 5, 3]
bar(x, y1, bottom=y, color = 'r' )

# box plot
subplot(235)
boxplot(x)

# select #6 scatter plot
subplot(236)
scatter(x, y)

show()